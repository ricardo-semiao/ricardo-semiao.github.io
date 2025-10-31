
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
            ]
            for item in components_all.select("div[data-component-name]")
        })

    return components



# External Data ----------------------------------------------------------------

def fetch_external_data(steps: dict) -> None:
    key, args = list(steps.items())[0]
    remote = args.get('remote', True)
    update = args.get('update', True)

    with open("config/external_sources.yaml", "r", encoding="utf-8") as file:
        sources = yaml_load(file)

    print(f"Setup == Fetching external ({'remote' if remote else 'local'}) sources:")
    

    for src_name, src in sources.items():
        if not src["update_required"] and not update:
            print(f"  - Skipping '{src_name}' (no update required).")
            continue

        src_remote = src["remote"]

        if remote and isinstance(src_remote, dict):
            repo_url = f"https://github.com/{src_remote["repo"]}.git"
            print(f"  - Fetching '{src_name}' from '{repo_url}' ...")

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
            print(f"  - Fetching {src_name} from '{src_remote}' ...")
            contents = get(src_remote)

            with open(src["target"]) as file:
                file.write(contents.text)

        else:
            local_path = str(environ[src["local"]])
            print(f"  - Fetching {src_name} from '{local_path}' ...")
            
            copytree(local_path, src["target"], dirs_exist_ok = True)

    print("  ✔ Done.\n")
    return None
