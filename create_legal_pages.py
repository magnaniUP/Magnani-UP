import os

LEGAL_PAGES = {
    'pt': {
        'privacidade': {
            'dir': 'pt/privacidade',
            'title': 'Política de Privacidade | Magnani UP®',
            'h1': 'Política de Privacidade',
            'desc': 'A sua privacidade é fundamental para nós. Esta política descreve como a Magnani UP® recolhe, utiliza e protege os seus dados pessoais de acordo com o RGPD.'
        },
        'termos': {
            'dir': 'pt/termos',
            'title': 'Termos e Condições | Magnani UP®',
            'h1': 'Termos e Condições de Utilização',
            'desc': 'Ao utilizar o website da Magnani UP®, concorda com os termos e condições gerais aqui descritos para a prestação de serviços digitais.'
        }
    },
    'br': {
        'privacidade': {
            'dir': 'br/privacidade',
            'title': 'Política de Privacidade | Magnani UP®',
            'h1': 'Política de Privacidade',
            'desc': 'A privacidade dos seus dados é prioridade na Magnani UP®. Esta política detalha como coletamos, tratamos e protegemos suas informações conforme a LGPD.'
        },
        'termos': {
            'dir': 'br/termos',
            'title': 'Termos e Condições | Magnani UP®',
            'h1': 'Termos e Condições de Uso',
            'desc': 'Estes termos regulam a navegação e a utilização dos serviços apresentados no website da Magnani UP®.'
        }
    },
    'it': {
        'privacidade': {
            'dir': 'it/privacidade',
            'title': 'Informativa sulla Privacy | Magnani UP®',
            'h1': 'Informativa sulla Privacy',
            'desc': 'La tua privacy è fondamentale per noi. Questa informativa descrive come Magnani UP® raccoglie, gestisce e protegge i tuoi dati personali in conformità al GDPR.'
        },
        'termos': {
            'dir': 'it/termos',
            'title': 'Termini e Condizioni | Magnani UP®',
            'h1': 'Termini e Condizioni di Utilizzo',
            'desc': 'I presenti termini stabiliscono le condizioni di utilizzo del sito web e dei servizi digitali offerti da Magnani UP®.'
        }
    }
}

for lang, pages in LEGAL_PAGES.items():
    for ptype, info in pages.items():
        os.makedirs(info['dir'], exist_ok=True)
        html = f'''<!DOCTYPE html>
<html lang="{lang}" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{info['title']}</title>
  <meta name="description" content="{info['desc']}">
  <meta name="robots" content="noindex, follow">
  <link rel="icon" type="image/svg+xml" href="../../images/logo/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../css/reset.css?v=20">
  <link rel="stylesheet" href="../../css/global.css?v=20">
  <link rel="stylesheet" href="../../css/header.css?v=20">
  <link rel="stylesheet" href="../../css/internal.css?v=20">
  <link rel="stylesheet" href="../../css/footer.css?v=20">
  <link rel="stylesheet" href="../../css/responsive.css?v=20">
</head>
<body>
  <div class="page-wrapper">
    <header class="site-header" id="site-header">
      <div class="header-container">
        <a href="/{lang}/" class="brand-logo" aria-label="Magnani UP®">
          <span class="brand-logo-content">
            <span class="brand-name">
              <span class="brand-name-main">Magnani</span>
              <span class="brand-name-up">UP</span>
              <sup class="brand-registered">®</sup>
            </span>
          </span>
        </a>
        <nav class="site-nav" id="main-nav" aria-label="Navegação">
          <ul class="nav-list">
            <li class="nav-item"><a href="/{lang}/" class="nav-link">Voltar ao Site</a></li>
          </ul>
        </nav>
      </div>
    </header>

    <main class="main-content-stage" id="conteudo-principal">
      <section class="internal-hero-section" style="padding: 140px 0 60px 0;">
        <div class="internal-hero-container">
          <h1 class="internal-hero-title">{info['h1']}</h1>
          <p class="internal-hero-desc">{info['desc']}</p>
          <div style="color: var(--color-text-muted); font-size: 1rem; line-height: 1.8; max-width: 800px; margin-top: 32px;">
            <p style="margin-bottom: 16px;">A Magnani UP® respeita rigorosamente a confidencialidade e a segurança de todos os dados tratados através deste website e de canais de atendimento digital.</p>
            <p style="margin-bottom: 24px;">Para dúvidas adicionais sobre a nossa política de dados ou termos contratuais, contacte a nossa equipa através dos canais oficiais indicados no website.</p>
            <a href="/{lang}/" class="btn-cta" style="display: inline-flex;"><span>Regressar à Página Inicial</span></a>
          </div>
        </div>
      </section>
    </main>

    <footer class="site-footer" id="site-footer" aria-label="Rodapé">
      <div class="footer-container">
        <div class="footer-bottom-bar" style="border-top: none; padding-top: 0;">
          <p class="footer-copyright">&copy; 2026 Magnani UP&reg;. Todos os direitos reservados.</p>
        </div>
      </div>
    </footer>
  </div>
</body>
</html>'''
        fpath = os.path.join(info['dir'], 'index.html')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Created legal page {fpath}")
