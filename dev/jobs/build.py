
# Setup  -----------------------------------------------------------------------

# File operations:
from pathlib import Path
from shutil import rmtree   
from yaml import safe_load as yaml_load

# HTML and XML parsing:
from xml.etree import ElementTree as ET
from xml.dom import minidom

# Others:
import re

# Type hints:
from typing import Any

# Local modules:
from jobs.utils import remove_readonly, glob_re, get_lastmod, run



# Site structure ---------------------------------------------------------------

def build_site_structure(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print(f"  - Creating _dist/ folder ...")

    # Rebuilding _dist/ folder:
    if Path("_dist/").is_dir():
        rmtree("_dist/", onexc = remove_readonly)
    Path("_dist/").mkdir()

    target_paths = {
        args["target"]
        for job_name, steps in jobs.items()
        for step_name, args in steps.items()
        if "_dist" in Path(args["target"]).parts
            and "." not in Path(args["target"]).name # Exclude files
    }

    for path in target_paths:
        Path(path).mkdir(exist_ok = True, parents = True)

    return None



# Sitemap ----------------------------------------------------------------------

def build_sitemap_index(args: dict[str, Any]) -> ET.Element:
    # Getting configurations:
    with open(Path("config/deployment.yaml"), "r", encoding = "utf-8") as file:
        root_url = yaml_load(file)["url"]

    sitemapindex = ET.Element(
        "sitemapindex",
        xmlns = "http://www.sitemaps.org/schemas/sitemap/0.9",
    )

    for external in args["external"]:
        external_path = Path(external.replace("_dist/", "/"))

        sitemap_el = ET.SubElement(sitemapindex, "sitemap")
        ET.SubElement(sitemap_el, "loc").text = (
            str(Path(root_url, external_path, "sitemap.xml").as_posix())
        )
        ET.SubElement(sitemap_el, "lastmod").text = get_lastmod(
            Path("_dist", external_path, "index.html")
        )
    
    return sitemapindex


def build_sitemap_urlset(args: dict[str, Any], sep_external: bool = False) -> ET.Element:
    # Getting configurations:
    with open(Path("config/deployment.yaml"), "r", encoding = "utf-8") as file:
        root_url = yaml_load(file)["url"]

    urlset = ET.Element(
        "urlset",
        xmlns = "http://www.sitemaps.org/schemas/sitemap/0.9",
    )

    # Getting HTML pages to include:
    html_pages = [
        Path(*page.parts[1:])
        for page in glob_re(Path("_dist"), r".*\.html", recursive = True)
        if not re.search(args["exclude"], str(page))
    ]
    if sep_external:
        exclude_pat = "|".join([re.escape(str(Path(path))) for path in args["external"]])
        html_pages = [
            page for page in html_pages
            if not re.search(exclude_pat, str(page))
        ]
        for external in args["external"]:
            external_path = Path(external.parts[1:])
            html_pages.append(Path(external_path, "index.html"))

    for page in html_pages:
        url = Path(root_url, page)
        if url.name == "index.html":
            url = Path(*url.parts[:-1])

        # Build url element
        url_el = ET.SubElement(urlset, "url")
        ET.SubElement(url_el, "loc").text = str(url.as_posix())
        ET.SubElement(url_el, "lastmod").text = get_lastmod(Path("_dist", page))

        # Add optional hints from args with sensible defaults
        changefreq = {Path(k): v for k, v in args["changefreq"].items()}.get(page)
        if changefreq:
            ET.SubElement(url_el, "changefreq").text = changefreq

        priority = {Path(k): v for k, v in args["priority"].items()}.get(page)
        if priority:
            ET.SubElement(url_el, "priority").text = str(priority)
    
    return urlset


def build_sitemap(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print(f"  - Updating static/sitemap.xml ...")

    if args.get("sep_external", False):
        combined_root = ET.Element("root")
        combined_root.append(build_sitemap_index(args))
        combined_root.append(build_sitemap_urlset(args, True))
    else:
        combined_root = build_sitemap_urlset(args, False)

    raw_xml = ET.tostring(combined_root, encoding = "utf-8")
    pretty = minidom.parseString(raw_xml).toprettyxml(
        indent = "  ", encoding = "utf-8"
    )

    with open(args["target"], "wb") as file:
        file.write(pretty)

    return None



# Quarto -----------------------------------------------------------------------

def build_quarto_blog(args: dict[str, Any], jobs: dict[str, dict[str, Any]]) -> None:
    print("  - Running `quarto render` ...")

    run("quarto", "render", str(args["source"]))

    return None
