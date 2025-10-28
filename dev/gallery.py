
# Setup ------------------------------------------------------------------------

# Numpy and operations:
import numpy as np
import numpy.random as rd
from numpy.typing import NDArray
from operator import eq, lt, gt

# File handling:
from pathlib import Path
from bs4 import BeautifulSoup



# Packing Optimization ---------------------------------------------------------

def pack_discrete_ncols(rectangles: NDArray, ncols: int) -> dict[str, NDArray]:
    # Setup:
    rects = rectangles.copy()
    nrects = rects.shape[0]
    rects = np.hstack((rects, np.arange(nrects).reshape(-1, 1)))
    ops = [eq, gt, lt] # Order or height preference
    used_flag = np.iinfo(np.int8).max # Flag to mark rectangle as used
    
    # Initialize loop:
    grid = np.full((np.sum(rects[:, 1]), ncols), -1, dtype = np.int8)
    rects_order = np.zeros(nrects, dtype = np.int8)
    i = 0

    # Main loop:
    while i <= nrects - 1:
        # Find current location and available space:
        avail_grid = grid == -1
        cur_h = np.argmax(np.any(avail_grid, axis = 1))
        cur_w = np.argmax(avail_grid[cur_h, :])
        avail_w = np.sum(avail_grid[cur_h, :])
        avail_h = np.sum(np.sum(avail_grid[cur_h:, :], axis = 1) == avail_w)

        # Find rectangles that fit exactly or with >1 space left:
        fits_w = (avail_w - rects[:, 1] >= 0) & (avail_w - rects[:, 1] != 1)
        avail_rects = rects[fits_w, :]

        # Choose rectangle following rect preference:
        chosen_idx = -1
        for op in ops:
            fits_h = op(avail_rects[:, 0], avail_h)
            if np.any(fits_h): # Given h, choose randomly across w
                chosen_idx = rd.choice(avail_rects[:, 2][fits_h])
                break

        # Mark space as 'hole' (-2) or update the grid:
        if chosen_idx == -1:
            grid[cur_h:(cur_h + avail_h), cur_w:(cur_w + avail_w)] = -2
        else:
            rects_order[i] = chosen_idx
            chosen_h, chosen_w, _ = rects[chosen_idx, :]
            grid[cur_h:(cur_h + chosen_h), cur_w:(cur_w + chosen_w)] = chosen_idx

            rects[chosen_idx, 1] = used_flag # Mark as used
            i += 1

    return {"order": rects_order, "grid": grid}


def best_pack_draw(
    rectangles: NDArray,
    ncols: int,
    ndraws: int,
    verbose: int = 1
) -> dict[str, NDArray]:
    if verbose >= 1:
        print((
            f"- Packing {rectangles.shape[0]} rectangles into "
            f"{ncols} columns over {ndraws} draws."
        ))

    orders = np.zeros((rectangles.shape[0], ndraws), dtype = np.int8)
    grids = np.zeros((ndraws, np.sum(rectangles[:, 1]), ncols), dtype = np.int8)
    obj = np.zeros(ndraws, dtype = np.int8)

    for draw in range(ndraws):
        if verbose == 2 and (draw + 1) % 10 == 0:
            print(f"- Completed {draw + 1}/{ndraws}")
        res = pack_discrete_ncols(rectangles, ncols)
        orders[:, draw] = res["order"]
        grids[draw, :, :] = res["grid"]
        obj[draw] = np.sum(res["grid"] == -2)
    
    orders_unique, idx_unique = np.unique(orders, return_index = True, axis = 1, sorted = False)
    obj_unique, grids_unique = obj[idx_unique], grids[idx_unique, :, :]
    idx_sorted = np.argsort(obj_unique)
    out = {
        "nholes": obj_unique[idx_sorted],
        "orders": orders_unique[:, idx_sorted],
        "grids": grids_unique[idx_sorted, :, :]
    }
    return out


# Gallery Build ----------------------------------------------------------------

def build_gallery(steps) -> None:
    print("Job == Building gallery...")

    key, args = list(steps.items())[0]

    path = Path(args["target"], "index.html")
    with open(path, "r", encoding = "utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    items = soup.select(".gallery-grid > img")
    rects = np.zeros((len(items), 2), dtype = np.int8)

    for i in range(len(items)):
        item = items[i]
        h, w = int(item["data-h"]), int(item["data-w"])
        rects[i, :] = (h, w)
        item.wrap(soup.new_tag("div", attrs = {
            "class": ["gallery-item", f"h-{h}", f"w-{w}"],
            "tabindex": "0"
        }))
        del item["data-h"]
        del item["data-w"]

    best = best_pack_draw(rects, args["ncols"], args.get("ndraws", 100))
    items = [items[i] for i in best["orders"][:, 0]]

    gallery = soup.select_one(".gallery-grid")
    gallery.clear()
    for item in items:
        gallery.append(item.parent)

    with open(path, "w", encoding = "utf-8") as file:
        file.write(str(soup))
