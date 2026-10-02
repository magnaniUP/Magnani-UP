/**
 * Magnani UP® — Controle Interativo do Accordion FAQ (/js/faq.js)
 * Vanilla JS com foco em Acessibilidade (WAI-ARIA) e Animação Fluida
 */

document.addEventListener('DOMContentLoaded', () => {
  const faqSection = document.querySelector('.faq-section');
  if (!faqSection) return;

  const faqItems = faqSection.querySelectorAll('.faq-item');
  const faqButtons = faqSection.querySelectorAll('.faq-question-btn');

  /**
   * Fecha um item do FAQ
   * @param {HTMLElement} item
   * @param {HTMLButtonElement} btn
   * @param {HTMLElement} panel
   */
  function closeItem(item, btn, panel) {
    item.classList.remove('is-open');
    btn.setAttribute('aria-expanded', 'false');
    if (panel) {
      panel.setAttribute('aria-hidden', 'true');
    }
  }

  /**
   * Abre um item do FAQ
   * @param {HTMLElement} item
   * @param {HTMLButtonElement} btn
   * @param {HTMLElement} panel
   */
  function openItem(item, btn, panel) {
    item.classList.add('is-open');
    btn.setAttribute('aria-expanded', 'true');
    if (panel) {
      panel.setAttribute('aria-hidden', 'false');
    }
  }

  // Inicializa o estado de acessibilidade (todos fechados por padrão)
  faqItems.forEach((item) => {
    const btn = item.querySelector('.faq-question-btn');
    const panelId = btn ? btn.getAttribute('aria-controls') : null;
    const panel = panelId ? document.getElementById(panelId) : item.querySelector('.faq-answer-panel');

    if (btn && panel) {
      btn.setAttribute('aria-expanded', 'false');
      panel.setAttribute('aria-hidden', 'true');
    }
  });

  // Manipulador de clique para alternância (Accordion: apenas 1 aberto por vez)
  faqButtons.forEach((btn, index) => {
    btn.addEventListener('click', () => {
      const currentItem = btn.closest('.faq-item');
      if (!currentItem) return;

      const isOpen = btn.getAttribute('aria-expanded') === 'true';
      const panelId = btn.getAttribute('aria-controls');
      const panel = panelId ? document.getElementById(panelId) : currentItem.querySelector('.faq-answer-panel');

      // Fecha todos os outros itens abertos
      faqItems.forEach((otherItem) => {
        if (otherItem !== currentItem) {
          const otherBtn = otherItem.querySelector('.faq-question-btn');
          const otherPanelId = otherBtn ? otherBtn.getAttribute('aria-controls') : null;
          const otherPanel = otherPanelId ? document.getElementById(otherPanelId) : otherItem.querySelector('.faq-answer-panel');
          if (otherBtn) {
            closeItem(otherItem, otherBtn, otherPanel);
          }
        }
      });

      // Alterna o item atual
      if (isOpen) {
        closeItem(currentItem, btn, panel);
      } else {
        openItem(currentItem, btn, panel);
      }
    });

    // Navegação por teclado aprimorada (Setas para Cima/Baixo, Home, End)
    btn.addEventListener('keydown', (e) => {
      let targetIndex = null;
      if (e.key === 'ArrowDown') {
        targetIndex = (index + 1) % faqButtons.length;
      } else if (e.key === 'ArrowUp') {
        targetIndex = (index - 1 + faqButtons.length) % faqButtons.length;
      } else if (e.key === 'Home') {
        targetIndex = 0;
      } else if (e.key === 'End') {
        targetIndex = faqButtons.length - 1;
      }

      if (targetIndex !== null) {
        e.preventDefault();
        faqButtons[targetIndex].focus();
      }
    });
  });
});
