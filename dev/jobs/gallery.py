
# Setup ------------------------------------------------------------------------

# File handling:
from pathlib import Path
from yaml import safe_load as yaml_load

# Masonry packing:
import numpy as np
from armasonry import best_pack_draw

# HTML parsing:
from bs4 import BeautifulSoup

# Type hints:
from typing import Any



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
        attrs ={
            "src": item["src"],
            "alt": item["alt"],
            "data-description": item["description"],
            "data-where": item["where"],
            "data-when": item["when"]
        }
        if i > 5: # Lazy loading for images not in the beginning
            attrs["loading"] = "lazy"
        gallery_item.append(soup.new_tag("img", attrs = attrs))
        gallery_items.append(gallery_item)

    best = best_pack_draw(
        rects,
        args["ncols"], args.get("ndraws", 1000),
        args.get("prefs_h", ["true"]), args.get("prefs_w", [])
    )
    gallery_items = [gallery_items[i - 1] for i in best["orders"][:, 0]]

    gallery = soup.select_one(".gallery-grid")
    gallery.clear()
    for gallery_item in gallery_items:
        gallery.append(gallery_item)

    if args.get("fill_holes", False):
        # TODO: Not working properly yet
        best_grid = best["grids"][0, :, :]
        for hole_flag in np.unique(best_grid[best_grid < 0]):
            hole_idx = np.where(best_grid == hole_flag)

            h_first, w_first = hole_idx[0][0], hole_idx[1][0]
            previous_rect = np.max(np.concatenate(
                (best_grid[:h_first, :].ravel(), best_grid[h_first, :w_first].ravel())
            ))

            h, w = len(hole_idx[0]), len(hole_idx[1])
            gallery.insert(
                previous_rect,
                soup.new_tag("div", attrs = {
                    "class": " ".join(["gallery-hole", f"h-{h}", f"w-{w}"])
                })
            )

    with open(path, "w", encoding = "utf-8") as file:
        file.write(str(soup))

    return None
