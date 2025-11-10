
# Setup  -----------------------------------------------------------------------

# File operations:
from pathlib import Path
from shutil import copytree, rmtree
from yaml import safe_load as yaml_load

# HTML and XML parsing:
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
from xml.dom import minidom

# Others:
import re

# Local modules:
from jobs.utils import remove_readonly, glob_re, get_lastmod, run



# Cahce ------------------------------------------------------------------------

def cache_store(steps: dict) -> None:
    key, args = list(steps.items())[0]
    jobs = args.get("jobs", {})

    if len(jobs) == 0:
        print("Cached jobs: skipping '", "', '".join(jobs.keys()), "'.\n")

    for job_name, job_path in jobs.items():
        copytree(job_path, Path(".tmp", job_path), dirs_exist_ok = True)
    
    return None

def cache_restore(steps: dict) -> None:
    key, args = list(steps.items())[0]
    jobs = args.get("jobs", {})

    for job_name, job_path in jobs.items():
        copytree(Path(".tmp", job_path), job_path, dirs_exist_ok = True)
    
    if Path(".tmp").is_dir():
        rmtree(Path(".tmp"), onexc = remove_readonly)
    
    return None



# Site structure ---------------------------------------------------------------

def build_site_structure(steps: dict, steps_all: dict) -> None:
    print("Setup == Creating site folder structure ...")

    # Rebuilding _dist/ folder:
    if Path("_dist/").is_dir():
        rmtree("_dist/", onexc = remove_readonly)
    Path("_dist/").mkdir()

    target_paths = [
        args["target"]
        for key, args in steps_all.items()
        if "_dist" in Path(args["target"]).parts
            and "." not in Path(args["target"]).name # Exclude files
    ]

    for path in target_paths:
        Path(path).mkdir(exist_ok = True, parents = True)

    print("  ✔ Done.\n")
    return None



# Sitemap ----------------------------------------------------------------------

def build_sitemap_index(steps: dict) -> ET.Element:
    # Getting configurations:
    with open(Path("config/deployment.yaml"), "r", encoding = "utf-8") as file:
        root_url = yaml_load(file)["url"]

    key, args = list(steps.items())[0]

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


def build_sitemap_urlset(steps: dict, sep_external: bool = False) -> ET.Element:
    # Getting configurations:
    with open(Path("config/deployment.yaml"), "r", encoding = "utf-8") as file:
        root_url = yaml_load(file)["url"]

    key, args = list(steps.items())[0]

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


def build_sitemap(steps: dict) -> None:
    print("Job == Building sitemap ...")

    key, args = list(steps.items())[0]

    if args.get("sep_external", False):
        combined_root = ET.Element("root")
        combined_root.append(build_sitemap_index(steps))
        combined_root.append(build_sitemap_urlset(steps, True))
    else:
        combined_root = build_sitemap_urlset(steps, False)

    raw_xml = ET.tostring(combined_root, encoding = "utf-8")
    pretty = minidom.parseString(raw_xml).toprettyxml(
        indent = "  ", encoding = "utf-8"
    )

    with open(args["target"], "wb") as file:
        file.write(pretty)

    print("  ✔ Done.\n")
    return None



# Quarto -----------------------------------------------------------------------

def build_quarto_blog(steps: dict) -> None:
    print("Job == Building Quarto blog ...")

    if len(steps) == 0:
        print("  ✔ No steps to run.\n")
        return None
    key, args = list(steps.items())[0]

    run("quarto", "render", str(args["source"]))

    print("  ✔ Done.\n")
    return None
