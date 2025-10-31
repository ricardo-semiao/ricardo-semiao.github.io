
# Setup ------------------------------------------------------------------------

# Data loading:
from dotenv import load_dotenv
from yaml import safe_load as yaml_load

# Local modules:
from jobs.utils import get_steps, filter_steps
from jobs.fetch import fetch_external_data
from jobs.build import build_site_structure, build_sitemap, build_quarto_blog
from jobs.gallery import build_gallery
from jobs.inject import inject_project, inject_template
from jobs.assets import assets_compile, assets_move, assets_remove, assets_merge

# Debug `os.chdir("..")`



# Main -------------------------------------------------------------------------

def main():
    # Initialization -----------------------------------------------------------

    # Reading configurations:
    load_dotenv("dev/.env")

    with open("config/jobs.yaml", "r", encoding = "utf-8") as file:
        jobs = yaml_load(file)

    with open("config/step_presets.yaml", "r", encoding = "utf-8") as file:
        presets = yaml_load(file)

    # Getting enriched steps:
    steps = get_steps(jobs, presets)



    # Jobs ---------------------------------------------------------------------

    # Building infrastructure and getting external data:
    build_site_structure(filter_steps(steps, "build_site_structure", True), steps)
    fetch_external_data(filter_steps(steps, "fetch_external_data", True))
    build_sitemap(filter_steps(steps, "build_sitemap", True))

    # Local projects:
    inject_template(filter_steps(steps, "inject_template"))
    build_gallery(filter_steps(steps, "build_gallery", True))
    
    # External projects:
    build_quarto_blog(filter_steps(steps, "build_quarto_blog", True))
    inject_project(filter_steps(steps, "inject_project"))
    # inject_links(filter_steps(steps, "adjust_links")) # Unneded

    # Assets:
    assets_compile(filter_steps(steps, "assets_compile"))
    assets_move(filter_steps(steps, "assets_move"))
    assets_merge(filter_steps(steps, "assets_merge"))
    assets_remove(filter_steps(steps, "assets_remove"))



    # Deployment to Site Branch ------------------------------------------------

    # ...


# Entry point:
if __name__ == "__main__":
    main()
