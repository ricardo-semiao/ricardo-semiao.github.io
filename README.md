# Ricardo Semião's Homepage

Welcome! This is the repository for my personal homepage. It is organized as follows:

- [pakcages/](packages/) contains a custom template engine build in Python, `template_injector`. Read [its readme](packages/README.md).
- [site_assets/](site_assets/) contains site-wide assets, that are used in other repositories that publish to GitHub Pages (such as [rfcd](https://github.com/ricardo-semiao/rfcd) and [varutils](https://github.com/ricardo-semiao/varutils)). It includes:
    - Images in [img/](site_assets/img/).
    - [site_structure.js](site_assets/site_structure.js) to highlight the current tab in the navbar.
    - My personal palette, [palette.css](palette.css), from my [personal themes repository](https://github.com/ricardo-semiao/ricardo-semiao).
    - [components.html](site_assets/components.html) with components to inject in the templates.
    - CSS files separated in [site_structure.css](site_assets/site_structure.css) for the navbar/footer and [site_style.css](site_assets/site_style.css) for everything else.
- [assets/](assets/) contain specific assets for each page in the site. Each page has a template to be injected, and a context-specific stylesheet.
- The [index.html](index.html) and [cv.html](cv.html) are the injected, final, outputs.
- [dev.py](dev.py) is a Python script to build the site.

This was my first true contact with web-dev, and got me really excited. To push myself, I attempted to use the most out of the "bare" web-dev tools, and limit the use of frameworks and external help.
