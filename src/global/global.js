// Set current page:
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('#rssite-header a');
    for (let i = 0; i < navLinks.length; i++) {
        const link = navLinks[i];
        const currentPath = window.location.pathname.replace(/(^\/|\/$)/g, '');
        const linkPath = link.pathname.replace(/(^\/|\/$)/g, '');
        
        if (currentPath === linkPath) {
            link.setAttribute("aria-current", "page");

            const dropContainer = link.closest(".nav-drop");
            if (dropContainer) {
                dropContainer.querySelector("button").setAttribute("aria-current", "page");
            }
        }
    }
});


// Handle .nav-drop aria-expanded
document.addEventListener("DOMContentLoaded", () => {
    const navDrops = document.querySelectorAll("#rssite-header .nav-drop");

    navDrops.forEach(drop => {
        const button = drop.querySelector("button")
        let isHovered = false;
        let isFocused = false;
        
        drop.addEventListener("focusin", () => {
            isFocused = true;
            button.setAttribute("aria-expanded", "true");
        });
        drop.addEventListener("focusout", () => {
            setTimeout(() => {
                isFocused = false;
                if (!isHovered) {
                    button.setAttribute("aria-expanded", "false");
                }
            }, 50);
        });
        drop.addEventListener("mouseenter", () => {
            isHovered = true;
            button.setAttribute("aria-expanded", "true");
        });
        drop.addEventListener("mouseleave", () => {
            isHovered = false;
            if (!isFocused) {
                button.setAttribute("aria-expanded", "false");
            }
        });
    });
});
