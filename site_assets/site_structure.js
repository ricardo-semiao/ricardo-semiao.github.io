document.addEventListener('DOMContentLoaded', function() {
    var navLinks = document.getElementsByClassName('site-nav-link');
    for (var i = 0; i < navLinks.length; i++) {
        if (new URL(navLinks[i].href).pathname == new URL(document.URL).pathname) {
            navLinks[i].classList.add('current-page');
        }
    }
});
