fetch('site_structure.html')
    .then(response => response.text())
    .then(data => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data, 'text/html');

        const headerHTML = doc.querySelector('#site-header').outerHTML;
        const footerHTML = doc.querySelector('#site-footer').outerHTML;

        document.querySelector('#site-header-container').innerHTML = headerHTML;
        document.querySelector('#site-footer-container').innerHTML = footerHTML;
    });

var navLinks = document.getElementsByClassName('nav-link');
for (var i = 0; i < navLinks.length; i++) {
    var linkUrl = new URL(navLinks[i].href);
    var currentUrl = new URL(document.URL);
    if (linkUrl.pathname == currentUrl.pathname) {
        navLinks[i].classList.add('current-page');
    }
}
