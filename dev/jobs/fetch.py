
# Setup ------------------------------------------------------------------------

# File operations:
from pathlib import Path
from shutil import copytree
from tempfile import mkdtemp
from yaml import safe_load as yaml_load
from os import environ

# HTML:
from requests import get
from bs4 import BeautifulSoup
from bs4.element import Tag

# Others:
import re

# Type hints:
from typing import Any

# Local modules:
from jobs.utils import glob_re, run, cd, move_contents, proj_root



# Internal Sources -------------------------------------------------------------

def get_components() -> dict[str, list[Tag]]:
    component_files = glob_re(Path("src"), r".*components\.html", recursive = True)
    components = {}

    for comp_file in component_files:
        with open(comp_file, "r", encoding="utf-8") as file:
            components_all = BeautifulSoup(file, "html.parser")

        # NOTE: Assumes no conflict in component names
        components.update({
            str(item["data-component-name"]): [
                tag for tag in item.contents if isinstance(tag, Tag)
                    or (isinstance(tag, str) and re.search(r"@@.+@@", tag))
            ]
            for item in components_all.select("div[data-component-name]")
        })

    return components



# External Data ----------------------------------------------------------------

def fetch_external_data(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    if not args["update_required"]:
        print(f"  - Not fetching external data (no update required).")
        return None

    use_remote = args.get("use_remote", True)
    arg_remote = args["remote"]
    
    if use_remote and isinstance(arg_remote, dict):
        repo_url = f"https://github.com/{arg_remote["repo"]}.git"
        print(f"  - Fetching external data from '{repo_url}' ...")

        with cd(Path(mkdtemp())):
            run(
                'git', 'clone',
                '--no-checkout', '--depth=1', '--filter=tree:0',
                repo_url, "temp_local_repo"
            )
            with cd(Path("temp_local_repo")):
                run(
                    'git', 'sparse-checkout', 'set',
                    '--no-cone', arg_remote["folder"]
                )
                run('git', 'checkout')
                move_contents(
                    Path(arg_remote["folder"]),
                    Path(str(proj_root), args["target"])
                )

    elif use_remote and isinstance(arg_remote, str):
        print(f"  - Fetching external data from '{arg_remote}' ...")
        contents = get(arg_remote)

        with open(args["target"]) as file:
            file.write(contents.text)

    else:
        local_path = str(environ[args["local"]])
        print(f"  - Fetching external data from '{local_path}' ...")
        
        copytree(local_path, args["target"], dirs_exist_ok = True)

    return None
