document.addEventListener('DOMContentLoaded', function() {
    if (window.innerWidth > 410) {
        const explanationCard = document.querySelector('.explanation-card');
        const linkTextP = explanationCard.querySelector('h4');
        const explanationTextP = explanationCard.querySelector('p');
    
        const links = document.querySelectorAll('.column-card a');
        links.forEach(link => {
            link.addEventListener('mouseenter', function(e) {
                linkTextP.textContent = e.target.textContent
                explanationTextP.textContent = e.target.getAttribute('data-explanation');
    
                explanationCard.style.position = 'absolute';
                explanationCard.style.left = link.getBoundingClientRect().right + 6 + 'px';
                explanationCard.style.top = e.pageY - explanationCard.offsetHeight/2 + 'px' ;
                explanationCard.style.visibility = 'visible';
            });
    
            link.addEventListener('mouseleave', function() {
                explanationCard.style.visibility = 'hidden';
            });
        });
    }
});
