const inkOverlayElement = document.getElementById('ink-overlay');
const paperOverlayElement = document.getElementById('paper-overlay');


document.getElementById('add-ink-btn').addEventListener('click', () => {
    inkOverlayElement.style.display = 'flex';
});

document.getElementById('add-paper-btn').addEventListener('click', () => {
    paperOverlayElement.style.display = 'flex'
})

document.getElementById('overlay-close').addEventListener('click', () => {
    inkOverlayElement.style.display = 'none';
})

document.getElementById('paper-overlay-close').addEventListener('click', () => {
    paperOverlayElement.style.display = 'none';
})
