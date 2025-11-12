
# Setup ------------------------------------------------------------------------

# File handling:
from pathlib import Path
from yaml import safe_load as yaml_load

# HTML parsing:
from bs4 import BeautifulSoup

# Type hints:
from typing import Any

# Numpy and operations:
import numpy as np
import numpy.random as rd
from numpy.lib.stride_tricks import sliding_window_view
from numpy.typing import NDArray
from operator import eq, lt, gt



# Packing Optimization ---------------------------------------------------------

def pack_discrete_ncols(rectangles: NDArray, ncols: int) -> dict[str, NDArray]:
    # Setup:
    rects = rectangles.copy()
    nrects = rects.shape[0]
    rects = np.hstack((rects, np.arange(1, nrects + 1).reshape(-1, 1))) # Add index column

    ops = [eq, gt, lt] # Order of height preference
    used_flag = np.iinfo(np.int8).max # Flag to mark rectangle as used

    # Initialize loop:
    grid = np.zeros((np.sum(rects[:, 1]), ncols), dtype = np.int8)
    rects_order = np.zeros(nrects, dtype = np.int8)
    i = 1

    # Main loop:
    while i <= nrects:
        # Find current location and available space:
        avail_grid = grid == 0
        cur_h = np.argmax(np.any(avail_grid, axis = 1))
        cur_w = np.argmax(avail_grid[cur_h, :])
        avail_w = np.sum(avail_grid[cur_h, :])
        avail_h = np.sum(np.sum(avail_grid[cur_h:, :], axis = 1) == avail_w)

        # Find rectangles that fit exactly or with >1 space left:
        fits_w = (avail_w - rects[:, 1] >= 0) & (avail_w - rects[:, 1] != 1)
        avail_rects = rects[fits_w, :]

        # Choose rectangle following rect preference:
        chosen_rect = -1
        for op in ops:
            fits_h = op(avail_rects[:, 0], avail_h)
            if np.any(fits_h): # Given h, choose randomly across w
                chosen_rect = rd.choice(avail_rects[:, 2][fits_h])
                break

        # Mark space as 'hole' (-i) or update the grid:
        if chosen_rect == -1:
            grid[cur_h:(cur_h + avail_h), cur_w:(cur_w + avail_w)] = -rects_order[i - 2]
        else:
            rects_order[i - 1] = chosen_rect
            chosen_h, chosen_w, _ = rects[chosen_rect - 1, :]
            grid[cur_h:(cur_h + chosen_h), cur_w:(cur_w + chosen_w)] = chosen_rect

            rects[chosen_rect - 1, 1] = used_flag # Mark as used
            i += 1

    return {"order": rects_order, "grid": grid}


def get_shared_divides(grids: NDArray, axis: int) -> NDArray:
    # axis = 2 for horizontal divides, 1 for vertical divides
    axis_inv = 1 if axis == 2 else 2

    divides = np.diff(grids, axis = axis) != 0
    divides_consecutive = np.all(sliding_window_view(divides, 2, axis = axis_inv), axis = 3)

    different_rects = np.diff(grids, axis = axis_inv) != 0
    different_rects = different_rects[:, :, :-1] if axis == 2 else different_rects[:, :-1, :]

    return np.sum(divides_consecutive & different_rects, axis = (1, 2))


