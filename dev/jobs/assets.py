
# Setup ------------------------------------------------------------------------

# File operations:
from pathlib import Path

# Others:
import re

# Type hints:
from typing import Any

# Local modules:
from jobs.utils import run, move_contents, glob_re



# Moving -----------------------------------------------------------------------

# Move assets to target folder
# step_args:
# - prefix: Optional prefix to add to target path (default: deploy target)
# - exclude: Pattern to exclude files from moving
def assets_move(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print("  - Moving assets ...")

    assets = [
        asset
        for asset in glob_re(args["source"])
        if not re.search(args.get("exclude", ".^"), str(asset))
            and re.search(args.get("include", ".*"), str(asset))
    ]
    
    move_contents(assets, args["target"])
    
    return None


# Remove assets from target folder
# step_args:
# - include: Pattern to include files for removing
def assets_remove(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print("  - Removing assets ...")

    assets = glob_re(args["source"], args["include"])
    for asset in assets:
        asset.unlink()

    return None


def assets_merge(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print("  - Merging assets ...")

    with open(args["target"], "w", encoding = "utf-8") as merged_file:

        for part_path in args["include"]:
            part_path = Path(args["source"], part_path)

            with open(part_path, "r", encoding = "utf-8") as part:
                merged_file.write(part.read() + "\n")

            part_path.unlink()

    return None



# Compiling --------------------------------------------------------------------


# Compile assets (e.g., SCSS to CSS)
# step_args:
# - prefix: Optional prefix to add to target path (default: deploy target)
# - type: Type of asset to compile. Only "css" is supported currently.
def assets_compile(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print("  - Compiling assets ...")

    if (args["type"] == "css"):
        for scss_file in glob_re(args["source"], args.get("include", r".*\.scss")):
            if re.search(args.get("exclude", r"^$"), str(scss_file)):
                continue

            target = Path(
                args["target"],
                scss_file.name.replace(".scss", ".css")
            )

            run(
                "sass", str(scss_file), str(target),
                "--no-source-map", "--load-path=src"
            )

    elif (args["type"] == "latex"):
        for tex_file in glob_re(args["source"], args.get("include", r".*\.tex")):
            if re.search(args.get("exclude", r"^$"), str(tex_file)):
                continue

            run(
                "latexmk", "-pdf", "-xelatex",
                "-interaction=nonstopmode", "-silent",
                "-output-directory=" + str(Path(args["target"])), str(tex_file),
                timeout = 30
            )

            aux_extensions = [".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".xdv"]
            for ext in aux_extensions:
                aux_file = Path(args["target"], tex_file.with_suffix(ext).name)
                if aux_file.exists():
                    aux_file.unlink()

    else:
        raise Exception(f"Compilation type '{args["type"]}' is not supported.")

    return None
