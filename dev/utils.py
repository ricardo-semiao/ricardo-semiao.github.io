
# Setup ------------------------------------------------------------------------

# File operations:
from pathlib import Path
from os import chdir
from shutil import copytree, copy2, rmtree
from stat import S_IWRITE

# Reading yaml:
from yaml import safe_load as yaml_load

# Others:
from contextlib import contextmanager
from datetime import datetime
import subprocess
import re

# Type hints:
from typing import Generator, Callable, Any

proj_root = Path(__file__).resolve().parent.parent



# Basic File helpers -----------------------------------------------------------

# Glob with regex pattern
def glob_re(
    path: Path,
    pattern: str = r".+",
    recursive: bool = False
) -> list[Path]:
    if not path.is_dir():
        raise Exception(f"Path {path} is not a directory.")
    
    dir_contents = [
        file
        for file in path.glob("**/*" if recursive else "*")
        if re.search(pattern, str(file))
    ]

    return dir_contents

# Move all contents from source_path to target_path
def move_contents(
    source: Path | list[Path],
    target: Path,
    flatten: bool = True
) -> None:
    if isinstance(source, Path):
        items = glob_re(source)
    elif isinstance(source, list):
        items = source
    else:
        raise Exception("`source` must be `Path` or `list[Path]`.")

    for item in items:
        src = item
        dest = target if flatten else Path(target, item)
        if src.is_dir():
            copytree(src, dest, dirs_exist_ok = True)
        elif src.is_file():
            copy2(src, dest)
        else:
            raise Exception(f"Path {src} is neither a file nor a directory.")

    return None



# Other File Helpers -----------------------------------------------------------

# Safely change directory
@contextmanager
def cd(path: Path) -> Generator[Path, None, None]:
    old_cwd = Path.cwd()
    chdir(path)

    try:
        yield old_cwd
    finally:
        chdir(old_cwd)

    return None

# Remove read-only files with shutil.rmtree
def remove_readonly(func: Callable[[str], Any], path: str, exc_info) -> None:
    Path(path).chmod(S_IWRITE)
    func(path)
    return None

# Read text docment yaml frontmatter
def get_frontmatter(path: Path) -> dict:
    if not path.is_file():
        raise Exception(f"Path {path} is not a file.")

    with open(path, "r", encoding = "utf-8") as file:
        header = file.read().split("---", 2)[1]

    return yaml_load(header)



# General Helpers --------------------------------------------------------------

log_path = Path(proj_root, "dev", "run.log")

# Run a command
def run(
    cmd: str, *opts: str, log_path: Path = log_path, **kwargs
) -> subprocess.CompletedProcess[str]:
    with open(log_path, "ab") as file_log:
        file_log.write((
            f"{datetime.now().isoformat()} -- "
            f"Running command: {cmd} {' '.join(opts)}\n"
        ).encode("utf-8"))

        res = subprocess.run(
            [cmd, *opts],
            stdout = file_log, stderr = subprocess.STDOUT, check = True,
            **kwargs
        )

    return res

# Get last modified time for a file
def get_lastmod(path: Path) -> str:
    if not path.is_file():
        raise Exception(f"Path {path} is not a file.")
    
    lastmod = None

    # External projects:
    for parent in path.parents:
        for config_file in ["bookdown.yml", "pkgdown.yml"]:
            config_path = Path(parent, config_file)
            if config_path.is_file():
                with open(config_path, "r", encoding="utf-8") as file:
                    lastmod = yaml_load(file)["last_built"]
    
    if lastmod:
        return lastmod

    # Blog:
    parts =  path.parts

    if "blog" in parts and "index.html" not in parts:
        post_file = Path("src", *parts[1:-1], path.stem + ".qmd")
        lastmod = str(get_frontmatter(post_file)["last-edited"])

    if lastmod:
        return lastmod

    # Local projects:
    src_dir = {
        Path("/index.html"): Path("src/index"),
        Path("/cv/index.html"): Path("src/cv"),
        Path("/blog/index.html"): Path("src/blog")
    }.get(path)

    if src_dir:
        run_out = run(
            "git", "log", "-1", "--format='%aI'", f"-- {src_dir}",
            capture_output = True, text = True
        )
        lastmod = run_out.stdout.strip() # Todo: format to iso

    if lastmod:
        return lastmod
    
    # Fallbadck - current time:
    lastmod = datetime.now().astimezone().isoformat(timespec="seconds").replace("+00:00", "Z")

    return lastmod



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
            
            if isinstance(args, dict):
                args_list = [args]
            else:
                args_list = args

            for i, args in enumerate(args_list):
                job_name = job_name + ("" if i == 0 else f" ({i + 1})")
                args["source"] = Path(job["source"], args.get("subsource", ""))
                args["target"] = Path(job["target"], args.get("subtarget", ""))
                steps[(job_name, step_name)] = args

    return steps


# Create site structure following steps' target paths
def create_dist_folder(steps: dict) -> None:
    print("Setup == Creating site folder structure ...")

    if Path("_dist/").is_dir():
        rmtree(Path("_dist/"), onexc = remove_readonly)
    Path("_dist/").mkdir(exist_ok = True)

    target_paths = [
        args["target"]
        for args in steps.values()
        if "_dist" in Path(args["target"]).parts
            and "." not in Path(args["target"]).name
    ]

    for path in target_paths:
        Path(path).mkdir(exist_ok = True, parents = True)

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