# Debug: `rectangles, ncols, ndraws, verbose = rects, args["ncols"], args.get("ndraws", 100), 1`
def best_pack_draw(
    rectangles: NDArray,
    ncols: int,
    ndraws: int,
    verbose: int = 1
) -> dict[str, NDArray]:
    nrects = rectangles.shape[0]

    if verbose >= 1:
        print((
            f"  - Packing {nrects} rectangles into "
            f"{ncols} columns over {ndraws} draws ..."
        ))

    ords = np.zeros((nrects, ndraws), dtype = np.int8)
    grids = np.zeros((ndraws, np.sum(rectangles[:, 1]), ncols), dtype = np.int8)
    obj = np.zeros(ndraws, dtype = np.int8)

    for draw in range(ndraws):
        if verbose == 2 and (draw + 1) % 10 == 0:
            print(f"- Completed {draw + 1}/{ndraws}")
        res = pack_discrete_ncols(rectangles, ncols)
        ords[:, draw] = res["order"]
        grids[draw, :, :] = res["grid"]
        obj[draw] = np.sum(res["grid"] == -2)

    # Selecting only unique orders:
    ords_unique, idx_unique = np.unique(ords, return_index = True, axis = 1, sorted = False)
    obj_unique, grids_unique = obj[idx_unique], grids[idx_unique, :, :]

    # Selecting grids with least shared divides:
    nholes = np.min(obj_unique)
    contenders = obj_unique == nholes
    grids_contender = grids_unique[contenders, :, :]
    divides_shared = get_shared_divides(grids_contender, 1) + get_shared_divides(grids_contender, 2)

    # Selecting grids with biggest height diversity:
    contenders2 = divides_shared == np.min(divides_shared)
    ords_contenders2 = ords_unique[:, np.where(contenders)[0][contenders2]]
    width_diversity = np.sum(abs(np.diff(rectangles[ords_contenders2 - 1, 0], axis = 0)), axis = 0)

    # Update extra space (0) to hole (-128) if line was 'started'
    last_lines = np.any(grids_unique != 0, axis = 2)
    extra_spaces = grids_unique == 0
    grids_unique[last_lines[:, :, None] & extra_spaces] = np.iinfo(np.int8).min
    # TODO: Change -128 to -i, where i is the index of the last placed rectangle

    # Save results:
    bests = width_diversity == np.max(width_diversity)
    idx = np.where(contenders)[0][np.where(contenders2)[0]][bests]
    out = {
        "nholes": nholes,
        "orders": ords_unique[:, idx],
        "grids": grids_unique[idx, :, :]
    }
    return out



# Gallery Build ----------------------------------------------------------------

def build_gallery(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    path = Path(args["target"], "index.html")
    with open(path, "r", encoding = "utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    with open("src/gallery/images.yaml", "r", encoding = "utf-8") as file:
        items = yaml_load(file) # NOTE: Hardcoded path

    rects = np.zeros((len(items), 2), dtype = np.int8)
    gallery_items = []

    for i, item in enumerate(items.values()):
        h, w = item["size"]
        rects[i, :] = (h, w)
        
        gallery_item = soup.new_tag("div", attrs = {
            "id": Path(item["src"]).stem,
            "class": " ".join(["gallery-item", f"h-{h}", f"w-{w}"]),
            "tabindex": "0"
        })
        gallery_item.append(soup.new_tag("img", attrs = {
            "src": item["src"], "alt": item["alt"], "loading": "lazy",
            "data-description": item["description"],
            "data-where": item["where"],
            "data-when": item["when"]
        }))
        gallery_items.append(gallery_item)

    best = best_pack_draw(rects, args["ncols"], args.get("ndraws", 100))
    gallery_items = [gallery_items[i - 1] for i in best["orders"][:, 0]]

    gallery = soup.select_one(".gallery-grid")
    gallery.clear()
    for gallery_item in gallery_items:
        gallery.append(gallery_item)

    best_grid = best["grids"][0, :, :]
    hole_flag = np.iinfo(np.int8).min
    if np.any(best_grid == hole_flag):
        h, w = (
            np.sum(np.any(best_grid == hole_flag, axis = 0)),
            np.sum(np.any(best_grid == hole_flag, axis = 1))
        )
        gallery.append(
            soup.new_tag("div", attrs = {
                "class": " ".join(["gallery-hole", f"h-{h}", f"w-{w}"])
                
            })
        )

    with open(path, "w", encoding = "utf-8") as file:
        file.write(str(soup))

    return None
