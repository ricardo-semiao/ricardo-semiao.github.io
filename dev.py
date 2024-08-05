from template_injector import build

# Install with:
#pip install git+https://github.com/ricardo-semiao/ricardo-semiao.github.io.git#subdirectory=template_injector

# Building the templates:
build(
    'templates/home_template.html',
    ['templates/components.html'],
    'docs/index.html',
    prettify = False
)

build(
    'templates/cv_template.html', 
    ['templates/components.html'],
    'docs/cv/index.html',
    prettify = False
)


# Downloading personal palette from github:
#import requests
#response = requests.get("https://raw.githubusercontent.com/ricardo-semiao/ricardo-semiao/main/palette/palette.css?token=$(date%20+%s)")
#with open("site_assets/palette.css", 'wb') as file:
#    file.write(response.content)
