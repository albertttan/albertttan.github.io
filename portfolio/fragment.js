const images = ['1.jpeg', '2.jpeg', '3.jpeg'];

function shuffle() {
    const img = new Image();
    img.src = `/portfolio/photos/static/${images[Math.floor(Math.random() * images.length)]}`;
    img.onload = () => {
        const x = Math.round(Math.random() * (img.width - 16)), y = Math.round(Math.random() * (img.height - 16));
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        ctx.imageSmoothingEnabled = false;
        ctx.drawImage(img, x, y, 16, 16, 0, 0, canvas.width, canvas.height);
        document.getElementById('original-link').href = img.src;
    };
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('shuffle').addEventListener('click', shuffle);
    shuffle();
});
