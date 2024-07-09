import re
from bs4 import BeautifulSoup
from yattag import indent


def components_html_to_dict(components_paths):
    divs = []

    for path in components_paths:
        with open(path, 'r', encoding='utf-8') as file:
            components_raw = file.read()

        components_soup = BeautifulSoup(components_raw, 'html.parser')
        divs += components_soup.find_all('div', attrs={'data-component-name': True})

    components = {
        div['data-component-name']: ''.join(str(child) for child in div.children)
        for div in divs
    }

    return components


def inject_components(template, components):
    for key, value in components.items():
        pattern = re.compile(r'\n([ \t]+)@@' + re.escape(key) + '@@')
        match = re.search(pattern, template)

        if match:
            cur_indent = match.group(1)
        else:
            continue

        value_pretty = indent(value, indentation = '    ', newline = f'\n{cur_indent}')
        template = re.sub(f'@@{key}@@', value_pretty, template)

    return template


def build(template_path, components_paths, output_path, prettify = False):
    components = components_html_to_dict(components_paths)

    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()

    output = inject_components(template, components)

    if prettify:
        output = indent(output, indentation = '    ', newline = '\n')

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(output)

    print(f'Injected components into {output_path}')
