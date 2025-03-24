const menuToggle = document.querySelector('.menu-toggle');
const sidebar = document.querySelector('.sidebar');

document.addEventListener('click', (event) => {
    const isMobile = window.innerWidth <= 768;
    const clickedNavItem = event.target.closest('.nav-item > .nav-title');
    const clickedSubnavItem = event.target.closest('.subnav li');
    const clickedMenuToggle = event.target.closest('.menu-toggle');
    const insideSidebar = sidebar.contains(event.target);
    
    if (clickedNavItem) {
        const isActive = clickedNavItem.classList.contains('active');
        document.querySelectorAll('.nav-title.active').forEach(el => {
            el.classList.remove('active');
            el.nextElementSibling.classList.remove('open');
        });
        if (!isActive) {
            clickedNavItem.classList.add('active');
            clickedNavItem.nextElementSibling.classList.add('open');
        }
    }
    
    if (clickedMenuToggle) {
        menuToggle.classList.toggle('active');
        sidebar.classList.toggle('active');
    }
    
    if (isMobile && (clickedSubnavItem || (!insideSidebar && !clickedMenuToggle && sidebar.classList.contains('active')))) {
        sidebar.classList.remove('active');
        menuToggle.classList.remove('active');
    }
});