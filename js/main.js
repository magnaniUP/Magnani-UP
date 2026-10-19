/**
 * Magnani UP® - Main Entrypoint & Conversion Interceptor
 */

const WHATSAPP_CONTACTS = {
  br: 'https://wa.me/5544998018242',
  pt: 'https://wa.me/393313882760',
  it: 'https://wa.me/393313882760'
};

function getWhatsAppUrl() {
  const path = window.location.pathname.toLowerCase();
  if (path.includes('/br/')) {
    return WHATSAPP_CONTACTS.br;
  }
  if (path.includes('/it/')) {
    return WHATSAPP_CONTACTS.it;
  }
  return WHATSAPP_CONTACTS.pt;
}

document.addEventListener('DOMContentLoaded', () => {
  console.log('Magnani UP® - Inicializado com sucesso para 3 mercados (PT, BR, IT).');

  // Garante que todos os botões de ação e conversão apontem e abram o WhatsApp correto
  const waUrl = getWhatsAppUrl();
  const ctaButtons = document.querySelectorAll('.btn-cta, .cta-btn, .hero-btn-primary, .footer-contact-btn');
  ctaButtons.forEach(btn => {
    btn.setAttribute('href', waUrl);
    btn.setAttribute('target', '_blank');
    btn.setAttribute('rel', 'noopener noreferrer');
  });

  // Listener global como garantia absoluta
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-cta, .cta-btn, .hero-btn-primary, .footer-contact-btn');
    if (btn) {
      btn.setAttribute('href', waUrl);
      btn.setAttribute('target', '_blank');
      btn.setAttribute('rel', 'noopener noreferrer');
    }
  }, { capture: true });

  // Torna todo o card de serviço clicável com transição suave
  document.querySelectorAll('.service-card').forEach((card) => {
    card.addEventListener('click', (e) => {
      if (e.target.closest('a')) return; // se clicou direto no link do título ou botão, deixa o navegador navegar
      const link = card.querySelector('.service-card-btn, .service-card-title-link');
      if (link && link.href) {
        window.location.href = link.href;
      }
    });
  });

  // Slider interativo de Portfólio no Mobile (Sincronização de Dots e Navegação)
  const portfolioGrid = document.querySelector('.sites-portfolio-grid');
  const portfolioDots = document.querySelectorAll('.sites-portfolio-dot');
  if (portfolioGrid && portfolioDots.length > 0) {
    const cards = portfolioGrid.querySelectorAll('.sites-portfolio-card');
    let isClickScrolling = false;

    portfolioGrid.addEventListener('scroll', () => {
      if (isClickScrolling) return;
      const scrollLeft = portfolioGrid.scrollLeft;
      const cardWidth = cards[0]?.offsetWidth || 1;
      const gap = 16;
      const activeIndex = Math.min(
        cards.length - 1,
        Math.max(0, Math.round(scrollLeft / (cardWidth + gap)))
      );
      portfolioDots.forEach((dot, idx) => {
        dot.classList.toggle('active', idx === activeIndex);
      });
    }, { passive: true });

    portfolioDots.forEach((dot, idx) => {
      dot.addEventListener('click', () => {
        isClickScrolling = true;
        portfolioDots.forEach((d, i) => d.classList.toggle('active', i === idx));
        if (cards[idx]) {
          cards[idx].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
          setTimeout(() => { isClickScrolling = false; }, 400);
        }
      });
    });
  }

  // Em ambiente local de desenvolvimento (localhost), ajusta URLs de produção para navegação local
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    document.querySelectorAll('a[href^="https://www.magnaniup.com/"]').forEach((link) => {
      const currentHref = link.getAttribute('href');
      if (currentHref && currentHref.startsWith('https://www.magnaniup.com/')) {
        link.setAttribute('href', currentHref.replace('https://www.magnaniup.com', ''));
      }
    });
  }
});
