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
});
