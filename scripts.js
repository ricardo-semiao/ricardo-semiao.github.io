var navLinks = document.getElementsByClassName('nav-link');
for (var i = 0; i < navLinks.length; i++) {
    if (navLinks[i].href == document.URL) {
        navLinks[i].classList.add('current-page');
    }
}
