from template_injector import build

# Install with:
#pip install git+https://github.com/ricardo-semiao/ricardo-semiao.github.io.git#subdirectory=template_injector

build(
    'assets/home/home_template.html',
    'site_assets/components.html',
    'index.html'
)

build(
    'assets/cv/cv_template.html', 
    'site_assets/components.html',
    'cv.html'
)
