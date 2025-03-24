const menuToggle = document.querySelector('.menu-toggle');
const sidebar = document.querySelector('.sidebar');

document.addEventListener('click', (event) => {
    const isMobile = window.innerWidth <= 768;
    const clickedNavItem = event.target.closest('.nav-item > .nav-title');
    const clickedSubnavItem = event.target.closest('.subnav li');
    const clickedMenuToggle = event.target.closest('.menu-toggle');
    const insideSidebar = sidebar.contains(event.target);
    
    if (clickedNavItem) {
        const isActive = clickedNavItem.classList.contains('current');
        document.querySelectorAll('.nav-title.current').forEach(el => {
            el.classList.remove('current');
            el.nextElementSibling.classList.remove('open');
        });
        if (!isActive) {
            clickedNavItem.classList.add('current');
            clickedNavItem.nextElementSibling.classList.add('open');
        }
    }
    
    if (clickedMenuToggle) {
        menuToggle.classList.toggle('current');
        sidebar.classList.toggle('current');
    }
    
    if (isMobile && (clickedSubnavItem || (!insideSidebar && !clickedMenuToggle && sidebar.classList.contains('current')))) {
        sidebar.classList.remove('current');
        menuToggle.classList.remove('current');
    }
});