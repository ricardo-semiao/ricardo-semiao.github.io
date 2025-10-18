
# Setup ------------------------------------------------------------------------

import os
import shutil
import tempfile

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from utils import join_path, run, chdir, move_contents, proj_root



# Internal Sources -------------------------------------------------------------

def get_components(path: str) -> dict[str, list[Tag]]:
    with open(path, "r", encoding="utf-8") as file:
        components_all = BeautifulSoup(file, "html.parser")

    components = {
        item["data-component-name"]: [
            tag for tag in item.contents if isinstance(tag, Tag)
        ]
        for item in components_all.select("div[data-component-name]")
    }

    return components



# External Sources -------------------------------------------------------------

def fetch_external_sources(
    sources: dict,
    remote: bool = True,
    update: bool = True
) -> None:
    print(f"Setup == Fetching external ({'remote' if remote else 'local'}) sources:")

    for key, src in sources.items():
        if not src["update_required"] and not update:
            print(f"  - Skipping '{key}' (no update required).")
            continue

        src_remote = src["remote"]

        if remote and isinstance(src_remote, dict):
            repo_url = f"https://github.com/{src_remote["repo"]}.git"
            print(f"  - Fetching '{key}' from '{repo_url}' ...")

            with chdir(tempfile.mkdtemp()):
                run(
                    'git', 'clone',
                    '--no-checkout', '--depth=1', '--filter=tree:0',
                    repo_url, "temp_local_repo"
                )
                with chdir("temp_local_repo"):
                    run(
                        'git', 'sparse-checkout', 'set',
                        '--no-cone', src_remote["folder"]
                    )
                    run('git', 'checkout')
                    move_contents(
                        src_remote["folder"],
                        join_path(str(proj_root), src["target"])
                    )

        elif remote and isinstance(src_remote, str):
            print(f"  - Fetching {key} from '{src_remote}' ...")
            contents = requests.get(src_remote)

            with open(src["target"]) as file:
                file.write(contents.text)

        else:
            local_path = str(os.environ[src["local"]])
            print(f"  - Fetching {key} from '{local_path}' ...")
            
            shutil.copytree(local_path, src["target"], dirs_exist_ok = True)

    print("  ✔ Done.\n")
    return None
