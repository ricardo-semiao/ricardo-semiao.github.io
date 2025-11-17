
# Setup -----------------------------------------------------------------------

# File operations:
from pathlib import Path

# HTML parsing:
from bs4 import BeautifulSoup
from template_injector import build

# Others:
import re
from copy import copy

# Type hints:
from typing import Any

# Local modules:
from steps.utils  import glob_re
from steps.fetch import get_components


# Injectors --------------------------------------------------------------------

# Inject components into external projects
manipulators = {
    "before": lambda el, comp: el.insert_before(comp),
    "after": lambda el, comp: el.insert_after(comp),
    "wrap": lambda el, comp: el.wrap(comp),
    "append": lambda el, comp: el.append(comp),
    "insert": lambda el, comp: el.insert(0, comp),
    "addclass": lambda el, comp: el.attrs.setdefault("class", []).append(comp),
    "remove": lambda el, comp: el.decompose()
}

def inject_project(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print("  - Injecting project components ...")

    components = get_components()
    html_pages = glob_re(args["source"], r".*\.html", recursive = True)

    for page in html_pages:
        with open(page, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        if not soup.body:
            continue # Skip non-content pages

        for comp_name, comp_args in args["components"].items():
            manipulate = manipulators[comp_args["position"]]
            for comp_item in components.get(comp_name, [comp_name]):
                # If no components found, use the name as raw HTML/text
                if comp_args.get("try", False):
                    try:
                        manipulate(soup.select_one(comp_args["selector"]), copy(comp_item))
                    except:
                        pass
                else:
                    manipulate(soup.select_one(comp_args["selector"]), copy(comp_item))

        with open(page, "w", encoding="utf-8") as file:
            file.write(str(soup))

    return None


# Inject components into local templates
# step_args: None (unused)
def inject_template(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print("  - Injecting template components ...")

    components_paths = glob_re(Path("src"), r".*_components\.html", recursive = True)
    # TODO: Only load needed components to avoid name clashes

    if args.get("recursive", False):
        template_paths = glob_re(Path(args["source"]), r".*(?<!_components)\.html", recursive = True)
    elif Path(args["source"]).is_dir(): # By default, index.html in the source folder
        template_paths = [Path(args["source"], "index.html")]
    else:
        template_paths = [Path(args["source"])]

    for path in template_paths:
        if Path(args["target"]).is_dir(): # By default, the target + name of the template
            target_path = Path(args["target"], path.name)
        elif Path(args["target"]).is_file():
            target_path = Path(args["target"])
        else:
            raise Exception(f"Target path {args['target']} does not exist.")

        build(
            path, components_paths, target_path,
            prettify = False, quiet = True
        )

    return None



# Adjusting Links --------------------------------------------------------------

def inject_links(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print("  - Adjusting links ...")

    html_pages = glob_re(args["source"], r".*\.html", recursive = True)

    for page in html_pages:
        with open(page, "r+", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        
        for pattern, replacement in args["replace"].items():
            pattern = re.compile(pattern)
            attr = args["attr"]
            for link in soup.find_all(**{attr: pattern}):
                link[attr] = re.sub(pattern, replacement, link[attr])

        with open(page, "w", encoding="utf-8") as file:
            file.write(str(soup))

    return None
