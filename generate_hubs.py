import os
import json
from scratch_services_data import DATA

HUB_CONFIG = {
    'pt': {
        'path': 'pt/servicos/index.html',
        'title': 'Serviços Digitais e Criação de Websites em Portugal | Magnani UP®',
        'meta_desc': 'Conheça os serviços digitais da Magnani UP® em Portugal: criação de websites, SEO, landing pages, tráfego pago, sistemas e gestão de Google Perfil de Empresa.',
        'h1': 'Serviços Digitais Especializados para Empresas',
        'hero_desc': 'Da estratégia de atração ao desenvolvimento técnico sob medida, criamos soluções digitais completas para que a sua empresa conquiste relevância, atraia clientes e cresça no digital.',
        'tag': 'OS NOSSOS SERVIÇOS',
        'cards': [
            {
                'slug': 'criacao-de-sites',
                'title': 'Criação de Websites Profissionais',
                'desc': 'Desenvolvimento de websites modernos, rápidos e responsivos para fortalecer a presença digital e transformar o site num verdadeiro ponto de contacto.',
                'link': '/pt/servicos/criacao-de-sites/',
                'link_label': 'Conhecer Criação de Websites'
            },
            {
                'slug': 'seo',
                'title': 'SEO (Otimização para Motores de Busca)',
                'desc': 'Melhoramos o posicionamento orgânico do seu website no Google para atrair tráfego qualificado de forma contínua.',
                'link': '/pt/servicos/seo/',
                'link_label': 'Conhecer serviço de SEO'
            },
            {
                'slug': 'landing-pages',
                'title': 'Criação de Landing Pages',
                'desc': 'Páginas desenvolvidas com foco exclusivo em conversão rápida para transformar visitantes em oportunidades de negócio.',
                'link': '/pt/servicos/landing-pages/',
                'link_label': 'Conhecer Landing Pages'
            },
            {
                'slug': 'trafego-pago',
                'title': 'Tráfego Pago & Google Ads',
                'desc': 'Gestão estratégica de campanhas patrocinadas no Google e redes sociais para alcançar clientes prontos para comprar.',
                'link': '/pt/servicos/trafego-pago/',
                'link_label': 'Conhecer Tráfego Pago'
            },
            {
                'slug': 'sistemas',
                'title': 'Criação de Sistemas Personalizados',
                'desc': 'Plataformas web e automações desenvolvidas sob medida para simplificar rotinas e otimizar processos operacionais.',
                'link': '/pt/servicos/sistemas/',
                'link_label': 'Conhecer Criação de Sistemas'
            },
            {
                'slug': 'google-meu-negocio',
                'title': 'Gestão de Google Meu Negócio',
                'desc': 'Otimização e gestão do Perfil de Empresa no Google Maps para conquistar máxima visibilidade nas pesquisas locais.',
                'link': '/pt/servicos/google-meu-negocio/',
                'link_label': 'Conhecer Google Meu Negócio'
            }
        ]
    },
    'br': {
        'path': 'br/servicos/index.html',
        'title': 'Serviços Digitais e Criação de Sites | Magnani UP®',
        'meta_desc': 'Conheça os serviços digitais da Magnani UP®: criação de sites, SEO, landing pages, tráfego pago, desenvolvimento de sistemas e Google Meu Negócio.',
        'h1': 'Serviços Digitais Especializados para Empresas',
        'hero_desc': 'Da estratégia de atração ao desenvolvimento tecnológico avançado, oferecemos soluções completas para fortalecer a presença digital da sua empresa e gerar resultados reais.',
        'tag': 'NOSSOS SERVIÇOS',
        'cards': [
            {
                'slug': 'criacao-de-sites',
                'title': 'Criação de Websites Profissionais',
                'desc': 'Desenvolvimento de websites modernos, rápidos e responsivos para fortalecer a presença digital e transformar o site num verdadeiro ponto de contacto.',
                'link': '/pt/servicos/criacao-de-sites/',
                'link_label': 'Conhecer Criação de Websites'
            },
            {
                'slug': 'seo',
                'title': 'SEO (Otimização para Mecanismos de Busca)',
                'desc': 'Melhoramos o posicionamento orgânico do seu site no Google para atrair clientes qualificados de forma contínua.',
                'link': '/br/servicos/seo/',
                'link_label': 'Conhecer serviço de SEO'
            },
            {
                'slug': 'landing-pages',
                'title': 'Criação de Landing Pages',
                'desc': 'Páginas desenvolvidas com foco exclusivo em conversão rápida para transformar visitantes em contatos comerciais.',
                'link': '/br/servicos/landing-pages/',
                'link_label': 'Conhecer Landing Pages'
            },
            {
                'slug': 'trafego-pago',
                'title': 'Tráfego Pago & Google Ads',
                'desc': 'Gestão estratégica de anúncios no Google Ads e redes sociais para conectar sua oferta a compradores potenciais.',
                'link': '/br/servicos/trafego-pago/',
                'link_label': 'Conhecer Tráfego Pago'
            },
            {
                'slug': 'sistemas',
                'title': 'Desenvolvimento de Sistemas',
                'desc': 'Sistemas web e ferramentas sob medida para automatizar tarefas manuais e organizar os processos da sua empresa.',
                'link': '/br/servicos/sistemas/',
                'link_label': 'Conhecer Sistemas'
            },
            {
                'slug': 'google-meu-negocio',
                'title': 'Gestão do Google Meu Negócio',
                'desc': 'Otimização de Perfil de Empresa e Google Maps para destacar sua empresa nas buscas locais da sua região.',
                'link': '/br/servicos/google-meu-negocio/',
                'link_label': 'Conhecer Google Meu Negócio'
            }
        ]
    },
    'it': {
        'path': 'it/servizi/index.html',
        'title': 'Servizi Digitali e Creazione Siti Web | Magnani UP®',
        'meta_desc': 'Scopri tutti i servizi digitali di Magnani UP®: creazione siti web, SEO, landing page ad alta conversione, Google Ads, sviluppo sistemi e Google Business Profile.',
        'h1': 'Servizi Digitali Specializzati per Aziende',
        'hero_desc': 'Dalla strategia di visibilità allo sviluppo tecnologico personalizzato, offriamo soluzioni digitali complete per aiutare la tua azienda a crescere e ottenere risultati concreti.',
        'tag': 'I NOSTRI SERVIZI',
        'cards': [
            {
                'slug': 'criacao-de-sites',
                'title': 'Criação de Websites Profissionais',
                'desc': 'Desenvolvimento de websites modernos, rápidos e responsivos para fortalecer a presença digital e transformar o site num verdadeiro ponto de contacto.',
                'link': '/pt/servicos/criacao-de-sites/',
                'link_label': 'Conhecer Criação de Websites'
            },
            {
                'slug': 'seo',
                'title': 'SEO (Posizionamento sui Motori di Ricerca)',
                'desc': 'Miglioriamo la visibilità organica del tuo sito web su Google per intercettare visitatori qualificati in modo continuativo.',
                'link': '/it/servizi/seo/',
                'link_label': 'Scopri il servizio SEO'
            },
            {
                'slug': 'landing-page',
                'title': 'Creazione Landing Page',
                'desc': 'Pagine web studiate con focus esclusivo sulla conversione rapida per trasformare gli utenti in clienti reali.',
                'link': '/it/servizi/landing-page/',
                'link_label': 'Scopri le Landing Page'
            },
            {
                'slug': 'traffico-a-pagamento',
                'title': 'Traffico a Pagamento & Google Ads',
                'desc': 'Gestione strategica di annunci su Google e social network per raggiungere utenti con reale intenzione d\'acquisto.',
                'link': '/it/servizi/traffico-a-pagamento/',
                'link_label': 'Scopri il Traffico a Pagamento'
            },
            {
                'slug': 'sistemi',
                'title': 'Sviluppo Sistemi Personalizzati',
                'desc': 'Piattaforme web e software su misura per ottimizzare i processi aziendali e automatizzare la gestione operativa.',
                'link': '/it/servizi/sistemi/',
                'link_label': 'Scopri lo Sviluppo Sistemi'
            },
            {
                'slug': 'google-business-profile',
                'title': 'Gestione Google Business Profile',
                'desc': 'Ottimizzazione della scheda aziendale su Google Maps e ricerche locali per farsi trovare dai clienti della tua zona.',
                'link': '/it/servizi/google-business-profile/',
                'link_label': 'Scopri Google Business Profile'
            }
        ]
    }
}

