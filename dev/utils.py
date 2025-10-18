
# Setup ------------------------------------------------------------------------

import shutil
import os
import stat
from pathlib import Path
from glob import glob

import yaml
import frontmatter

from contextlib import contextmanager
from datetime import datetime
import subprocess
import re

from typing import Generator, Callable, Any

proj_root = Path(__file__).resolve().parent.parent



# File helpers -----------------------------------------------------------------

# Safely change directory
@contextmanager
def chdir(path: str) -> Generator[str, None, None]:
    old_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield old_cwd
    finally:
        os.chdir(old_cwd)
    return None

# Remove read-only files with shutil.rmtree
def remove_readonly(func: Callable[[str], Any], path: str, exc_info) -> None:
    os.chmod(path, stat.S_IWRITE)
    func(path)
    return None

# Move all contents from source_path to target_path
def move_contents(
    source_path: str | list,
    target_path: str,
    flatten: bool = True
) -> None:
    if isinstance(source_path, str):
        items = [
            join_path(source_path, item)
            for item in os.listdir(source_path)
        ]
    else:
        items = source_path

    for item in items:
        s = item
        d = target_path if flatten else join_path(target_path, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok = True)
        else:
            shutil.copy2(s, d)
    return None


def join_path(*parts: str) -> str:
    parts_filtered = [p for p in parts if p is not None and p != ""]
    if all(part == "" for part in parts_filtered):
        return ""
    if len(parts_filtered) == 1:
        return parts_filtered[0]
    else:
        return os.path.join(*parts_filtered)
    


def glob_re(path: str, pattern: str, recursive: bool = False) -> list[str]:
    res = [
        file
        for file in iter_dir(path, recursive = recursive)
        if re.search(pattern, file)
    ]
    return res


def iter_dir(path: str, recursive: bool = False) -> list[str]:
    return glob(join_path(path, "**"), recursive = recursive)



# General Helpers --------------------------------------------------------------

log_path = join_path(str(proj_root), "dev", "run.log")

def run(
    cmd: str, *opts: str, log_path: str = log_path, **kwargs
) -> subprocess.CompletedProcess[str]:
    with open(log_path, "ab") as logf:
        logf.write((
            f"{datetime.now().isoformat()} -- "
            f"Running command: {cmd} {' '.join(opts)}\n"
        ).encode("utf-8"))

        res = subprocess.run(
            [cmd, *opts],
            stdout = logf, stderr = subprocess.STDOUT, check = True,
            **kwargs
        )
    return res


def get_lastmod(path: str) -> str:
    # External projects:
    parent_dir = os.path.dirname(path)
    for _ in range(path.count("/")):
        for config_file in ["bookdown.yml", "pkgdown.yml"]:
            if os.path.isfile(join_path(parent_dir, config_file)):
                return yaml.safe_load(path)["last_built"]
        parent_dir = os.path.dirname(parent_dir)
    
    # Local projects:
    src_dir = {
        "/index.html": "src/index",
        "/cv/index.html": "src/cv",
        "/blog/index.html": "src/blog"
    }.get("path")
    if src_dir:
        lastmod = run(
            "git", "log", "-1", "--format='%aI'", f"-- {src_dir}",
            capture_output = True, text = True
        )
        return lastmod.stdout.strip()

    # Blog:
    post_name = re.match(r"/blog/posts/(.+)\.html", path)
    if post_name:
        post_file = join_path("src/blog/posts", f"{post_name[1]}.qmd")
        lastmod = frontmatter.load(post_file)["last-edited"]
        return lastmod

    return datetime.now().astimezone().isoformat(timespec="seconds").replace("+00:00", "Z")



# Main Functions ---------------------------------------------------------------

# Flatten jobs into dict of steps, add presets and source/target arguments
def get_steps(
    jobs: dict,
    presets: dict
) -> dict[tuple[str, str], dict]:
    steps = {}

    for job_name, job in jobs.items():
        for step_name, args in job["steps"].items():
            if isinstance(args, str):
                args = presets[step_name][args]
            args["source"] = join_path(job["source"], args.get("subsource", ""))
            args["target"] = join_path(job["target"], args.get("subtarget", ""))
            steps[(job_name, step_name)] = args

    return steps


# Create site structure following steps' target paths
def create_dist_folder(steps: dict) -> None:
    print("Setup == Creating site folder structure ...")

    if os.path.exists("_dist/"):
        shutil.rmtree("_dist/", onexc = remove_readonly)
    os.makedirs("_dist/")

    target_paths = [
        args["target"]
        for args in steps.values()
        if re.match(r"^_dist", args["target"])
            and not re.match(r".*\.\w+$", args["target"])
    ]

    for path in target_paths:
        os.makedirs(path, exist_ok = True)

    print("  ✔ Done.\n")
    return None


# Filter steps by step name
def filter_steps(steps, step_name) -> dict:
    steps_filtered = {
        key: args
        for key, args in steps.items()
        if key[1] == step_name
    }
    return steps_filtered
