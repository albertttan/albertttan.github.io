async function shuffle() {
    const response = await fetch('/portfolio/photos/static/images.json');
    const images = await response.json();
    const img = new Image();
    img.src = `/portfolio/photos/static/${images[Math.floor(Math.random() * images.length)]}`;
    img.onload = () => {
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        ctx.imageSmoothingEnabled = false;
        ctx.drawImage(img, 
            Math.round(Math.random() * (img.width - 16)),
            Math.round(Math.random() * (img.height - 16)),
            16, 16, 0, 0, canvas.width, canvas.height
        );
        document.getElementById('full-memory').href = img.src;
    };
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('shuffle').addEventListener('click', shuffle);
    shuffle();
});
