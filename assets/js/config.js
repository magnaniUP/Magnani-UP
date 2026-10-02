/**
 * Magnani UP® - Regional Configuration & Routes
 */

const REGIONAL_CONFIG = {
  pt: {
    country: 'Portugal',
    lang: 'pt-PT',
    locale: 'pt_PT',
    baseUrl: '/pt/',
    domain: 'https://dominio.com/pt/',
    nav: {
      inicio: { label: 'Início', path: '/pt/' },
      servicos: { label: 'Serviços', path: '/pt/servicos/' },
      sobre: { label: 'Sobre', path: '/pt/sobre/' },
      faq: { label: 'FAQ', path: '/pt/faq/' },
      contato: { label: 'Contato', path: '/pt/contacto/' }
    },
    cta: {
      label: 'Vamos conversar',
      path: '/pt/contacto/'
    }
  },
  br: {
    country: 'Brasil',
    lang: 'pt-BR',
    locale: 'pt_BR',
    baseUrl: '/br/',
    domain: 'https://dominio.com/br/',
    nav: {
      inicio: { label: 'Início', path: '/br/' },
      servicos: { label: 'Serviços', path: '/br/servicos/' },
      sobre: { label: 'Sobre', path: '/br/sobre/' },
      faq: { label: 'FAQ', path: '/br/faq/' },
      contato: { label: 'Contato', path: '/br/contato/' }
    },
    cta: {
      label: 'Vamos conversar',
      path: '/br/contato/'
    }
  }
};

function getCurrentRegion() {
  const path = window.location.pathname;
  if (path.startsWith('/pt') || document.documentElement.lang === 'pt-PT') {
    return 'pt';
  }
  if (path.startsWith('/br') || document.documentElement.lang === 'pt-BR') {
    return 'br';
  }
  return 'pt';
}

window.MagnaniConfig = {
  regions: REGIONAL_CONFIG,
  getCurrentRegion: getCurrentRegion
};
