from template_injector import build

# Install with:
#pip install git+https://github.com/ricardo-semiao/ricardo-semiao.github.io.git@feature/injector#subdirectory=template_injector

build('index_template.html', 'site_assets/components.html')
build('cv/index_template.html', 'site_assets/components.html')
