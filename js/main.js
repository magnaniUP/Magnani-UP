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