from generate_services import SERVICE_ICONS

def render_hub(lang_code):
    cfg = HUB_CONFIG[lang_code]
    d = DATA[lang_code]
    
    pt_url = "https://dominio.com/pt/servicos/"
    br_url = "https://dominio.com/br/servicos/"
    it_url = "https://dominio.com/it/servizi/"
    canonical = pt_url if lang_code == 'pt' else (br_url if lang_code == 'br' else it_url)
    
    if lang_code == 'pt':
        nav_items = [
            (d['base_url'], 'Início'),
            (d['servicos_url'], 'Serviços'),
            (d['sobre_anchor'], 'Sobre'),
            (d['faq_anchor'], 'FAQ'),
            (d['contato_anchor'], 'Contacto')
        ]
        footer_serv_links = [
            ('/pt/servicos/criacao-de-sites/', 'Criação de Websites'),
            ('/pt/servicos/seo/', 'SEO'),
            ('/pt/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/pt/servicos/sistemas/', 'Criação de Sistemas'),
            ('/pt/servicos/google-meu-negocio/', 'Google Perfil de Empresa')
        ]
    elif lang_code == 'br':
        nav_items = [
            (d['base_url'], 'Início'),
            (d['servicos_url'], 'Serviços'),
            (d['sobre_anchor'], 'Sobre'),
            (d['faq_anchor'], 'FAQ'),
            (d['contato_anchor'], 'Contato')
        ]
        footer_serv_links = [
            ('/br/servicos/criacao-de-sites/', 'Criação de Sites'),
            ('/br/servicos/seo/', 'SEO'),
            ('/br/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/br/servicos/sistemas/', 'Desenvolvimento de Sistemas'),
            ('/br/servicos/google-meu-negocio/', 'Google Meu Negócio')
        ]
    else:
        nav_items = [
            (d['base_url'], 'Home'),
            (d['servicos_url'], 'Servizi'),
            (d['sobre_anchor'], 'Chi Siamo'),
            (d['faq_anchor'], 'FAQ'),
            (d['contato_anchor'], 'Contatti')
        ]
        footer_serv_links = [
            ('/it/servizi/creazione-siti-web/', 'Creazione Siti Web'),
            ('/it/servizi/seo/', 'SEO'),
            ('/it/servizi/traffico-a-pagamento/', 'Traffico a Pagamento'),
            ('/it/servizi/sistemi/', 'Sviluppo Sistemi Web'),
            ('/it/servizi/google-business-profile/', 'Google Business Profile')
        ]

    # JSON-LD
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": "https://dominio.com/#organization",
                "name": "Magnani UP®",
                "url": "https://dominio.com/",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://dominio.com/images/logo/logo.png",
                    "width": 113,
                    "height": 27
                },
                "description": d['footer_desc'],
                "sameAs": ["https://instagram.com", "https://linkedin.com"]
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": d['breadcrumb_home'],
                        "item": d['base_url']
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": d['breadcrumb_services'],
                        "item": canonical
                    }
                ]
            },
            {
                "@type": "CollectionPage",
                "@id": f"{canonical}#webpage",
                "url": canonical,
                "name": cfg['title'],
                "description": cfg['meta_desc'],
                "isPartOf": {
                    "@id": "https://dominio.com/#website"
                }
            }
        ]
    }
    schema_json = json.dumps(schema, indent=2, ensure_ascii=False)

    # Cards HTML
    cards_html = ""
    for c in cfg['cards']:
        icon = SERVICE_ICONS.get(c['slug'], SERVICE_ICONS['seo'])
        cards_html += f'''
            <article class="service-card">
              <div class="service-card-content">
                <div class="service-icon-badge" aria-hidden="true">
                  {icon}
                </div>
                <h2 class="service-card-title">{c['title']}</h2>
                <p class="service-card-desc">{c['desc']}</p>
              </div>
              <a href="{c['link']}" class="service-card-btn" aria-label="{c['link_label']}">
                <svg class="service-btn-arrow" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                  <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5"/>
                </svg>
              </a>
            </article>'''

    nav_links_html = "".join([f'<li class="nav-item"><a href="{href}" class="nav-link {"active" if label in ["Serviços", "Servizi"] else ""}">{label}</a></li>\n' for href, label in nav_items])
    mobile_links_html = "".join([f'<li><a href="{href}" class="mobile-nav-link {"active" if label in ["Serviços", "Servizi"] else ""}">{label}</a></li>\n' for href, label in nav_items])

    footer_nav_links_html = "".join([f'<li><a href="{href}" class="footer-link">{label}</a></li>\n' for href, label in nav_items])
    footer_serv_links_html = "".join([f'<li><a href="{href}" class="footer-link">{label}</a></li>\n' for href, label in footer_serv_links])

    market_switch_html = f'''
          <a href="{pt_url}" class="market-btn {'current' if lang_code == 'pt' else ''}" aria-label="Português de Portugal">
            <span class="market-flag" aria-hidden="true">🇵🇹</span>
            <span class="market-label">PT</span>
          </a>
          <a href="{br_url}" class="market-btn {'current' if lang_code == 'br' else ''}" aria-label="Português do Brasil">
            <span class="market-flag" aria-hidden="true">🇧🇷</span>
            <span class="market-label">BR</span>
          </a>
          <a href="{it_url}" class="market-btn {'current' if lang_code == 'it' else ''}" aria-label="Italiano">
            <span class="market-flag" aria-hidden="true">🇮🇹</span>
            <span class="market-label">IT</span>
          </a>'''

    mobile_market_switch_html = f'''
          <a href="{pt_url}" class="mobile-market-link {'current' if lang_code == 'pt' else ''}">🇵🇹 PT</a>
          <a href="{br_url}" class="mobile-market-link {'current' if lang_code == 'br' else ''}">🇧🇷 BR</a>
          <a href="{it_url}" class="mobile-market-link {'current' if lang_code == 'it' else ''}">🇮🇹 IT</a>'''

    html = f'''<!DOCTYPE html>
<html lang="{d['lang']}" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-KDB6M7XW');</script>
  <!-- End Google Tag Manager -->
  <title>{cfg['title']}</title>
  
  <meta name="description" content="{cfg['meta_desc']}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{canonical}">
  
  <!-- Hreflang Rigoroso (pt-PT, pt-BR, it-IT, x-default) -->
  <link rel="alternate" hreflang="pt-PT" href="{pt_url}">
  <link rel="alternate" hreflang="pt-BR" href="{br_url}">
  <link rel="alternate" hreflang="it-IT" href="{it_url}">
  <link rel="alternate" hreflang="x-default" href="{pt_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{cfg['title']}">
  <meta property="og:description" content="{cfg['meta_desc']}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Magnani UP®">
  <meta property="og:locale" content="{d['locale']}">
  <meta property="og:image" content="https://dominio.com/images/og/og-magnani-up.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{cfg['h1']} - Magnani UP®">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{cfg['title']}">
  <meta name="twitter:description" content="{cfg['meta_desc']}">
  <meta name="twitter:image" content="https://dominio.com/images/og/og-magnani-up.png">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="../../images/logo/favicon.svg">

  <!-- Tipografia Oficial do Mockup (Google Fonts: Plus Jakarta Sans) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Estilos da Arquitetura -->
  <link rel="stylesheet" href="../../css/reset.css?v=20">
  <link rel="stylesheet" href="../../css/global.css?v=20">
  <link rel="stylesheet" href="../../css/header.css?v=20">
  <link rel="stylesheet" href="../../css/internal.css?v=20">
  <link rel="stylesheet" href="../../css/services.css?v=20">
  <link rel="stylesheet" href="../../css/process.css?v=20">
  <link rel="stylesheet" href="../../css/faq.css?v=20">
  <link rel="stylesheet" href="../../css/cta.css?v=20">
  <link rel="stylesheet" href="../../css/footer.css?v=20">
  <link rel="stylesheet" href="../../css/responsive.css?v=20">

  <!-- Dados Estruturados Schema.org -->
  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KDB6M7XW"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->
  <div class="page-wrapper">
    <!-- ====================================================================
         HEADER / MENU PRINCIPAL
         ==================================================================== -->
    <header class="site-header" id="site-header">
      <div class="header-container">
        
        <a href="{d['base_url']}" class="brand-logo" aria-label="Magnani UP® - {d['breadcrumb_home']}">
          <span class="brand-logo-content">
            <svg class="brand-symbol-svg" viewBox="0 0 56 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
              <defs>
                <linearGradient id="{lang_code}-hub-mGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#7045f5"/>
                  <stop offset="50%" stop-color="#8b5cf6"/>
                  <stop offset="100%" stop-color="#a78bfa"/>
                </linearGradient>
                <linearGradient id="{lang_code}-hub-upGrad" x1="0%" y1="100%" x2="0%" y2="0%">
                  <stop offset="0%" stop-color="#ffffff"/>
                  <stop offset="70%" stop-color="#ffffff"/>
                  <stop offset="100%" stop-color="#ede9fe"/>
                </linearGradient>
              </defs>
              <path d="M 4 29 L 10.8 9.5 C 11.8 6.8 14.8 6.8 15.8 9.5 L 20 18.5 C 21 20.8 23.8 20.8 24.8 18.5 L 29 9.5 C 30 6.8 33 6.8 34 9.5 L 38.5 20 C 39.2 21.8 41.5 22 42.5 20.5 L 46 14.5" 
                    stroke="url(#{lang_code}-hub-mGrad)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M 33.5 17.5 L 36.8 28.5 C 37.8 31.8 41.8 31.8 42.8 28.5 L 51.5 5.5 C 52 4.2 50.8 3.2 49.2 3.2 L 44 3.2 C 42.2 3.2 41 4.5 40.2 6.2 L 38 11" 
                    stroke="url(#{lang_code}-hub-upGrad)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="brand-name">
              <span class="brand-name-main">Magnani</span>
              <span class="brand-name-up">UP</span>
              <sup class="brand-registered">®</sup>
            </span>
          </span>
        </a>

        <nav class="site-nav" id="main-nav" aria-label="Navegação principal">
          <ul class="nav-list">
            {nav_links_html}
          </ul>
        </nav>

        <div class="header-actions">
          <div class="header-market-switch" aria-label="Mercado e Idioma">
            {market_switch_html}
          </div>

          <a href="{d['wa_link']}" target="_blank" rel="noopener noreferrer" class="btn-cta">
            <span>{d['cta_talk']}</span>
            <svg class="cta-arrow" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
              <path d="M6 3.5L10.5 8L6 12.5"/>
            </svg>
          </a>

          <button type="button" 
                  class="hamburger-btn" 
                  id="hamburger-toggle" 
                  aria-expanded="false" 
                  aria-controls="mobile-drawer" 
                  aria-label="Menu">
            <span class="hamburger-box">
              <span class="hamburger-line"></span>
              <span class="hamburger-line"></span>
              <span class="hamburger-line"></span>
            </span>
          </button>
        </div>

      </div>
    </header>

    <div class="mobile-overlay" id="mobile-overlay" aria-hidden="true"></div>

    <div class="mobile-drawer" id="mobile-drawer" role="dialog" aria-modal="true" aria-label="Navegação móvel">
      <nav class="mobile-nav" aria-label="Navegação móvel">
        <ul class="mobile-nav-list">
          {mobile_links_html}
        </ul>
      </nav>

      <div class="mobile-drawer-cta">
        <div class="mobile-market-switch" aria-label="Mercado / Lingua">
          {mobile_market_switch_html}
        </div>

        <a href="{d['wa_link']}" target="_blank" rel="noopener noreferrer" class="btn-cta">
          <span>{d['cta_talk']}</span>
          <svg class="cta-arrow" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
            <path d="M6 3.5L10.5 8L6 12.5"/>
          </svg>
        </a>
      </div>
    </div>

    <!-- Conteúdo Principal -->
    <main class="main-content-stage" id="conteudo-principal">

      <!-- Breadcrumbs -->
      <section class="breadcrumb-section" aria-label="Breadcrumb">
        <div class="breadcrumb-container">
          <nav class="breadcrumb-nav" aria-label="Caminho de navegação">
            <ol class="breadcrumb-list">
              <li class="breadcrumb-item">
                <a href="{d['base_url']}" class="breadcrumb-link">{d['breadcrumb_home']}</a>
                <span class="breadcrumb-separator" aria-hidden="true">/</span>
              </li>
              <li class="breadcrumb-item breadcrumb-current" aria-current="page">
                {d['breadcrumb_services']}
              </li>
            </ol>
          </nav>
        </div>
      </section>

      <!-- Hero Interno -->
      <section class="internal-hero-section" aria-labelledby="hub-h1">
        <div class="internal-hero-container">
          <div class="internal-hero-kicker">
            <span class="internal-kicker-line" aria-hidden="true"></span>
            <span class="internal-kicker-text">{cfg['tag']}</span>
          </div>

          <h1 class="internal-hero-title" id="hub-h1">
            {cfg['h1']}
          </h1>

          <p class="internal-hero-desc">
            {cfg['hero_desc']}
          </p>

          <div class="internal-hero-actions">
            <a href="{d['wa_link']}" target="_blank" rel="noopener noreferrer" class="btn-cta">
              <span>{d['cta_talk']}</span>
              <svg class="cta-arrow" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                <path d="M6 3.5L10.5 8L6 12.5"/>
              </svg>
            </a>
          </div>
        </div>
      </section>

      <!-- Grid dos Serviços -->
      <section class="services-section" id="servicos" aria-labelledby="hub-h1">
        <div class="services-container">
          <div class="services-cards-grid">
            {cards_html}
          </div>
        </div>
      </section>

      <!-- CTA Banner -->
      <section class="cta-section" id="contato" aria-labelledby="cta-hub-title">
        <div class="cta-container">
          <div class="cta-banner">
            <svg class="cta-bg-art" viewBox="0 0 1200 240" preserveAspectRatio="none" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
              <defs>
                <linearGradient id="{lang_code}-hub-ctaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#141a45" stop-opacity="0.95"/>
                  <stop offset="50%" stop-color="#0e1338" stop-opacity="0.98"/>
                  <stop offset="100%" stop-color="#080c25" stop-opacity="1"/>
                </linearGradient>
                <linearGradient id="{lang_code}-hub-stripeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#7045f5" stop-opacity="0.35"/>
                  <stop offset="50%" stop-color="#8b5cf6" stop-opacity="0.2"/>
                  <stop offset="100%" stop-color="#f5711a" stop-opacity="0.35"/>
                </linearGradient>
              </defs>
              <rect width="1200" height="240" rx="20" fill="url(#{lang_code}-hub-ctaGrad)"/>
              <path d="M 680 -20 L 820 260 L 760 260 L 620 -20 Z" fill="url(#{lang_code}-hub-stripeGrad)"/>
              <path d="M 780 -20 L 920 260 L 880 260 L 740 -20 Z" fill="url(#{lang_code}-hub-stripeGrad)" opacity="0.6"/>
            </svg>

            <div class="cta-content-wrapper">
              <div class="cta-text-col">
                <h2 class="cta-title" id="cta-hub-title">
                  {d['cta_banner_title']}
                </h2>
                <p class="cta-desc">
                  {d['cta_banner_desc']}
                </p>
              </div>

              <div class="cta-action-col">
                <a href="{d['wa_link']}" target="_blank" rel="noopener noreferrer" class="cta-btn">
                  <span>{d['cta_banner_btn']}</span>
                  <svg class="cta-btn-arrow" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                    <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5"/>
                  </svg>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

    </main>

    <!-- Footer -->
    <footer class="site-footer" id="site-footer" aria-label="Rodapé do site">
      <div class="footer-container">
        <div class="footer-main-grid">
          
          <div class="footer-brand-col">
            <a href="{d['base_url']}" class="brand-logo footer-brand-logo" aria-label="Magnani UP®">
              <span class="brand-logo-content">
                <svg class="brand-symbol-svg" viewBox="0 0 56 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
                  <defs>
                    <linearGradient id="{lang_code}-hubfoot-mGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                      <stop offset="0%" stop-color="#7045f5"/>
                      <stop offset="50%" stop-color="#8b5cf6"/>
                      <stop offset="100%" stop-color="#a78bfa"/>
                    </linearGradient>
                    <linearGradient id="{lang_code}-hubfoot-upGrad" x1="0%" y1="100%" x2="0%" y2="0%">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="70%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#ede9fe"/>
                    </linearGradient>
                  </defs>
                  <path d="M 4 29 L 10.8 9.5 C 11.8 6.8 14.8 6.8 15.8 9.5 L 20 18.5 C 21 20.8 23.8 20.8 24.8 18.5 L 29 9.5 C 30 6.8 33 6.8 34 9.5 L 38.5 20 C 39.2 21.8 41.5 22 42.5 20.5 L 46 14.5" 
                        stroke="url(#{lang_code}-hubfoot-mGrad)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M 33.5 17.5 L 36.8 28.5 C 37.8 31.8 41.8 31.8 42.8 28.5 L 51.5 5.5 C 52 4.2 50.8 3.2 49.2 3.2 L 44 3.2 C 42.2 3.2 41 4.5 40.2 6.2 L 38 11" 
                        stroke="url(#{lang_code}-hubfoot-upGrad)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span class="brand-name">
                  <span class="brand-name-main">Magnani</span>
                  <span class="brand-name-up">UP</span>
                  <sup class="brand-registered">®</sup>
                </span>
              </span>
            </a>

            <span class="footer-tagline">{d['footer_tagline']}</span>
            <p class="footer-institutional-desc">{d['footer_desc']}</p>

            <ul class="footer-social-list" aria-label="Redes sociais">
              <li>
                <a href="https://instagram.com" class="footer-social-link" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
                  <svg class="footer-social-svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                    <rect x="2" y="2" width="20" height="20" rx="5" ry="5" fill="none" stroke="currentColor" stroke-width="2"/>
                    <circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/>
                    <circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/>
                  </svg>
                </a>
              </li>
              <li>
                <a href="https://linkedin.com" class="footer-social-link" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                  <svg class="footer-social-svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                    <rect x="2" y="2" width="20" height="20" rx="4" fill="none" stroke="currentColor" stroke-width="2"/>
                    <circle cx="7" cy="7" r="1.8" fill="currentColor"/>
                    <path d="M5.5 10.5H8.5V18.5H5.5V10.5Z" fill="currentColor"/>
                    <path d="M11 10.5H13.8V11.7C14.3 10.8 15.4 10.2 16.7 10.2C19.5 10.2 20 12 20 14.5V18.5H17V14.8C17 13.5 16.6 12.6 15.3 12.6C14 12.6 13.5 13.5 13.5 14.8V18.5H11V10.5Z" fill="currentColor"/>
                  </svg>
                </a>
              </li>
              <li>
                <a href="{d['base_url']}" class="footer-social-link" aria-label="Website">
                  <svg class="footer-social-svg" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                    <circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/>
                    <line x1="3" y1="12" x2="21" y2="12" stroke="currentColor" stroke-width="2"/>
                    <path d="M12 3C14.5 5.5 16 8.5 16 12C16 15.5 14.5 18.5 12 21C9.5 18.5 8 15.5 8 12C8 8.5 9.5 5.5 12 3Z" fill="none" stroke="currentColor" stroke-width="2"/>
                  </svg>
                </a>
              </li>
            </ul>
          </div>

          <nav class="footer-col" aria-label="{d['footer_nav_title']}">
            <h3 class="footer-col-title">{d['footer_nav_title']}</h3>
            <ul class="footer-links-list">
              {footer_nav_links_html}
            </ul>
          </nav>

          <nav class="footer-col" aria-label="{d['footer_serv_title']}">
            <h3 class="footer-col-title">{d['footer_serv_title']}</h3>
            <ul class="footer-links-list">
              {footer_serv_links_html}
            </ul>
          </nav>

          <div class="footer-col footer-contact-col">
            <h3 class="footer-col-title">{d['footer_contact_title']}</h3>
            <p class="footer-contact-text">
              {d['footer_contact_desc']}
            </p>
            <a href="{d['wa_link']}" target="_blank" rel="noopener noreferrer" class="footer-contact-btn">
              <span>{d['cta_banner_btn']} &rarr;</span>
            </a>
          </div>

        </div>

        <div class="footer-bottom-bar">
          <p class="footer-copyright">{d['footer_rights']}</p>
          <div class="footer-legal-links">
            <a href="{d['base_url']}privacidade/" class="footer-legal-link">{d['footer_privacy']}</a>
            <span class="footer-legal-divider" aria-hidden="true"></span>
            <a href="{d['base_url']}termos/" class="footer-legal-link">{d['footer_terms']}</a>
          </div>
        </div>

      </div>
    </footer>

  </div>

  <script src="../../js/navigation.js?v=20"></script>
  <script src="../../js/main.js?v=20"></script>
</body>
</html>'''
    return html

def main():
    for lang in ['pt', 'br', 'it']:
        content = render_hub(lang)
        path = HUB_CONFIG[lang]['path']
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated hub {path}")

if __name__ == '__main__':
    main()
