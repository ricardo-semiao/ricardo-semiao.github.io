const updateTooltip = function(link, tooltip, tooltipH4, tooltipP, remove) {
    if (remove) {
        link.removeAttribute("aria-describedby")
        tooltip.setAttribute("aria-hidden", "true");
        tooltip.style.visibility = "hidden";
    } else {
        link.setAttribute("aria-describedby", "projects-tooltip");

        tooltipH4.textContent = link.textContent
        tooltipP.textContent = link.getAttribute('data-explanation');

        tooltip.setAttribute("aria-hidden", "false");
        tooltip.style.visibility = "visible";
        tooltip.style.left = link.getBoundingClientRect().right + 6 + 'px';
        tooltip.style.top = link.pageY - tooltip.offsetHeight/2 + 'px';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const tooltip = document.querySelector('#projects-tooltip');
    const tooltipH4 = tooltip.querySelector('h4');
    const tooltipP = tooltip.querySelector('p');

    let isHovered = false;
    let isFocused = false;

    const links = document.querySelectorAll('.column-card a');
    links.forEach(link => {
        link.addEventListener("focusin", () => {
            isFocused = true;
            updateTooltip(link, tooltip, tooltipH4, tooltipP, remove = false);
        });
        link.addEventListener("focusout", () => {
            isFocused = false;
            if (!isHovered) {
                updateTooltip(link, tooltip, tooltipH4, tooltipP, remove = true);
            }
        });
        link.addEventListener("mouseenter", () => {
            isHovered = true;
            updateTooltip(link, tooltip, tooltipH4, tooltipP, remove = false);
        });
        link.addEventListener("mouseleave", () => {
            isHovered = false;
            if (!isFocused) {
                updateTooltip(link, tooltip, tooltipH4, tooltipP, remove = true);
            }
        });
    });
});
