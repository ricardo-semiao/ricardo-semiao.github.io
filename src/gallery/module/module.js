"use strict";

const globals = window.RSSITE;

const updateGo = function(item, img, go) {
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
        const args = [item, item.querySelector('img'), go];
        item.addEventListener("focusin", () => {
            updateGo(...args, remove = false);
            item.style.backgroundColor = "var(--gray);";
            history.replaceState(null, "", window.location.pathname + "#" + item.id);
        });
        item.addEventListener("focusout", () => {
            updateGo(...args, remove = true);
            item.style.backgroundColor = "";
            history.replaceState(null, "", window.location.pathname);
        });
    });
});
