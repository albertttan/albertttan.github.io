const menuToggle = document.querySelector('.menu-toggle');
const sidebar = document.querySelector('.sidebar');

// Ensure sidebar is shown by default on mobile
if (window.innerWidth <= 768) {
    sidebar.classList.add('current');
}

menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('current');
    menuToggle.classList.toggle('current');
});

document.addEventListener('click', (event) => {
    if (window.innerWidth > 768) return;
    
    const insideSidebar = sidebar.contains(event.target);
    const clickedMenuToggle = menuToggle.contains(event.target);
    
    if (!insideSidebar && !clickedMenuToggle) {
        sidebar.classList.remove('current');
        menuToggle.classList.remove('current');
    }
});
