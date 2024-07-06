import sys
from os import path
import re
from bs4 import BeautifulSoup


def components_html_to_dict(components_path):
    with open(components_path, 'r', encoding='utf-8') as file:
        components_raw = file.read()

    components_soup = BeautifulSoup(components_raw, 'html.parser')
    divs = components_soup.find_all('div', attrs={'data-component-name': True})

    return {div['data-component-name']: ''.join(str(child) for child in div.children) for div in divs}


def inject_components(template, components):
    for key, value in components.items():
        template = re.sub(f'@@{key}@@', value, template)

    return template


def build(template_path, components_path, output_path):
    components = components_html_to_dict(components_path)

    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()

    output = inject_components(template, components)

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(output)

    print(f'Injected components into {output_path}')
