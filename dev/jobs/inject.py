
# Setup -----------------------------------------------------------------------

# File operations:
from pathlib import Path

# HTML parsing:
from bs4 import BeautifulSoup
from template_injector import build

# Others:
import re
from copy import copy

# Local modules:
from jobs.utils  import glob_re
from jobs.fetch import get_components


# Injectors --------------------------------------------------------------------

# Inject components into external projects
manipulators = {
    "before": lambda el, comp: el.insert_before(comp),
    "after": lambda el, comp: el.insert_after(comp),
    "wrap": lambda el, comp: el.wrap(copy(comp)),
    "append": lambda el, comp: el.append(comp)
}

def inject_project(steps: dict) -> None:
    print("Job == Injecting components into projects:")

    components = get_components()
    
    for key, args in steps.items():
        print(f"  - Injecting components into '{key[0]}' ...")
        
        html_pages = glob_re(args["source"], r".*\.html", recursive = True)

        for page in html_pages:

            with open(page, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")
                if not soup.body:
                    continue # Skip non-content pages

            for comp_name, comp_args in args["components"].items():
                manipulate = manipulators[comp_args["position"]]
                for comp_item in components[comp_name]:
                    manipulate(soup.select_one(comp_args["selector"]), comp_item)

            with open(page, "w", encoding="utf-8") as file:
                file.write(str(soup))

    print("  ✔ Done.\n")
    return None


# Inject components into local templates
# step_args: None (unused)
def inject_template(steps: dict) -> None:
    print("Job == Injecting components into templates:")

    for key, args in steps.items():
        print(f"  - Injecting components into '{key[0]}' ...")

        components_paths = [Path("src/global/global_components.html")]
        local_component_path = Path(args["source"], "global_components.html")
        if local_component_path.is_file():
            components_paths.append(local_component_path)

        build(
            Path(args["source"], "template.html"),
            components_paths,
            Path(args["target"], "index.html"),
            prettify = False, quiet = True
        )

    print("  ✔ Done.\n")
    return None



# Adjusting Links --------------------------------------------------------------

def inject_links(steps: dict) -> None:
    print("Job == Adjusting links ...")

    for key, args in steps.items():
        print(f"  - Adjusting links of '{key[0]}' ...")

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

    print("  ✔ Done.\n")
    return None
