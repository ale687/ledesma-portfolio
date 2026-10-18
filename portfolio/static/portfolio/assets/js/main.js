const toggle = document.getElementById('nav-toggle');
const menu = document.getElementById('nav-menu');
function closeMenu() {
    if (!menu || !toggle) return;
    menu.classList.remove('show');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open navigation');
}
if (toggle && menu) {
    toggle.addEventListener('click', () => {
        const open = menu.classList.toggle('show');
        toggle.setAttribute('aria-expanded', String(open));
        toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    });
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && menu.classList.contains('show')) {
            closeMenu();
            toggle.focus();
        }
    });
    document.addEventListener('click', (event) => {
        if (!menu.contains(event.target) && !toggle.contains(event.target)) closeMenu();
    });
    window.matchMedia('(min-width: 768px)').addEventListener('change', closeMenu);
}
document.querySelectorAll('.nav__link').forEach((link) => {
    if (new URL(link.href).pathname === window.location.pathname) {
        link.classList.add('active-link');
        link.setAttribute('aria-current', 'page');
    }
    link.addEventListener('click', closeMenu);
});
if (typeof ScrollReveal === 'function' && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const sr = ScrollReveal({ origin: 'top', distance: '20px', duration: 600, delay: 100 });
    sr.reveal('.home__data, .about__img, .skills__subtitle, .skills__text');
    sr.reveal('.home__img, .about__subtitle, .about__text, .skills__img', { delay: 200 });
    sr.reveal('.home__social-icon, .skills__data', { interval: 80 });
}
