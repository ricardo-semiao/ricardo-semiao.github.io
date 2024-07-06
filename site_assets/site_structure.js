document.addEventListener('DOMContentLoaded', function() {
    var navlinks = document.getElementsByClassName('site-nav-link');
    for (var i = 0; i < navlinks.length; i++) {
        if (document.URL.split('/')[3] == navlinks[i].href.split('/')[3]) {
            navlinks[i].classList.add('current-page');
        }
    }
});
