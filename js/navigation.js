/**
 * Magnani UP® - Multi-market Navigation & Equivalence Router
 * Suporte completo a 3 mercados: Portugal (pt-PT), Brasil (pt-BR), Itália (it-IT)
 */

const MARKETS_CONFIG = {
  pt: {
    code: 'pt-PT',
    locale: 'pt_PT',
    name: 'Portugal',
    flag: '🇵🇹',
    baseUrl: '/pt/',
    routes: {
      inicio: '/pt/',
      servicos: '/pt/servicos/',
      sobre: '/pt/sobre/',
      faq: '/pt/faq/',
      contato: '/pt/contacto/'
    },
    labels: {
      inicio: 'Início',
      servicos: 'Serviços',
      sobre: 'Sobre',
      faq: 'FAQ',
      contato: 'Contato',
      cta: 'Vamos conversar'
    }
  },
  br: {
    code: 'pt-BR',
    locale: 'pt_BR',
    name: 'Brasil',
    flag: '🇧🇷',
    baseUrl: '/br/',
    routes: {
      inicio: '/br/',
      servicos: '/br/servicos/',
      sobre: '/br/sobre/',
      faq: '/br/faq/',
      contato: '/br/contato/'
    },
    labels: {
      inicio: 'Início',
      servicos: 'Serviços',
      sobre: 'Sobre',
      faq: 'FAQ',
      contato: 'Contato',
      cta: 'Vamos conversar'
    }
  },
  it: {
    code: 'it-IT',
    locale: 'it_IT',
    name: 'Italia',
    flag: '🇮🇹',
    baseUrl: '/it/',
    routes: {
      inicio: '/it/',
      servicos: '/it/servizi/',
      sobre: '/it/chi-siamo/',
      faq: '/it/faq/',
      contato: '/it/contatti/'
    },
    labels: {
      inicio: 'Home',
      servicos: 'Servizi',
      sobre: 'Chi siamo',
      faq: 'FAQ',
      contato: 'Contatti',
      cta: 'Parliamo'
    }
  }
};

/**
 * Retorna a URL equivalente da página atual em outro mercado
 */
function getEquivalentUrl(targetMarket, currentPath = window.location.pathname) {
  const target = MARKETS_CONFIG[targetMarket];
  if (!target) return '/pt/';

  // Identifica a seção semântica atual
  let section = 'inicio';
  if (currentPath.includes('/servicos/') || currentPath.includes('/servizi/')) {
    section = 'servicos';
  } else if (currentPath.includes('/sobre/') || currentPath.includes('/chi-siamo/')) {
    section = 'sobre';
  } else if (currentPath.includes('/faq/')) {
    section = 'faq';
  } else if (currentPath.includes('/contacto/') || currentPath.includes('/contato/') || currentPath.includes('/contatti/')) {
    section = 'contato';
  }

  return target.routes[section] || target.baseUrl;
}

/**
 * Inicializador da navegação e interações do Header
 */
function initNavigation() {
  const header = document.getElementById('site-header');
  const toggleBtn = document.getElementById('hamburger-toggle');
  const drawer = document.getElementById('mobile-drawer');
  const overlay = document.getElementById('mobile-overlay');

  if (!header) return;

  // Efeito de rolagem suave (blur adesivo)
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

  // Menu móvel acessível
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

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && isMenuOpen) {
        closeMenu();
      }
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
}

// Expõe helpers internacionalizados globalmente
window.MagnaniNav = {
  markets: MARKETS_CONFIG,
  getEquivalentUrl: getEquivalentUrl,
  init: initNavigation
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initNavigation);
} else {
  initNavigation();
}
