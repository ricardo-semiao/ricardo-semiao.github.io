from template_injector import build
import requests

# Install with:
#pip install git+https://github.com/ricardo-semiao/ricardo-semiao.github.io.git#subdirectory=template_injector

# Downloading personal palette from github:
response = requests.get("https://raw.githubusercontent.com/ricardo-semiao/ricardo-semiao/main/palette/palette.css?token=$(date%20+%s)")
with open("site_assets/palette.css", 'wb') as file:
    file.write(response.content)

# Building the templates:
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
