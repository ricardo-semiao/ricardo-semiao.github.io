"use strict";

const globals = window.RSSITE;

const updateGo = function(img, go, remove) {
    if (remove) {
        img.setAttribute("aria-describedby", "");
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

const updateGallery = function(go_context, go, remove) {
    if (remove) {
        updateGo(go_context.img, go, true);
        go_context.img.style.opacity = "";
        go_context.item.classList.replace("gallery-hole", "gallery-item");
        history.replaceState(null, "", window.location.pathname);
    } else {
        updateGo(go_context.img, go, false);
        go_context.img.style.opacity = "0";
        item.classList.replace("gallery-item", "gallery-hole");
        history.replaceState(null, "", window.location.pathname + "#" + item.id);
    }
}

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
const go_context = {
    img: null,
    item: null
}
let go_active = false;

document.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.gallery-item');

    items.forEach(item => {
        item.addEventListener("focusin", () => {
            if (!go_active) {
                go_active = true;
                go_context.img = item.querySelector('img');
                go_context.item = item;
                updateGallery(go_context, go, false);
                go.closer.focus();
            }
        });
        item.addEventListener("click", () => { // Reopen if it is already focused
            if (!go_active) {
                go_active = true;
                go_context.img = item.querySelector('img');
                go_context.item = item;
                updateGallery(go_context, go, false);
                go.closer.focus();
            }
        });
    });
});

go.closer.addEventListener('click', () => {
    if (go_active) {
        go_context.item.focus(); // Must be before updating go_active to not trigger focusin event
        go_active = false;
        updateGallery(go_context, go, true);
    }
});
