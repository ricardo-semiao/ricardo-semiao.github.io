
# Setup ------------------------------------------------------------------------

import os
import re
import yaml

from template_injector import build
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
from xml.dom import minidom

from utils import join_path, run, move_contents, glob_re, iter_dir, get_lastmod
from fetch import get_components



# Creating HTML ----------------------------------------------------------------

def build_navbar(steps: dict, update: bool = True) -> None:
    if not update:
        print("Skipping navbar build (update = False).\n")
        return None
    print("Job == Building navigation bar ...")

    with open("src/global/components.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    ul = soup.new_tag("ul", attrs={"class": "nav-ul"})
    dropdowns = {}

    # args = steps[("index", "build_navbar")]
    for key, args in steps.items():
        target = re.sub(r"_dist/?", "/", args["target"])
        parts = target.split("/")

        a = soup.new_tag("a", attrs = {"href": target})
        a.string = args["label"]
        li = soup.new_tag("li", attrs = {"class": "nav-li"})
        li.append(a)

        if len(parts) == 2:
            ul.append(li)
        
        elif len(parts) == 3:
            if parts[1] not in dropdowns:
                dropdowns[parts[1]] = soup.new_tag("li", attrs = {"class": "nav-drop"})
                p = soup.new_tag("p")
                p.string = args["drop_label"]
                dropdowns[parts[1]].append(p)
                dropdowns[parts[1]].append(soup.new_tag("button"))
                dropdowns[parts[1]].append(soup.new_tag("ul"))
            dropdowns[parts[1]].ul.append(li)
        
        else:
            raise Exception(f"Cannot build navbar entry for target '{args['target']}'.")

    for drop in dropdowns.values():
        ul.append(drop)

    soup.\
        select_one("div[data-component-name=site-header] nav > ul").\
        replace_with(ul)
    
    with open("src/global/components.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify(formatter = "html5"))

    print("  ✔ Done.\n")
    return None


def build_sitemap(steps: dict) -> None:
    print("Job == Building sitemap ...")

    # Getting configurations:
    with open("config/deployment.yaml", "r", encoding = "utf-8") as file:
        root_url = yaml.safe_load(file)["url"]

    key, args = list(steps.items())[0]

    # Creating XML objects:
    urlset = ET.Element(
        "urlset",
        xmlns = "http://www.sitemaps.org/schemas/sitemap/0.9",
    )
    sitemapindex = ET.Element(
        "sitemapindex",
        xmlns = "http://www.sitemaps.org/schemas/sitemap/0.9",
    )

    # Getting HTML pages to include:
    html_pages = [
        re.sub(r"_dist(/|\\)?", "/", page)
        for page in glob_re("_dist", r".*\.html", recursive = True)
        if not re.search(args["exclude"], page)
            and not re.search(r"|".join(args["external"]), page)
    ]

    for external in args["external"]:
        external_path = external.replace("_dist/", "/")
        sitemap_el = ET.SubElement(sitemapindex, "sitemap")
        ET.SubElement(sitemap_el, "loc").text = (
            root_url + external_path + "/sitemap.xml"
        )
        ET.SubElement(sitemap_el, "lastmod").text = get_lastmod(
            external_path + "/index.html"
        )

        html_pages.append(f"/{external_path}/index.html")

    html_pages.sort(key = lambda page: (page.count("/") + page.count("\\"), page))

    for page in html_pages:
        url = root_url + page
        if url.endswith("index.html"):
            url = url[:-len("index.html")]

        # Build url element.
        url_el = ET.SubElement(urlset, "url")
        ET.SubElement(url_el, "loc").text = url
        ET.SubElement(url_el, "lastmod").text = get_lastmod(page)

        # Add optional hints from args with sensible defaults.
        changefreq = args["changefreq"].get(page)
        if changefreq:
            ET.SubElement(url_el, "changefreq").text = changefreq

        priority = args["priority"].get(page)
        if priority is not None:
            ET.SubElement(url_el, "priority").text = str(priority)

        # Combine urlset and sitemapindex into a single XML structure
        combined_root = ET.Element("root")
        combined_root.append(urlset)
        combined_root.append(sitemapindex)

        raw_xml = ET.tostring(combined_root, encoding = "utf-8")
        pretty = minidom.parseString(raw_xml).toprettyxml(
            indent = "  ", encoding = "utf-8"
        )

    with open(args["target"], "wb") as file:
        file.write(pretty)

    print("  ✔ Done.\n")
    return None



# Inject Components ------------------------------------------------------------

# Inject components into external projects
# step_args:
# - Variable length of components to inject. See `configs/steps_presets.yaml`
def inject_project(steps: dict) -> None:
    print("Job == Injecting components into projects:")
    components = get_components("src/global/components.html")
    
    for key, args in steps.items():
        print(f"  - Injecting components into '{key[0]}' ...")

        html_pages = glob_re(args["source"], r".*\.html", recursive = True)

        for page in html_pages:
            with open(page, "r+", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")
            
            if not soup.body:
                continue # Skip non-content pages

            for comp_name, comp_args in args["components"].items():
                for item in components[comp_name]:
                    reference = soup.select_one(comp_args["selector"])
                    if comp_args["position"] == "before":
                        reference.insert_before(item)
                    else:
                        reference.insert_after(item)

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

        components_paths = ["src/global/components.html"]
        local_component_path = join_path(args["source"], "components.html")
        if os.path.exists(local_component_path):
            components_paths.append(local_component_path)

        build(
            join_path(args["source"], "template.html"),
            components_paths,
            join_path(args["target"], "index.html"),
            prettify = False, quiet = True
        )

    print("  ✔ Done.\n")
    return None



# Assets -----------------------------------------------------------------------

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
            for asset in iter_dir(args["source"])
            if not re.search(args.get("exclude", ".^"), asset)
                and re.search(args.get("include", ".*"), asset)
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
        print(f"  - Moving assets of '{key[0]}' ...")

        assets = glob_re(args["source"], args["include"])
        for asset in assets:
            os.remove(asset)
    
    print("  ✔ Done.\n")
    return None


# Compile assets (e.g., SCSS to CSS)
# step_args:
# - prefix: Optional prefix to add to target path (default: deploy target)
# - type: Type of asset to compile. Only "css" is supported currently.
def assets_compile(steps: dict) -> None:
    print("Job == Compiling assets:")

    for key, args in steps.items():
        print(f"  - Compiling assets of '{key[0]}' ...")

        if (args["type"] == "css"):

            for scss_file in glob_re(args["source"], r".*\.scss"):

                target = join_path(
                    args["target"],
                    re.split(r'/|\\', scss_file)[-1].replace(".scss", ".css")
                )

                run("sass", scss_file, target, "--no-source-map")

        else:
            raise Exception(f"Compilation type '{args["type"]}' is not supported.")

    print("  ✔ Done.\n")
    return None


def assets_merge(steps: dict) -> None:
    print("Job == Merging assets:")

    for key, args in steps.items():
        print(f"  - Compiling Merging of '{key[0]}' ...")

        with open(args["target"], "w", encoding = "utf-8") as merged_file:

            for part_path in args["include"]:
                part_path = join_path(args["source"], part_path)

                with open(part_path, "r", encoding = "utf-8") as part:
                    merged_file.write(part.read() + "\n")

                os.remove(part_path)

    print("  ✔ Done.\n")
    return None
