import os
import json
from scratch_services_data import DATA

SERVICE_KEYS = [
    ('criacao-de-sites', 'criacao-de-sites', 'creazione-siti-web'),
    ('seo', 'seo', 'seo'),
    ('landing-pages', 'landing-pages', 'landing-page'),
    ('trafego-pago', 'trafego-pago', 'traffico-a-pagamento'),
    ('sistemas', 'sistemas', 'sistemi'),
    ('google-meu-negocio', 'google-meu-negocio', 'google-business-profile')
]

SERVICE_ICONS = {
    'criacao-de-sites': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <rect x="3.5" y="4.5" width="21" height="18" rx="3" stroke="#ffffff" stroke-width="1.8"/>
      <line x1="3.5" y1="9.5" x2="24.5" y2="9.5" stroke="#a78bfa" stroke-width="1.6"/>
      <rect x="13.5" y="12.5" width="8" height="7.5" rx="1.5" fill="#1e295d" stroke="#f5711a" stroke-width="1.6"/>
      <line x1="6.5" y1="13.5" x2="10.5" y2="13.5" stroke="#a78bfa" stroke-width="1.6" stroke-linecap="round"/>
      <line x1="6.5" y1="17" x2="10.5" y2="17" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round" opacity="0.8"/>
    </svg>''',
    'creazione-siti-web': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <rect x="3.5" y="4.5" width="21" height="18" rx="3" stroke="#ffffff" stroke-width="1.8"/>
      <line x1="3.5" y1="9.5" x2="24.5" y2="9.5" stroke="#a78bfa" stroke-width="1.6"/>
      <rect x="13.5" y="12.5" width="8" height="7.5" rx="1.5" fill="#1e295d" stroke="#f5711a" stroke-width="1.6"/>
      <line x1="6.5" y1="13.5" x2="10.5" y2="13.5" stroke="#a78bfa" stroke-width="1.6" stroke-linecap="round"/>
      <line x1="6.5" y1="17" x2="10.5" y2="17" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round" opacity="0.8"/>
    </svg>''',
    'seo': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <circle cx="12" cy="12" r="7" stroke="#a78bfa" stroke-width="2.2"/>
      <path d="M17 17L23.5 23.5" stroke="#f5711a" stroke-width="2.4" stroke-linecap="round"/>
    </svg>''',
    'landing-pages': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <rect x="3.5" y="4.5" width="21" height="18" rx="3" stroke="#ffffff" stroke-width="1.8"/>
      <line x1="3.5" y1="9.5" x2="24.5" y2="9.5" stroke="#a78bfa" stroke-width="1.6"/>
      <rect x="13.5" y="12.5" width="8" height="7.5" rx="1.5" fill="#1e295d" stroke="#f5711a" stroke-width="1.6"/>
      <line x1="6.5" y1="13.5" x2="10.5" y2="13.5" stroke="#a78bfa" stroke-width="1.6" stroke-linecap="round"/>
      <line x1="6.5" y1="17" x2="10.5" y2="17" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round" opacity="0.8"/>
    </svg>''',
    'landing-page': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <rect x="3.5" y="4.5" width="21" height="18" rx="3" stroke="#ffffff" stroke-width="1.8"/>
      <line x1="3.5" y1="9.5" x2="24.5" y2="9.5" stroke="#a78bfa" stroke-width="1.6"/>
      <rect x="13.5" y="12.5" width="8" height="7.5" rx="1.5" fill="#1e295d" stroke="#f5711a" stroke-width="1.6"/>
      <line x1="6.5" y1="13.5" x2="10.5" y2="13.5" stroke="#a78bfa" stroke-width="1.6" stroke-linecap="round"/>
      <line x1="6.5" y1="17" x2="10.5" y2="17" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round" opacity="0.8"/>
    </svg>''',
    'trafego-pago': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <path d="M5 12V16H8L14 20V8L8 12H5Z" stroke="#f5711a" stroke-width="2" stroke-linejoin="round"/>
      <path d="M7 16L8.5 21H11L9.8 16" stroke="#f5711a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M17.5 10C18.8 11.2 19.5 12.8 19.5 14C19.5 15.2 18.8 16.8 17.5 18" stroke="#a78bfa" stroke-width="2" stroke-linecap="round"/>
      <path d="M20.5 7C22.8 9 24 11.5 24 14C24 16.5 22.8 19 20.5 21" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>
    </svg>''',
    'traffico-a-pagamento': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <path d="M5 12V16H8L14 20V8L8 12H5Z" stroke="#f5711a" stroke-width="2" stroke-linejoin="round"/>
      <path d="M7 16L8.5 21H11L9.8 16" stroke="#f5711a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M17.5 10C18.8 11.2 19.5 12.8 19.5 14C19.5 15.2 18.8 16.8 17.5 18" stroke="#a78bfa" stroke-width="2" stroke-linecap="round"/>
      <path d="M20.5 7C22.8 9 24 11.5 24 14C24 16.5 22.8 19 20.5 21" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>
    </svg>''',
    'sistemas': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <path d="M8.5 9L3.5 14L8.5 19" stroke="#a78bfa" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M19.5 9L24.5 14L19.5 19" stroke="#a78bfa" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M16 6.5L12 21.5" stroke="#f5711a" stroke-width="2.2" stroke-linecap="round"/>
    </svg>''',
    'sistemi': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <path d="M8.5 9L3.5 14L8.5 19" stroke="#a78bfa" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M19.5 9L24.5 14L19.5 19" stroke="#a78bfa" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M16 6.5L12 21.5" stroke="#f5711a" stroke-width="2.2" stroke-linecap="round"/>
    </svg>''',
    'google-meu-negocio': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <path d="M4 7H24L22 13H6L4 7Z" stroke="#a78bfa" stroke-width="2" stroke-linejoin="round" fill="#1c2156"/>
      <path d="M10 7V13" stroke="#a78bfa" stroke-width="1.5"/>
      <path d="M14 7V13" stroke="#a78bfa" stroke-width="1.5"/>
      <path d="M18 7V13" stroke="#a78bfa" stroke-width="1.5"/>
      <path d="M6 13V22H22V13" stroke="#f5711a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      <rect x="11.5" y="16" width="5" height="6" stroke="#ffffff" stroke-width="1.6" fill="none"/>
    </svg>''',
    'google-business-profile': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
      <path d="M4 7H24L22 13H6L4 7Z" stroke="#a78bfa" stroke-width="2" stroke-linejoin="round" fill="#1c2156"/>
      <path d="M10 7V13" stroke="#a78bfa" stroke-width="1.5"/>
      <path d="M14 7V13" stroke="#a78bfa" stroke-width="1.5"/>
      <path d="M18 7V13" stroke="#a78bfa" stroke-width="1.5"/>
      <path d="M6 13V22H22V13" stroke="#f5711a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      <rect x="11.5" y="16" width="5" height="6" stroke="#ffffff" stroke-width="1.6" fill="none"/>
    </svg>'''
}

def render_page(lang_code, s_info, pt_slug, br_slug, it_slug):
    d = DATA[lang_code]
    slug = s_info['slug']
    
    # Hreflang URLs
    pt_url = f"https://dominio.com/pt/servicos/{pt_slug}/"
    br_url = f"https://dominio.com/br/servicos/{br_slug}/"
    it_url = f"https://dominio.com/it/servizi/{it_slug}/"
    current_canonical = pt_url if lang_code == 'pt' else (br_url if lang_code == 'br' else it_url)
    
    # Navigation labels
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

    # JSON-LD Schema
    schema_graph = [
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
            "@id": f"{current_canonical}#breadcrumb",
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
                    "item": d['servicos_url']
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": s_info['h1'],
                    "item": current_canonical
                }
            ]
        },
        {
            "@type": "Service",
            "@id": f"{current_canonical}#service",
            "name": s_info['h1'],
            "description": s_info['meta_desc'],
            "url": current_canonical,
            "provider": {
                "@id": "https://dominio.com/#organization"
            },
            "areaServed": [d['locale'].split('_')[1]]
        },
        {
            "@type": "FAQPage",
            "@id": f"{current_canonical}#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item['q'],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": item['a']
                    }
                } for item in s_info['faqs']
            ]
        }
    ]

    schema_json = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, indent=2, ensure_ascii=False)

    # Render Benefits HTML
    benefits_html = ""
    for b in s_info['benefits']:
        benefits_html += f'''
            <article class="detail-card">
              <div class="detail-card-icon" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                  <polyline points="22 4 12 14.01 9 11.01"/>
                </svg>
              </div>
              <h3 class="detail-card-title">{b['title']}</h3>
              <p class="detail-card-desc">{b['desc']}</p>
            </article>'''

    # Render Process Steps HTML
    steps_html = ""
    for i, step in enumerate(s_info['steps']):
        steps_html += f'''
            <li class="process-step-item">
              <div class="process-icon-badge" aria-hidden="true">
                <span class="faq-num-badge">{step['num']}</span>
              </div>
              <h3 class="process-step-title">{step['title']}</h3>
              <p class="process-step-desc">{step['desc']}</p>
            </li>'''
        if i < len(s_info['steps']) - 1:
            steps_html += '''
            <li class="process-flow-connector" aria-hidden="true">
              <svg class="process-arrow-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                <path d="M6 3.5L10.5 8L6 12.5"/>
              </svg>
            </li>'''

    # Render FAQ HTML
    faq_html = ""
    for i, f in enumerate(s_info['faqs']):
        idx = i + 1
        faq_html += f'''
            <div class="faq-item">
              <button type="button" 
                      class="faq-question-btn" 
                      id="service-faq-btn-{idx}" 
                      aria-expanded="false" 
                      aria-controls="service-faq-ans-{idx}">
                <span class="faq-question-left">
                  <span class="faq-num-badge" aria-hidden="true">0{idx}</span>
                  <span class="faq-question-text">{f['q']}</span>
                </span>
                <svg class="faq-chevron-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                  <path d="M3.5 6L8 10.5L12.5 6"/>
                </svg>
              </button>
              <div class="faq-answer-panel" id="service-faq-ans-{idx}" role="region" aria-labelledby="service-faq-btn-{idx}">
                <div class="faq-answer-inner">
                  <div class="faq-answer-content">
                    <p class="faq-answer-text">{f['a']}</p>
                  </div>
                </div>
              </div>
            </div>'''

    # Nav links HTML
    nav_links_html = "".join([f'<li class="nav-item"><a href="{href}" class="nav-link">{label}</a></li>\n' for href, label in nav_items])
    mobile_links_html = "".join([f'<li><a href="{href}" class="mobile-nav-link">{label}</a></li>\n' for href, label in nav_items])

    # Footer links HTML
    footer_nav_links_html = "".join([f'<li><a href="{href}" class="footer-link">{label}</a></li>\n' for href, label in nav_items])
    footer_serv_links_html = "".join([f'<li><a href="{href}" class="footer-link">{label}</a></li>\n' for href, label in footer_serv_links])

    # Market selector links
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

    # Service Icon SVG
    service_icon = SERVICE_ICONS.get(slug, SERVICE_ICONS['seo'])

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
  <title>{s_info['title']}</title>
  
  <meta name="description" content="{s_info['meta_desc']}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{current_canonical}">
  
  <!-- Hreflang Rigoroso (pt-PT, pt-BR, it-IT, x-default) -->
  <link rel="alternate" hreflang="pt-PT" href="{pt_url}">
  <link rel="alternate" hreflang="pt-BR" href="{br_url}">
  <link rel="alternate" hreflang="it-IT" href="{it_url}">
  <link rel="alternate" hreflang="x-default" href="{pt_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{s_info['title']}">
  <meta property="og:description" content="{s_info['meta_desc']}">
  <meta property="og:url" content="{current_canonical}">
  <meta property="og:site_name" content="Magnani UP®">
  <meta property="og:locale" content="{d['locale']}">
  <meta property="og:image" content="https://dominio.com/images/og/og-magnani-up.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{s_info['h1']} - Magnani UP®">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{s_info['title']}">
  <meta name="twitter:description" content="{s_info['meta_desc']}">
  <meta name="twitter:image" content="https://dominio.com/images/og/og-magnani-up.png">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="../../../images/logo/favicon.svg">

  <!-- Tipografia Oficial do Mockup (Google Fonts: Plus Jakarta Sans) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Estilos da Arquitetura -->
  <link rel="stylesheet" href="../../../css/reset.css?v=20">
  <link rel="stylesheet" href="../../../css/global.css?v=20">
  <link rel="stylesheet" href="../../../css/header.css?v=20">
  <link rel="stylesheet" href="../../../css/internal.css?v=20">
  <link rel="stylesheet" href="../../../css/services.css?v=20">
  <link rel="stylesheet" href="../../../css/process.css?v=20">
  <link rel="stylesheet" href="../../../css/faq.css?v=20">
  <link rel="stylesheet" href="../../../css/cta.css?v=20">
  <link rel="stylesheet" href="../../../css/footer.css?v=20">
  <link rel="stylesheet" href="../../../css/responsive.css?v=20">

  <!-- Dados Estruturados Schema.org (BreadcrumbList, Service, FAQPage) -->
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
         HEADER / MENU PRINCIPAL (Fidelidade Absoluta ao Mockup Magnani UP®)
         ==================================================================== -->
    <header class="site-header" id="site-header">
      <div class="header-container">
        
        <!-- Lado Esquerdo: Logo Magnani UP® -->
        <a href="{d['base_url']}" class="brand-logo" aria-label="Magnani UP® - {d['breadcrumb_home']}">
          <span class="brand-logo-content">
            <svg class="brand-symbol-svg" viewBox="0 0 56 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
              <defs>
                <linearGradient id="{lang_code}-mGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#7045f5"/>
                  <stop offset="50%" stop-color="#8b5cf6"/>
                  <stop offset="100%" stop-color="#a78bfa"/>
                </linearGradient>
                <linearGradient id="{lang_code}-upGrad" x1="0%" y1="100%" x2="0%" y2="0%">
                  <stop offset="0%" stop-color="#ffffff"/>
                  <stop offset="70%" stop-color="#ffffff"/>
                  <stop offset="100%" stop-color="#ede9fe"/>
                </linearGradient>
              </defs>
              <path d="M 4 29 L 10.8 9.5 C 11.8 6.8 14.8 6.8 15.8 9.5 L 20 18.5 C 21 20.8 23.8 20.8 24.8 18.5 L 29 9.5 C 30 6.8 33 6.8 34 9.5 L 38.5 20 C 39.2 21.8 41.5 22 42.5 20.5 L 46 14.5" 
                    stroke="url(#{lang_code}-mGrad)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M 33.5 17.5 L 36.8 28.5 C 37.8 31.8 41.8 31.8 42.8 28.5 L 51.5 5.5 C 52 4.2 50.8 3.2 49.2 3.2 L 44 3.2 C 42.2 3.2 41 4.5 40.2 6.2 L 38 11" 
                    stroke="url(#{lang_code}-upGrad)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span class="brand-name">
              <span class="brand-name-main">Magnani</span>
              <span class="brand-name-up">UP</span>
              <sup class="brand-registered">®</sup>
            </span>
          </span>
        </a>

        <!-- Centro: Menu de Navegação Desktop -->
        <nav class="site-nav" id="main-nav" aria-label="Navegação principal">
          <ul class="nav-list">
            {nav_links_html}
          </ul>
        </nav>

        <!-- Lado Direito: Seletor de Idiomas, Botão de Conversão & Toggle Mobile -->
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

          <!-- Botão Hamburger Mobile (Acessível) -->
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

    <!-- Overlay e Gaveta de Navegação Mobile -->
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

    <!-- Conteúdo Principal Semântico -->
    <main class="main-content-stage" id="conteudo-principal">

      <!-- Breadcrumbs Acessíveis -->
      <section class="breadcrumb-section" aria-label="Breadcrumb">
        <div class="breadcrumb-container">
          <nav class="breadcrumb-nav" aria-label="Caminho de navegação">
            <ol class="breadcrumb-list">
              <li class="breadcrumb-item">
                <a href="{d['base_url']}" class="breadcrumb-link">{d['breadcrumb_home']}</a>
                <span class="breadcrumb-separator" aria-hidden="true">/</span>
              </li>
              <li class="breadcrumb-item">
                <a href="{d['servicos_url']}" class="breadcrumb-link">{d['breadcrumb_services']}</a>
                <span class="breadcrumb-separator" aria-hidden="true">/</span>
              </li>
              <li class="breadcrumb-item breadcrumb-current" aria-current="page">
                {s_info['h1']}
              </li>
            </ol>
          </nav>
        </div>
      </section>

      <!-- Hero Interno Especializado -->
      <section class="internal-hero-section" aria-labelledby="service-h1">
        <div class="internal-hero-container">
          <div class="internal-hero-kicker">
            <span class="internal-kicker-line" aria-hidden="true"></span>
            <span class="internal-kicker-text">{d['kicker_text']}</span>
          </div>

          <h1 class="internal-hero-title" id="service-h1">
            {s_info['h1'].split('|')[0].strip()}
          </h1>

          <p class="internal-hero-desc">
            {s_info['hero_desc']}
          </p>

          <div class="internal-hero-actions">
            <a href="{d['wa_link']}" target="_blank" rel="noopener noreferrer" class="btn-cta">
              <span>{d['cta_talk']}</span>
              <svg class="cta-arrow" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                <path d="M6 3.5L10.5 8L6 12.5"/>
              </svg>
            </a>
            <a href="#beneficios" class="hero-btn-secondary">
              <span>{s_info['benefits_title']}</span>
              <svg class="hero-btn-arrow-secondary" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                <path d="M6 3.5L10.5 8L6 12.5"/>
              </svg>
            </a>
          </div>
        </div>
      </section>

      <!-- Seção Benefícios e Problemas Resolvidos -->
      <section class="detail-section" id="beneficios" aria-labelledby="benefits-title">
        <div class="detail-container">
          <div class="detail-header">
            <div class="detail-header-left">
              <div class="detail-tag">
                <span class="detail-tag-line" aria-hidden="true"></span>
                <span class="detail-tag-text">{s_info['benefits_tag']}</span>
              </div>
              <h2 class="detail-section-title" id="benefits-title">
                {s_info['benefits_title']}
              </h2>
              <p class="detail-section-desc">
                {s_info['tagline']}
              </p>
            </div>
          </div>

          <div class="detail-grid-3">
            {benefits_html}
          </div>
        </div>
      </section>

      <!-- Metodologia / Como Trabalhamos -->
      <section class="process-section" id="metodologia" aria-labelledby="process-title">
        <div class="process-container">
          <div class="process-header-row">
            <div class="process-header-left">
              <div class="process-tag">
                <span class="process-tag-line" aria-hidden="true"></span>
                <span class="process-tag-text">{d['kicker_text']}</span>
              </div>
              <h2 class="process-title" id="process-title">
                {d['methodology_title']}
              </h2>
            </div>
            <div class="process-header-right">
              <p class="process-intro-text">
                {d['methodology_subtitle']}
              </p>
            </div>
          </div>

          <ol class="process-flow-list">
            {steps_html}
          </ol>
        </div>
      </section>

      <!-- FAQ Específico do Serviço -->
      <section class="faq-section" id="faq" aria-labelledby="service-faq-title">
        <div class="faq-container">
          <div class="faq-header">
            <div class="faq-tag">
              <span class="faq-tag-line" aria-hidden="true"></span>
              <span class="faq-tag-text">{d['faq_tag']}</span>
            </div>
            <h2 class="faq-title" id="service-faq-title">
              {d['faq_title']}
            </h2>
          </div>

          <div class="faq-accordion-list" role="region" aria-label="{d['faq_title']}">
            {faq_html}
          </div>
        </div>
      </section>

      <!-- Seção CTA Oficial com Arte Magnani UP® -->
      <section class="cta-section" id="contato" aria-labelledby="cta-banner-title">
        <div class="cta-container">
          <div class="cta-banner">
            
            <svg class="cta-bg-art" viewBox="0 0 1200 240" preserveAspectRatio="none" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
              <defs>
                <linearGradient id="{lang_code}-{slug}-ctaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#141a45" stop-opacity="0.95"/>
                  <stop offset="50%" stop-color="#0e1338" stop-opacity="0.98"/>
                  <stop offset="100%" stop-color="#080c25" stop-opacity="1"/>
                </linearGradient>
                <linearGradient id="{lang_code}-{slug}-stripeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#7045f5" stop-opacity="0.35"/>
                  <stop offset="50%" stop-color="#8b5cf6" stop-opacity="0.2"/>
                  <stop offset="100%" stop-color="#f5711a" stop-opacity="0.35"/>
                </linearGradient>
              </defs>
              <rect width="1200" height="240" rx="20" fill="url(#{lang_code}-{slug}-ctaGrad)"/>
              <path d="M 680 -20 L 820 260 L 760 260 L 620 -20 Z" fill="url(#{lang_code}-{slug}-stripeGrad)"/>
              <path d="M 780 -20 L 920 260 L 880 260 L 740 -20 Z" fill="url(#{lang_code}-{slug}-stripeGrad)" opacity="0.6"/>
            </svg>

            <div class="cta-content-wrapper">
              <div class="cta-text-col">
                <h2 class="cta-title" id="cta-banner-title">
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

    <!-- ====================================================================
         FOOTER / RODAPÉ OFICIAL (Fidelidade Absoluta ao Mockup Magnani UP®)
         ==================================================================== -->
    <footer class="site-footer" id="site-footer" aria-label="Rodapé do site">
      <div class="footer-container">
        
        <div class="footer-main-grid">
          
          <!-- Coluna 1 — Marca -->
          <div class="footer-brand-col">
            <a href="{d['base_url']}" class="brand-logo footer-brand-logo" aria-label="Magnani UP®">
              <span class="brand-logo-content">
                <svg class="brand-symbol-svg" viewBox="0 0 56 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
                  <defs>
                    <linearGradient id="{lang_code}-foot-mGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                      <stop offset="0%" stop-color="#7045f5"/>
                      <stop offset="50%" stop-color="#8b5cf6"/>
                      <stop offset="100%" stop-color="#a78bfa"/>
                    </linearGradient>
                    <linearGradient id="{lang_code}-foot-upGrad" x1="0%" y1="100%" x2="0%" y2="0%">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="70%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#ede9fe"/>
                    </linearGradient>
                  </defs>
                  <path d="M 4 29 L 10.8 9.5 C 11.8 6.8 14.8 6.8 15.8 9.5 L 20 18.5 C 21 20.8 23.8 20.8 24.8 18.5 L 29 9.5 C 30 6.8 33 6.8 34 9.5 L 38.5 20 C 39.2 21.8 41.5 22 42.5 20.5 L 46 14.5" 
                        stroke="url(#{lang_code}-foot-mGrad)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M 33.5 17.5 L 36.8 28.5 C 37.8 31.8 41.8 31.8 42.8 28.5 L 51.5 5.5 C 52 4.2 50.8 3.2 49.2 3.2 L 44 3.2 C 42.2 3.2 41 4.5 40.2 6.2 L 38 11" 
                        stroke="url(#{lang_code}-foot-upGrad)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span class="brand-name">
                  <span class="brand-name-main">Magnani</span>
                  <span class="brand-name-up">UP</span>
                  <sup class="brand-registered">®</sup>
                </span>
              </span>
            </a>

            <span class="footer-tagline">{d['footer_tagline']}</span>

            <p class="footer-institutional-desc">
              {d['footer_desc']}
            </p>

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

          <!-- Coluna 2 — Navegação -->
          <nav class="footer-col" aria-label="{d['footer_nav_title']}">
            <h3 class="footer-col-title">{d['footer_nav_title']}</h3>
            <ul class="footer-links-list">
              {footer_nav_links_html}
            </ul>
          </nav>

          <!-- Coluna 3 — Serviços -->
          <nav class="footer-col" aria-label="{d['footer_serv_title']}">
            <h3 class="footer-col-title">{d['footer_serv_title']}</h3>
            <ul class="footer-links-list">
              {footer_serv_links_html}
            </ul>
          </nav>

          <!-- Coluna 4 — Contacto -->
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

        <!-- Divisor Inferior & Barra Legal -->
        <div class="footer-bottom-bar">
          <p class="footer-copyright">
            {d['footer_rights']}
          </p>
          <div class="footer-legal-links">
            <a href="{d['base_url']}privacidade/" class="footer-legal-link">{d['footer_privacy']}</a>
            <span class="footer-legal-divider" aria-hidden="true"></span>
            <a href="{d['base_url']}termos/" class="footer-legal-link">{d['footer_terms']}</a>
          </div>
        </div>

      </div>
    </footer>

  </div>

  <script src="../../../js/navigation.js?v=20"></script>
  <script src="../../../js/faq.js?v=20"></script>
  <script src="../../../js/main.js?v=20"></script>
</body>
</html>'''
    return html

def main():
    generated_count = 0
    for pt_slug, br_slug, it_slug in SERVICE_KEYS:
        # PT
        pt_content = render_page('pt', DATA['pt']['services'][pt_slug], pt_slug, br_slug, it_slug)
        pt_file = f"pt/servicos/{pt_slug}/index.html"
        os.makedirs(os.path.dirname(pt_file), exist_ok=True)
        with open(pt_file, 'w', encoding='utf-8') as f:
            f.write(pt_content)
        generated_count += 1
        print(f"Generated {pt_file}")

        # BR
        br_content = render_page('br', DATA['br']['services'][br_slug], pt_slug, br_slug, it_slug)
        br_file = f"br/servicos/{br_slug}/index.html"
        os.makedirs(os.path.dirname(br_file), exist_ok=True)
        with open(br_file, 'w', encoding='utf-8') as f:
            f.write(br_content)
        generated_count += 1
        print(f"Generated {br_file}")

        # IT
        it_content = render_page('it', DATA['it']['services'][it_slug], pt_slug, br_slug, it_slug)
        it_file = f"it/servizi/{it_slug}/index.html"
        os.makedirs(os.path.dirname(it_file), exist_ok=True)
        with open(it_file, 'w', encoding='utf-8') as f:
            f.write(it_content)
        generated_count += 1
        print(f"Generated {it_file}")

    print(f"Total service pages generated: {generated_count}")

if __name__ == '__main__':
    main()
