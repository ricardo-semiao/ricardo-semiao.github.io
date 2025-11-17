# Ricardo Semião's Website

Welcome! This is the repository for my personal site. It is built from scratch with the goal of being a first contact with web development. It uses bare HTML/SCSS/JS and custom Python scripts to orchestrate components, optimize masonry layouts, process external project sites, and manage the Quarto blog.


## Build Process

The main script is [dev/dev.py](dev/dev.py), which reads a set of jobs from [config/jobs.yaml](config/jobs.yaml). Each job represents a page or sub-site (index page, Quarto blog, RFCD book, etc.) and has a series of steps. Each step is implemented as a Python function in the [dev/steps](dev/steps) folder and is called with parameters that are passed to the step functions.

In simplified terms, the available steps are:

- Initialization:
    - `build_site_structure()`: Creates the site structure at the target folder (`_site/`).
    - `fetch_external_data()`: Fetches raw data from external projects, from remote or local sources.
- Inject:
    - `inject_template()`: Injects components (e.g., header, footer, etc.) into templates. Used for local pages (index, CV, gallery). Powered by my custom templating package `template_injector`.
    - `inject_project()`: Injects components into external project pages, adding the site's constructs to them. Powered via CSS selectors and BeautifulSoup.
- Specific builds:
    - `build_gallery()`: Reads from the list of images at [src/gallery/images.yaml](src/gallery/images.yaml) and builds a masonry-optimized gallery page. The masonry optimization is done via a custom algorithm implemented in the `armasonry` package. The function also injects the images with descriptions and other metadata.
    - `build_quarto_blog()`: Runs Quarto render.
    - `build_sitemap()`: Builds the sitemap.xml file.
- Assets:
    - `assets_move()`: Moves static assets (JS, images, etc.) to the target folder. `assets_remove()` removes unneeded assets from external projects.
    - `assets_compile()`: Moves files that need compilation, such as SCSS and the TeX files for my CV.
    - `assets_merge()`: Merges several CSS files into a single one for optimization.

Each job calls one or more of these steps, in specific orders, with specific parameters. Steps can have presets at [config/steps_presets.yaml](config/steps_presets.yaml) to avoid repetition in the main jobs file.

Jobs can be cached during development to avoid rebuilding via the `cache_store()` and `cache_restore()` functions, plus the `dev/.env` environment variable `CACHED_JOBS`.


## Deployment

Deployment is done via GitHub Pages, which serves the content from the `site` branch.

Currently, the build process creates the site in a `_site/` subfolder. In it, I opened a git worktree that points to the `site` orphan branch. This way, I have manual and independent control over the development and deployment branches.

The build process includes reproducibility efforts, with dependencies defined in [pyproject.toml](pyproject.toml). uv is used to guarantee the correct Python and package versions. A custom function `check_external_deps()` checks if the required external dependencies (Quarto, git, sass, latexmk, and uv itself) are installed, in PATH, and with the correct versions.
