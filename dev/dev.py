
# Setup ------------------------------------------------------------------------

from dotenv import load_dotenv
import yaml

from utils import get_steps, create_dist_folder, filter_steps
from fetch import fetch_external_sources
from jobs import build_navbar, build_sitemap
from jobs import inject_project, inject_template
from jobs import assets_compile, assets_move, assets_remove, assets_merge


# Debug `os.chdir("..")`



# Main -------------------------------------------------------------------------

def main():
    # Initialization -----------------------------------------------------------

    # Reading configurations:
    load_dotenv(".env")

    with open("config/jobs.yaml", "r", encoding = "utf-8") as file:
        jobs = yaml.safe_load(file)

    with open("config/step_presets.yaml", "r", encoding = "utf-8") as file:
        presets = yaml.safe_load(file)


    # Getting enriched steps:
    steps = get_steps(jobs, presets)

    # Creating site folder structure:
    create_dist_folder(steps)


    # Fetching external resources:
    with open("config/external_sources.yaml", "r", encoding="utf-8") as file:
        sources = yaml.safe_load(file)
    
    fetch_external_sources(sources, remote = False, update = False)



    # Jobs ---------------------------------------------------------------------

    # Building components (navbar):
    build_navbar(filter_steps(steps, "build_navbar"), update = False)

    # Injections:
    #inject_project(filter_steps(steps, "inject_project"))
    inject_template(filter_steps(steps, "inject_template"))

    # Sitemap:
    build_sitemap(filter_steps(steps, "build_sitemap"))

    # Assets:
    assets_compile(filter_steps(steps, "assets_compile"))
    assets_move(filter_steps(steps, "assets_move"))
    assets_merge(filter_steps(steps, "assets_merge"))
    assets_remove(filter_steps(steps, "assets_remove"))

    # Blog:
    # Todo: do


    # Deployment to Site Branch ------------------------------------------------




if __name__ == "__main__":
    main()
