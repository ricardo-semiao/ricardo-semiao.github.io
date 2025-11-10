"use strict";

const globals = window.RSSITE;

const updateGo = function(item, img, go, remove) {
    if (remove) {
        img.setAttribute("aria-describedby", "go-info");
        go.self.setAttribute("aria-hidden", "true");

        go.img.src = "";
        go.img.alt = "";
    } else {
        img.setAttribute("aria-describedby", "go-info");
        go.self.setAttribute("aria-hidden", "false");

        go.img.src = img.src;
        go.img.alt = img.alt;

        go.title.textContent = img.getAttribute('alt');
        go.text.textContent = img.getAttribute('data-description');
        go.where.textContent = img.getAttribute('data-where');
        go.when.textContent = img.getAttribute('data-when');
    }
}

// const updateBackground = function(item, remove) {
//     if (remove) {
//         item.style.backgroundImage = "url('./costelas.png')";
//         item.style.backgroundSize = "cover";
//         item.style.backgroundPosition = "center";
//         item.style.opacity = "0.75";
//     } else {
//         item.style.backgroundImage = "";
//         item.style.backgroundSize = "";
//         item.style.backgroundPosition = "";
//         item.style.opacity = "";
//     }
// }


document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.querySelector('#gallery-overlay');
    const go = {
        self: overlay,
        closer: overlay.querySelector('.go-closer'),
        img: overlay.querySelector('.go-img'),
        title: overlay.querySelector('.go-title'),
        text: overlay.querySelector('.go-text'),
        where: overlay.querySelector('.go-wherewhen > :nth-child(1)'),
        when: overlay.querySelector('.go-wherewhen > :nth-child(2)')
    }
    const items = document.querySelectorAll('.gallery-item');

    items.forEach(item => {
        const img = item.querySelector('img')
        const args = [item, img, go];
        item.addEventListener("focusin", () => {
            updateGo(...args, false);
            img.style.opacity = "0";
            item.classList.replace("gallery-item", "gallery-hole");
            history.replaceState(null, "", window.location.pathname + "#" + item.id);
        });
        item.addEventListener("focusout", () => {
            updateGo(...args, true);
            img.style.opacity = "";
            item.classList.replace("gallery-hole", "gallery-item");
            history.replaceState(null, "", window.location.pathname);
        });
    });
});
