/**
 * Magnani UP® - Header Controller & Regional Language Switcher
 */

(function () {
  'use strict';

  function initHeader() {
    const header = document.getElementById('site-header');
    const toggleBtn = document.getElementById('hamburger-toggle');
    const drawer = document.getElementById('mobile-drawer');
    const overlay = document.getElementById('mobile-overlay');

    if (!header) return;

    // 1. Scroll effect (fundo com blur ao rolar)
    let lastScrollY = window.scrollY;
    let ticking = false;

    function onScroll() {
      lastScrollY = window.scrollY;
      if (!ticking) {
        window.requestAnimationFrame(() => {
          if (lastScrollY > 20) {
            header.classList.add('scrolled');
          } else {
            header.classList.remove('scrolled');
          }
          ticking = false;
        });
        ticking = true;
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // 2. Menu mobile drawer
    if (toggleBtn && drawer) {
      let isMenuOpen = false;

      function openMenu() {
        isMenuOpen = true;
        toggleBtn.setAttribute('aria-expanded', 'true');
        toggleBtn.setAttribute('aria-label', 'Fechar menu de navegação');
        drawer.classList.add('open');
        if (overlay) overlay.classList.add('active');
        document.body.classList.add('menu-open');

        const firstFocusable = drawer.querySelector('a, button');
        if (firstFocusable) {
          setTimeout(() => firstFocusable.focus(), 100);
        }
      }

      function closeMenu() {
        if (!isMenuOpen) return;
        isMenuOpen = false;
        toggleBtn.setAttribute('aria-expanded', 'false');
        toggleBtn.setAttribute('aria-label', 'Abrir menu de navegação');
        drawer.classList.remove('open');
        if (overlay) overlay.classList.remove('active');
        document.body.classList.remove('menu-open');
        toggleBtn.focus();
      }

      function toggleMenu() {
        if (isMenuOpen) {
          closeMenu();
        } else {
          openMenu();
        }
      }

      toggleBtn.addEventListener('click', toggleMenu);

      if (overlay) {
        overlay.addEventListener('click', closeMenu);
      }

      const drawerLinks = drawer.querySelectorAll('a');
      drawerLinks.forEach((link) => {
        link.addEventListener('click', () => {
          closeMenu();
        });
      });

      window.addEventListener(
        'resize',
        () => {
          if (window.innerWidth > 991 && isMenuOpen) {
            closeMenu();
          }
        },
        { passive: true }
      );
    }

    // 3. Troca direta de versão ao clicar nas bandeiras (Portugal / Brasil)
    function switchRegion(targetRegion) {
      const currentPath = window.location.pathname;
      let newPath = '/pt/';

      if (targetRegion === 'br') {
        if (currentPath.includes('/pt/contacto/') || currentPath.includes('/pt/contato/')) {
          newPath = '/br/contato/';
        } else if (currentPath.includes('/pt/servicos/')) {
          newPath = '/br/servicos/';
        } else if (currentPath.includes('/pt/sobre/')) {
          newPath = '/br/sobre/';
        } else if (currentPath.includes('/pt/faq/')) {
          newPath = '/br/faq/';
        } else {
          newPath = '/br/';
        }
      } else {
        if (currentPath.includes('/br/contato/') || currentPath.includes('/br/contacto/')) {
          newPath = '/pt/contacto/';
        } else if (currentPath.includes('/br/servicos/')) {
          newPath = '/pt/servicos/';
        } else if (currentPath.includes('/br/sobre/')) {
          newPath = '/pt/sobre/';
        } else if (currentPath.includes('/br/faq/')) {
          newPath = '/pt/faq/';
        } else {
          newPath = '/pt/';
        }
      }

      // Navega imediatamente para a versão correspondente
      window.location.href = newPath;
    }

    document.querySelectorAll('.flag-link, .mobile-flag-btn').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        const target = btn.getAttribute('data-lang');
        if (target) {
          e.preventDefault();
          switchRegion(target);
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeader);
  } else {
    initHeader();
  }
})();
