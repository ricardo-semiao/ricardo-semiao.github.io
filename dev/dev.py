
# Setup ------------------------------------------------------------------------

# Data loading:
from os import environ
from dotenv import load_dotenv
from yaml import safe_load as yaml_load

# Local modules:
from jobs.utils import get_enriched_jobs, cache_store, cache_restore
from importlib import import_module
step_functions = {
    **import_module("jobs.fetch").__dict__,
    **import_module("jobs.build").__dict__,
    **import_module("jobs.gallery").__dict__,
    **import_module("jobs.inject").__dict__,
    **import_module("jobs.assets").__dict__
}

# Debug `os.chdir("..")`



# Main -------------------------------------------------------------------------

def main():
    # Reading configurations and stashing cached jobs:
    load_dotenv("dev/.env")
    cached_jobs = yaml_load(environ.get("CACHED_JOBS", "{}"))
    cache_store(cached_jobs)


    # Getting enriched jobs:
    with open("config/jobs.yaml", "r", encoding = "utf-8") as file_jobs,\
         open("config/step_presets.yaml", "r", encoding = "utf-8") as file_presets:
        jobs = get_enriched_jobs(
            yaml_load(file_jobs), yaml_load(file_presets), cached_jobs
        )


    # Running Jobs and restoring cache on fail:
    try:
        for job_name, steps in jobs.items():
            print(f"=> Building {job_name}")
            for step_name, args in steps.items():
                step_functions[step_name.split("-")[0]](args, jobs)
            print("  ✔ Done.\n")
    except Exception as e:
        cache_restore(cached_jobs)
        raise e
    else:
        cache_restore(cached_jobs)


    # Deployment:
    # TODO


# Entry point:
if __name__ == "__main__":
    main()
