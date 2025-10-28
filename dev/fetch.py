
# Setup ------------------------------------------------------------------------

# File operations:
from pathlib import Path
from os import environ
from shutil import copytree
from tempfile import mkdtemp

# HTML:
from requests import get
from bs4 import BeautifulSoup
from bs4.element import Tag

# Local modules:
from utils import run, cd, move_contents, proj_root



# Internal Sources -------------------------------------------------------------

def get_components(path: Path) -> dict[str, list[Tag]]:
    with open(path, "r", encoding="utf-8") as file:
        components_all = BeautifulSoup(file, "html.parser")

    components = {
        str(item["data-component-name"]): [
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

            with cd(Path(mkdtemp())):
                run(
                    'git', 'clone',
                    '--no-checkout', '--depth=1', '--filter=tree:0',
                    repo_url, "temp_local_repo"
                )
                with cd(Path("temp_local_repo")):
                    run(
                        'git', 'sparse-checkout', 'set',
                        '--no-cone', src_remote["folder"]
                    )
                    run('git', 'checkout')
                    move_contents(
                        src_remote["folder"],
                        Path(str(proj_root), src["target"])
                    )

        elif remote and isinstance(src_remote, str):
            print(f"  - Fetching {key} from '{src_remote}' ...")
            contents = get(src_remote)

            with open(src["target"]) as file:
                file.write(contents.text)

        else:
            local_path = str(environ[src["local"]])
            print(f"  - Fetching {key} from '{local_path}' ...")
            
            copytree(local_path, src["target"], dirs_exist_ok = True)

    print("  ✔ Done.\n")
    return None
