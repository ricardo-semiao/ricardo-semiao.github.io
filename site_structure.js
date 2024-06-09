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

var navLinks = document.getElementsByClassName('site-nav-link');
for (var i = 0; i < navLinks.length; i++) {
    if (navLinks[i].href == document.URL) {
        navLinks[i].classList.add('current-page');
    }
}
