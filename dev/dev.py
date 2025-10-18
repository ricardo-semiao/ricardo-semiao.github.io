from template_injector import build

# Install with:
#pip install git+https://github.com/ricardo-semiao/ricardo-semiao.git#subdirectory=packages/template_injector

# Building the templates:
build(
    'assets/home/home_template.html',
    ['site_assets/components.html'],
    'index.html',
    prettify = False
)

build(
    'assets/cv/cv_template.html', 
    ['site_assets/components.html'],
    'cv.html',
    prettify = False
)


# Downloading personal palette from github:
#import requests
#response = requests.get("https://raw.githubusercontent.com/ricardo-semiao/ricardo-semiao/main/palette/palette.css?token=$(date%20+%s)")
#with open("site_assets/palette.css", 'wb') as file:
#    file.write(response.content)
