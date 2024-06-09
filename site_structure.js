fetch('site_structure.html')
    .then(response => response.text())
    .then(data => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data, 'text/html');

        const headerHTML = doc.querySelector('#site-header');
        const footerHTML = doc.querySelector('#site-footer');

        var navLinks = headerHTML.getElementsByClassName('site-nav-link');
        for (var i = 0; i < navLinks.length; i++) {
            if (navLinks[i].href == document.URL) {
                navLinks[i].classList.add('current-page');
            }
        }

        document.querySelector('#site-header-container').innerHTML = headerHTML.outerHTML;
        document.querySelector('#site-footer-container').innerHTML = footerHTML.outerHTML;
    });
