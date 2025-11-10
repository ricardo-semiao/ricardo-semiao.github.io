
# Setup ------------------------------------------------------------------------

# File operations:
from pathlib import Path

# Others:
import re

# Local modules:
from jobs.utils import run, move_contents, glob_re



# Moving -----------------------------------------------------------------------

# Move assets to target folder
# step_args:
# - prefix: Optional prefix to add to target path (default: deploy target)
# - exclude: Pattern to exclude files from moving
def assets_move(steps: dict) -> None:
    print("Job == Moving assets:")

    for key, args in steps.items():
        print(f"  - Moving assets of '{key[0]}' ...")

        assets = [
            asset
            for asset in glob_re(args["source"])
            if not re.search(args.get("exclude", ".^"), str(asset))
                and re.search(args.get("include", ".*"), str(asset))
        ]
        
        move_contents(assets, args["target"])
    
    print("  ✔ Done.\n")
    return None


# Remove assets from target folder
# step_args:
# - include: Pattern to include files for removing
def assets_remove(steps: dict) -> None:
    print("Job == Removing assets:")

    for key, args in steps.items():
        print(f"  - Removing assets of '{key[0]}' ...")

        assets = glob_re(args["source"], args["include"])
        for asset in assets:
            asset.unlink()
    
    print("  ✔ Done.\n")
    return None


def assets_merge(steps: dict) -> None:
    print("Job == Merging assets:")

    for key, args in steps.items():
        print(f"  - Compiling Merging of '{key[0]}' ...")

        with open(args["target"], "w", encoding = "utf-8") as merged_file:

            for part_path in args["include"]:
                part_path = Path(args["source"], part_path)

                with open(part_path, "r", encoding = "utf-8") as part:
                    merged_file.write(part.read() + "\n")

                part_path.unlink()

    print("  ✔ Done.\n")
    return None



# Compiling --------------------------------------------------------------------


# Compile assets (e.g., SCSS to CSS)
# step_args:
# - prefix: Optional prefix to add to target path (default: deploy target)
# - type: Type of asset to compile. Only "css" is supported currently.
def assets_compile(steps: dict) -> None:
    print("Job == Compiling assets:")

    for key, args in steps.items():
        print(f"  - Compiling assets of '{key[0]}' ...")

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

        else:
            raise Exception(f"Compilation type '{args["type"]}' is not supported.")

    print("  ✔ Done.\n")
    return None
