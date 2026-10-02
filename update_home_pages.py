import re
import json

def update_home(file_path, backup_path, lang_code):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if lang_code == 'pt':
        title = "Criação de Sites e Soluções Digitais em Portugal | Magnani UP®"
        meta_desc = "Criação de websites profissionais, SEO, landing pages, tráfego pago e soluções digitais para empresas que pretendem fortalecer a sua presença online em Portugal."
        canonical = "https://dominio.com/pt/"
        og_locale = "pt_PT"
        og_alt = "Magnani UP® - Agência Digital e Criação de Websites em Portugal"
        hero_desc = "Criamos websites profissionais, modernos e de alta performance para empresas que pretendem fortalecer a sua presença digital, conquistar novos clientes e impulsionar resultados sustentáveis."
        
        b1_title = "Sites rápidos e otimizados"
        b1_desc = "para motores de busca (SEO)"
        b2_title = "Design 100% responsivo"
        b2_desc = "em todos os dispositivos"
        b3_title = "Suporte e acompanhamento"
        b3_desc = "em todas as etapas do projeto"
        
        wa_link = "https://wa.me/393313882760"
        
        service_links = [
            ('/pt/servicos/seo/', 'SEO'),
            ('/pt/servicos/landing-pages/', 'Landing Pages'),
            ('/pt/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/pt/servicos/sistemas/', 'Criação de Sistemas'),
            ('/pt/servicos/google-meu-negocio/', 'Google Perfil de Empresa')
        ]
        
        s1_desc = "Otimização técnica e estratégica para posicionar o seu website nas pesquisas do Google, atraindo tráfego orgânico qualificado para a sua empresa."
        s2_desc = "Páginas focadas em conversão, com design responsivo, comunicação persuasiva e estrutura estratégica para transformar visitantes em novos contactos."
        s3_desc = "Gestão estratégica de campanhas no Google Ads e redes sociais, conectando a sua oferta a clientes prontos para comprar com foco em retorno sobre o investimento."
        s4_desc = "Desenvolvimento de sistemas web e automações sob medida para digitalizar rotinas, integrar dados e acelerar a operação do seu negócio."
        s5_desc = "Otimização da sua presença no Google Maps e pesquisas locais para que a sua empresa seja facilmente encontrada por clientes na sua zona."

        faq_items = [
            {
                "q": "Quanto tempo demora para o website ficar pronto?",
                "a": "O prazo depende da dimensão e complexidade do projeto. Após analisarmos as necessidades, apresentamos um prazo estimado para a entrega."
            },
            {
                "q": "O que está incluído nas landing pages?",
                "a": "As landing pages são desenvolvidas com foco em conversão, incluindo estrutura estratégica, design responsivo e conteúdo orientado ao objetivo da campanha."
            },
            {
                "q": "Qual é o investimento em tráfego pago?",
                "a": "O investimento em tráfego pago varia de acordo com os objetivos, público, plataformas e orçamento definido para a campanha."
            },
            {
                "q": "Desenvolvem sistemas à medida?",
                "a": "Sim. Desenvolvemos sistemas personalizados de acordo com as necessidades e processos específicos de cada negócio."
            },
            {
                "q": "Como funciona o processo de contratação?",
                "a": "Após o primeiro contacto, analisamos as necessidades do projeto, definimos o âmbito e apresentamos a proposta correspondente."
            }
        ]

    elif lang_code == 'br':
        title = "Criação de Sites e Soluções Digitais | Magnani UP®"
        meta_desc = "Criação de sites profissionais, SEO, landing pages, tráfego pago e soluções digitais para empresas que desejam expandir seus negócios e presença online."
        canonical = "https://dominio.com/br/"
        og_locale = "pt_BR"
        og_alt = "Magnani UP® - Agência Digital e Criação de Sites no Brasil"
        hero_desc = "Criamos sites profissionais, modernos e de alta performance para empresas que buscam fortalecer sua presença digital, atrair clientes qualificados e impulsionar resultados reais."
        
        b1_title = "Sites rápidos e otimizados"
        b1_desc = "para mecanismos de busca (SEO)"
        b2_title = "Design 100% responsivo"
        b2_desc = "em todos os dispositivos"
        b3_title = "Suporte e acompanhamento"
        b3_desc = "em todas as etapas do projeto"
        
        wa_link = "https://wa.me/5544998018242"
        
        service_links = [
            ('/br/servicos/seo/', 'SEO'),
            ('/br/servicos/landing-pages/', 'Landing Pages'),
            ('/br/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/br/servicos/sistemas/', 'Criação de Sistemas'),
            ('/br/servicos/google-meu-negocio/', 'Google Meu Negócio')
        ]
        
        s1_desc = "Otimização técnica e estratégica para posicionar o seu site nas buscas do Google, atraindo tráfego orgânico qualificado para a sua empresa."
        s2_desc = "Páginas focadas em conversão, com design responsivo, redação persuasiva e estrutura estratégica para transformar visitantes em novos contatos."
        s3_desc = "Gestão estratégica de campanhas no Google Ads e redes sociais, conectando sua oferta a clientes prontos para comprar com foco em retorno real."
        s4_desc = "Desenvolvimento de sistemas web e automações sob medida para digitalizar processos, integrar dados e aumentar a produtividade da sua empresa."
        s5_desc = "Otimização da sua presença no Google Maps e buscas locais para que a sua empresa seja facilmente encontrada por clientes da sua região."

        faq_items = [
            {
                "q": "Quanto tempo demora para o site ficar pronto?",
                "a": "O prazo depende do porte e da complexidade do projeto. Após analisarmos as necessidades, apresentamos um prazo estimado para a entrega."
            },
            {
                "q": "O que está incluído nas landing pages?",
                "a": "As landing pages são desenvolvidas com foco em conversão, incluindo estrutura estratégica, design responsivo e conteúdo orientado ao objetivo da campanha."
            },
            {
                "q": "Qual é o investimento em tráfego pago?",
                "a": "O investimento em tráfego pago varia de acordo com os objetivos, público, plataformas e orçamento definido para a campanha."
            },
            {
                "q": "Desenvolvem sistemas sob medida?",
                "a": "Sim. Desenvolvemos sistemas personalizados de acordo com as necessidades e processos específicos de cada negócio."
            },
            {
                "q": "Como funciona o processo de contratação?",
                "a": "Após o primeiro contato, analisamos as necessidades do projeto, definimos o escopo e apresentamos a proposta correspondente."
            }
        ]

    else: # 'it'
        title = "Creazione Siti Web e Soluzioni Digitali | Magnani UP®"
        meta_desc = "Creazione siti web professionali, SEO, landing page, traffico a pagamento e soluzioni digitali su misura per aziende che vogliono crescere online."
        canonical = "https://dominio.com/it/"
        og_locale = "it_IT"
        og_alt = "Magnani UP® - Agenzia Digitale e Creazione Siti Web in Italia"
        hero_desc = "Sviluppiamo siti web professionali, veloci e su misura per aziende che vogliono rafforzare la presenza digitale, acquisire nuovi clienti e ottenere risultati concreti."
        
        b1_title = "Siti veloci e ottimizzati"
        b1_desc = "per i motori di ricerca (SEO)"
        b2_title = "Design 100% reattivo"
        b2_desc = "su tutti i dispositivi"
        b3_title = "Supporto e affiancamento"
        b3_desc = "in tutte le fasi del progetto"
        
        wa_link = "https://wa.me/393313882760"
        
        service_links = [
            ('/it/servizi/seo/', 'SEO'),
            ('/it/servizi/landing-page/', 'Landing Page'),
            ('/it/servizi/traffico-a-pagamento/', 'Traffico a Pagamento'),
            ('/it/servizi/sistemi/', 'Sviluppo Sistemi'),
            ('/it/servizi/google-business-profile/', 'Google Business Profile')
        ]
        
        s1_desc = "Ottimizzazione tecnica e strategica per posizionare il tuo sito web sui motori di ricerca, attirando traffico organico qualificato."
        s2_desc = "Pagine web orientate alla conversione con struttura persuasiva e design reattivo per trasformare gli utenti in contatti commerciali."
        s3_desc = "Gestione professionale di campagne pubblicitarie Google Ads e social network con monitoraggio trasparente del ritorno sull'investimento."
        s4_desc = "Sviluppo di piattaforme web e software personalizzati per automatizzare i flussi aziendali e aumentare la produttività."
        s5_desc = "Ottimizzazione della presenza su Google Maps e ricerche locali per farti trovare facilmente dai clienti della tua zona."

        faq_items = [
            {
                "q": "Quanto tempo ci vuole per completare un sito web?",
                "a": "I tempi dipendono dalle dimensioni e dalla complessità del progetto. Dopo aver analizzato le tue esigenze, presentiamo una stima dettagliata per la consegna."
            },
            {
                "q": "Cosa è incluso nelle landing page?",
                "a": "Le landing page sono sviluppate con focus sulla conversione, includendo una struttura strategica, design reattivo e contenuti orientati agli obiettivi della campagna."
            },
            {
                "q": "Qual è l'investimento richiesto per la pubblicità online?",
                "a": "L'investimento in traffico a pagamento varia a seconda degli obiettivi, del pubblico di riferimento, delle piattaforme e del budget definito per la campagna."
            },
            {
                "q": "Sviluppate sistemi personalizzati su misura?",
                "a": "Sì. Sviluppiamo sistemi personalizzati in base alle esigenze e ai processi operativi specifici di ogni azienda."
            },
            {
                "q": "Come funziona il processo di collaborazione?",
                "a": "Dopo il primo contatto, analizziamo i requisiti del progetto, definiamo l'ambito di lavoro e presentiamo la proposta corrispondente."
            }
        ]

    # Replace <title>
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    
    # Replace meta description
    content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']>', f'<meta name="description" content="{meta_desc}">', content)
    
    # Ensure meta robots
    if '<meta name="robots"' not in content:
        content = content.replace(f'<meta name="description" content="{meta_desc}">',
                                  f'<meta name="description" content="{meta_desc}">\n  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">')

    # Replace canonical
    content = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\'].*?["\']>', f'<link rel="canonical" href="{canonical}">', content)

    # Replace Open Graph
    og_block = f'''  <!-- Open Graph / Redes Sociais -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Magnani UP®">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:image" content="https://dominio.com/images/og/og-magnani-up.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{og_alt}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{meta_desc}">
  <meta name="twitter:image" content="https://dominio.com/images/og/og-magnani-up.png">'''

    content = re.sub(r'<!-- Open Graph -->.*?(?=<!-- Tipografia|\s*<link rel="icon")', og_block + '\n\n', content, flags=re.DOTALL)

    # Build Schema JSON-LD
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
            "description": meta_desc,
            "sameAs": [
                "https://instagram.com",
                "https://linkedin.com"
            ],
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": wa_link.replace("https://wa.me/", "+"),
                "contactType": "customer service",
                "availableLanguage": ["Portuguese", "Italian"]
            }
        },
        {
            "@type": "WebSite",
            "@id": "https://dominio.com/#website",
            "url": "https://dominio.com/",
            "name": "Magnani UP®",
            "publisher": {
                "@id": "https://dominio.com/#organization"
            },
            "inLanguage": lang_code if lang_code == 'it' else f"pt-{lang_code.upper()}"
        },
        {
            "@type": "WebPage",
            "@id": f"{canonical}#webpage",
            "url": canonical,
            "name": title,
            "description": meta_desc,
            "isPartOf": {
                "@id": "https://dominio.com/#website"
            },
            "inLanguage": lang_code if lang_code == 'it' else f"pt-{lang_code.upper()}",
            "about": {
                "@id": "https://dominio.com/#organization"
            }
        },
        {
            "@type": "FAQPage",
            "@id": f"{canonical}#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item["q"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": item["a"]
                    }
                } for item in faq_items
            ]
        }
    ]

    schema_json = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, indent=2, ensure_ascii=False)
    new_schema_tag = f'''  <!-- Schema.org Internacionalizado (Organization, WebSite, WebPage, FAQPage) -->
  <script type="application/ld+json">
{schema_json}
  </script>'''

    content = re.sub(r'<!-- Schema\.org.*?-->\s*<script type="application/ld\+json">.*?</script>', new_schema_tag, content, flags=re.DOTALL)

    # Hero description
    content = re.sub(r'<p class="hero-description">.*?</p>', f'<p class="hero-description">\n                {hero_desc}\n              </p>', content, flags=re.DOTALL)

    # Benefits section text
    content = re.sub(r'<span class="benefits-text-title">Sites otimizados</span>\s*<span class="benefits-text-desc">.*?</span>',
                     f'<span class="benefits-text-title">{b1_title}</span>\n                  <span class="benefits-text-desc">{b1_desc}</span>', content)
    content = re.sub(r'<span class="benefits-text-title">Sites rápidos e otimizados</span>\s*<span class="benefits-text-desc">.*?</span>',
                     f'<span class="benefits-text-title">{b1_title}</span>\n                  <span class="benefits-text-desc">{b1_desc}</span>', content)
    content = re.sub(r'<span class="benefits-text-title">Siti veloci e ottimizzati</span>\s*<span class="benefits-text-desc">.*?</span>',
                     f'<span class="benefits-text-title">{b1_title}</span>\n                  <span class="benefits-text-desc">{b1_desc}</span>', content)

    # Service card descriptions
    descs = [s1_desc, s2_desc, s3_desc, s4_desc, s5_desc]
    # Replace the card descriptions
    def repl_card_desc(m):
        idx = repl_card_desc.count
        repl_card_desc.count += 1
        if idx < len(descs):
            return f'<p class="service-card-desc">\n                  {descs[idx]}\n                </p>'
        return m.group(0)
    repl_card_desc.count = 0
    content = re.sub(r'<p class="service-card-desc">.*?</p>', repl_card_desc, content, flags=re.DOTALL)

    # Replace footer links for services
    footer_links_html = "".join([f'          <li><a href="{href}" class="footer-link">{label}</a></li>\n' for href, label in service_links])
    footer_col3_regex = r'(<nav class="footer-col" aria-label="[^"]*">\s*<h3 class="footer-col-title">[^<]*</h3>\s*<ul class="footer-links-list">)(.*?)(</ul>\s*</nav>)'
    
    # We find the second footer-col (which is services)
    matches = list(re.finditer(footer_col3_regex, content, re.DOTALL))
    if len(matches) >= 2:
        m = matches[1] # second nav is Serviços
        replacement = m.group(1) + "\n" + footer_links_html + "        " + m.group(3)
        content = content[:m.start()] + replacement + content[m.end():]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path} and backup {backup_path}")

update_home('pt/index.html', '.backup/pt_index.html', 'pt')
update_home('br/index.html', '.backup/br_index.html', 'br')
update_home('it/index.html', '.backup/it_index.html', 'it')
