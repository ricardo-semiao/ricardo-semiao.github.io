document.addEventListener('DOMContentLoaded', function() {
    const explanationCard = document.querySelector('.explanation-card');
    const linkTextP = explanationCard.querySelector('h4');
    const explanationTextP = explanationCard.querySelector('p');

    const links = document.querySelectorAll('.column-card a');
    links.forEach(link => {
        link.addEventListener('mouseenter', function(e) {
            linkTextP.textContent = e.target.textContent
            explanationTextP.textContent = e.target.getAttribute('data-explanation');

            explanationCard.style.display = 'block';
            explanationCard.style.left = e.pageX + 'px';
            explanationCard.style.top = e.pageY - explanationCard.offsetHeight/2 + 'px' ;
        });

        link.addEventListener('mouseleave', function() {
            explanationCard.style.display = 'none';
        });
    });
});
