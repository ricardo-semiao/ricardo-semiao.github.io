"use strict";

const updateTooltip = function(li, a, pt, remove) {
    if (remove) {
        a.removeAttribute("aria-describedby")
        pt.self.setAttribute("aria-hidden", "true");
    } else {
        a.setAttribute("aria-describedby", "projects-tooltip");

        pt.title.textContent = a.textContent
        pt.text.textContent = a.getAttribute('data-description');

        pt.self.setAttribute("aria-hidden", "false");

        // Position calculation:
        const aRect = a.getBoundingClientRect();
        const viewportDims = {
            "height": document.documentElement.clientHeight,
            "width": document.documentElement.clientWidth
        };
        const tooltipDims = {"height": pt.self.offsetHeight, "width": pt.self.offsetWidth};

        const mainWidth = parseFloat(getComputedStyle(document.querySelector("#rssite-header > nav")).width);
        padding = (viewportDims.width - mainWidth) / 2;

        const left = aRect.left + aRect.width / 2; // Also consider other centering options
        const excessRight = Math.max(0, left + tooltipDims.width - viewportDims.width);
        pt.self.style.left = Math.max(left - excessRight - padding, padding) + "px";

        const excessTop = aRect.top - 4 - tooltipDims.height;
        const top = excessTop > 0 ? excessTop : aRect.bottom + 4;
        pt.self.style.top = top + window.scrollY + "px";
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const projects_tooltip = document.querySelector('#projects-tooltip');
    const pt = {
        self: projects_tooltip,
        title: projects_tooltip.querySelector('.pt-title'),
        text: projects_tooltip.querySelector('.pt-text')
    };

    let isHovered = false;
    let isFocused = false;

    const lis = document.querySelectorAll('.column-card li');
    lis.forEach(li => {
        const args = [li, li.querySelector('a'), pt];
        li.addEventListener("focusin", () => {
            isFocused = true;
            updateTooltip(...args, remove = false);
        });
        li.addEventListener("focusout", () => {
            isFocused = false;
            if (!isHovered) {
                updateTooltip(...args, remove = true);
            }
        });
        li.addEventListener("mouseenter", () => {
            isHovered = true;
            updateTooltip(...args, remove = false);
        });
        li.addEventListener("mouseleave", () => {
            isHovered = false;
            if (!isFocused) {
                updateTooltip(...args, remove = true);
            }
        });
    });
});
