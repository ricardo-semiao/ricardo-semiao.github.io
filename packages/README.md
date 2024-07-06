# template_injector

This is a simple HTML template engine built in Python.

The basics of its functioning is as below:

- Components are defined in a HTML file, encapsulating them in a `<div>` tag with a `data-component-name` attribute.
- The module looks for `@@component-name@@` entries in a template HTML file, and injects the matching component's div content in their place.

Some technical aspects:
- The injection is done with regular expressions via `re.sub`.
- The HTML of the components is parsed with BeautifulSoup.
- The injected output is prettified using `yattag.indent`.
