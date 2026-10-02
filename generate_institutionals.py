import os
import json
from scratch_services_data import DATA

INSTITUTIONAL_CONFIG = {
    'pt': {
        'sobre': {
            'path': 'pt/sobre/index.html',
            'title': 'Sobre a Magnani UP® | Agência Digital em Portugal',
            'meta_desc': 'Conheça a Magnani UP®: agência digital focada em websites profissionais, design estratégico, SEO e soluções tecnológicas para empresas.',
            'h1': 'Criamos experiências digitais que impulsionam empresas',
            'tag': 'SOBRE A MAGNANI UP®',
            'hero_desc': 'A Magnani UP® nasceu com o propósito de transformar a presença online de empresas através de websites modernos, tecnologia robusta e estratégias digitais focadas em gerar resultados sustentáveis.',
            'cards_tag': 'OS NOSSOS PILARES',
            'cards_title': 'Compromisso com qualidade, transparência e performance',
            'cards_desc': 'Não criamos apenas websites; desenvolvemos ferramentas estratégicas desenhadas para fortalecer marcas e atrair novos clientes.',
            'cards': [
                {
                    'title': 'Design Estratégico & Moderno',
                    'desc': 'Cada layout é concebido com atenção minuciosa à tipografia, hierarquia visual e usabilidade intuitiva para transmitir confiança imediata.'
                },
                {
                    'title': 'Tecnologia & Velocidade',
                    'desc': 'Desenvolvemos com código limpo, sem dependências desnecessárias, assegurando carregamento veloz e pontuações elevadas nos motores de busca.'
                },
                {
                    'title': 'Orientação para Resultados',
                    'desc': 'Todas as decisões técnicas e criativas visam facilitar o contacto do cliente com a sua empresa e impulsionar o seu crescimento comercial.'
                }
            ]
        },
        'faq': {
            'path': 'pt/faq/index.html',
            'title': 'Perguntas Frequentes (FAQ) | Magnani UP® Portugal',
            'meta_desc': 'Tire todas as suas dúvidas sobre prazos, criação de websites, landing pages, tráfego pago, SEO e contratação de serviços digitais na Magnani UP®.',
            'h1': 'Perguntas Frequentes sobre os Nossos Serviços',
            'tag': 'ESCLARECIMENTO DE DÚVIDAS',
            'hero_desc': 'Reunimos as respostas para as principais questões sobre como trabalhamos, prazos médios, metodologias e contratação dos nossos serviços digitais.',
            'faqs': [
                {
                    'q': 'Quanto tempo demora para o website ficar pronto?',
                    'a': 'O prazo depende da dimensão e complexidade do projeto. Após analisarmos as necessidades, apresentamos um prazo estimado para a entrega.'
                },
                {
                    'q': 'O que está incluído nas landing pages?',
                    'a': 'As landing pages são desenvolvidas com foco em conversão, incluindo estrutura estratégica, design responsivo e conteúdo orientado ao objetivo da campanha.'
                },
                {
                    'q': 'Qual é o investimento em tráfego pago?',
                    'a': 'O investimento em tráfego pago varia de acordo com os objetivos, público, plataformas e orçamento definido para a campanha.'
                },
                {
                    'q': 'Desenvolvem sistemas à medida?',
                    'a': 'Sim. Desenvolvemos sistemas personalizados de acordo com as necessidades e processos específicos de cada negócio.'
                },
                {
                    'q': 'Como funciona o processo de contratação?',
                    'a': 'Após o primeiro contacto, analisamos as necessidades do projeto, definimos o âmbito e apresentamos a proposta correspondente.'
                },
                {
                    'q': 'O website fica adaptado para telemóveis e tablets?',
                    'a': 'Sim, todos os websites desenvolvidos pela Magnani UP® são 100% responsivos e rigorosamente testados em computadores, tablets e smartphones.'
                },
                {
                    'q': 'Terei acompanhamento após a conclusão do projeto?',
                    'a': 'Sim. Prestamos suporte durante a publicação e disponibilizamos pacotes de acompanhamento contínuo e evolução técnica conforme necessário.'
                }
            ]
        },
        'contacto': {
            'path': 'pt/contacto/index.html',
            'title': 'Contacto & Orçamento | Magnani UP® Portugal',
            'meta_desc': 'Entre em contacto com a equipa da Magnani UP® em Portugal. Fale connosco pelo WhatsApp ou agende uma reunião para discutir o seu projeto digital.',
            'h1': 'Vamos conversar sobre o seu próximo projeto digital?',
            'tag': 'FALE CONNOSCO',
            'hero_desc': 'Estamos disponíveis para ouvir os seus desafios, analisar as suas metas e propor a solução digital mais eficiente para a sua empresa.',
            'cards_tag': 'CANAIS DE ATENDIMENTO',
            'cards_title': 'Comunicação direta, rápida e transparente',
            'cards_desc': 'Escolha a forma mais conveniente para falar com os nossos especialistas.',
            'cards': [
                {
                    'title': 'WhatsApp Direto',
                    'desc': 'Fale em tempo real com a nossa equipa para tirar dúvidas imediatas e solicitar uma avaliação do seu projeto.'
                },
                {
                    'title': 'Atendimento Comercial',
                    'desc': 'Analisamos o seu segmento de mercado e preparamos uma proposta personalizada e transparente.'
                },
                {
                    'title': 'Presença Multirregional',
                    'desc': 'Soluções digitais prontas para empresas que atuam em Portugal, Brasil e no mercado europeu.'
                }
            ]
        }
    },
    'br': {
        'sobre': {
            'path': 'br/sobre/index.html',
            'title': 'Sobre a Magnani UP® | Agência Digital',
            'meta_desc': 'Conheça a Magnani UP®: agência digital especializada em criação de sites profissionais, landing pages, SEO e soluções personalizadas para empresas.',
            'h1': 'Criamos experiências digitais que impulsionam empresas',
            'tag': 'SOBRE A MAGNANI UP®',
            'hero_desc': 'A Magnani UP® foi criada para transformar a presença online de empresas por meio de sites modernos, código otimizado e soluções digitais focadas em gerar resultados reais.',
            'cards_tag': 'NOSSOS PILARES',
            'cards_title': 'Compromisso com qualidade, transparência e eficiência',
            'cards_desc': 'Desenvolvemos soluções que combinam design moderno, velocidade de carregamento e foco na geração de novos clientes.',
            'cards': [
                {
                    'title': 'Design Estratégico & Moderno',
                    'desc': 'Layouts criados para encantar o usuário, com hierarquia visual clara e navegação fluida em qualquer dispositivo.'
                },
                {
                    'title': 'Tecnologia & Velocidade',
                    'desc': 'Código limpo e otimizado para proporcionar rapidez, estabilidade e conformidade com as exigências dos buscadores.'
                },
                {
                    'title': 'Foco em Conversão',
                    'desc': 'Estrutura pensada para facilitar o contato de clientes qualificados com a equipe comercial do seu negócio.'
                }
            ]
        },
        'faq': {
            'path': 'br/faq/index.html',
            'title': 'Perguntas Frequentes (FAQ) | Magnani UP®',
            'meta_desc': 'Tire suas dúvidas sobre criação de sites, landing pages, tráfego pago, SEO e desenvolvimento de sistemas na Magnani UP®.',
            'h1': 'Perguntas Frequentes sobre Nossos Serviços',
            'tag': 'DÚVIDAS FREQUENTES',
            'hero_desc': 'Reunimos as respostas para as principais dúvidas sobre prazos, funcionamento dos serviços e processo de contratação da Magnani UP®.',
            'faqs': [
                {
                    'q': 'Quanto tempo demora para o site ficar pronto?',
                    'a': 'O prazo depende do porte e da complexidade do projeto. Após analisarmos as necessidades, apresentamos um prazo estimado para a entrega.'
                },
                {
                    'q': 'O que está incluído nas landing pages?',
                    'a': 'As landing pages são desenvolvidas com foco em conversão, incluindo estrutura estratégica, design responsivo e conteúdo orientado ao objetivo da campanha.'
                },
                {
                    'q': 'Qual é o investimento em tráfego pago?',
                    'a': 'O investimento em tráfego pago varia de acordo com os objetivos, público, plataformas e orçamento definido para a campanha.'
                },
                {
                    'q': 'Desenvolvem sistemas sob medida?',
                    'a': 'Sim. Desenvolvemos sistemas personalizados de acordo com as necessidades e processos específicos de cada negócio.'
                },
                {
                    'q': 'Como funciona o processo de contratação?',
                    'a': 'Após o primeiro contato, analisamos as necessidades do projeto, definimos o escopo e apresentamos a proposta correspondente.'
                },
                {
                    'q': 'O site funciona perfeitamente no celular?',
                    'a': 'Sim, todos os sites que criamos são 100% responsivos e funcionam perfeitamente em celulares, tablets e computadores.'
                },
                {
                    'q': 'Terei suporte após o site ser publicado?',
                    'a': 'Sim, oferecemos acompanhamento técnico e suporte para tirar dúvidas e manter seu site funcionando com máxima estabilidade.'
                }
            ]
        },
        'contato': {
            'path': 'br/contato/index.html',
            'title': 'Contato & Orçamento | Magnani UP®',
            'meta_desc': 'Entre em contato com a equipe da Magnani UP®. Fale conosco pelo WhatsApp ou solicite um orçamento para seu projeto digital.',
            'h1': 'Vamos conversar sobre o seu próximo projeto digital?',
            'tag': 'FALE CONOSCO',
            'hero_desc': 'Estamos prontos para entender as metas do seu negócio e indicar a solução digital mais eficiente para você atrair novos clientes.',
            'cards_tag': 'CANAIS DE CONTATO',
            'cards_title': 'Atendimento rápido e direto com nossa equipe',
            'cards_desc': 'Escolha a opção mais prática para falar conosco.',
            'cards': [
                {
                    'title': 'WhatsApp Direto',
                    'desc': 'Converse diretamente com nossos especialistas para tirar dúvidas e receber orientações para o seu projeto.'
                },
                {
                    'title': 'Orçamento Personalizado',
                    'desc': 'Apresentamos uma proposta clara e transparente, de acordo com o estágio e objetivos da sua empresa.'
                },
                {
                    'title': 'Atendimento Ágil',
                    'desc': 'Comunicação descomplicada para que você tenha respostas rápidas e suporte profissional em cada etapa.'
                }
            ]
        }
    },
    'it': {
        'sobre': {
            'path': 'it/chi-siamo/index.html',
            'title': 'Chi Siamo | Magnani UP® Agenzia Digitale',
            'meta_desc': 'Scopri Magnani UP®: agenzia digitale specializzata nella realizzazione di siti web professionali, landing page, SEO e soluzioni su misura per aziende.',
            'h1': 'Creiamo esperienze digitali che fanno crescere le aziende',
            'tag': 'CHI SIAMO',
            'hero_desc': 'Magnani UP® nasce con l\'obiettivo di rafforzare la presenza online delle imprese attraverso siti web moderni, tecnologie veloci e strategie digitali concrete.',
            'cards_tag': 'I NOSTRI VALORI',
            'cards_title': 'Qualità, trasparenza e orientamento ai risultati',
            'cards_desc': 'Non creiamo semplici siti web, ma strumenti di lavoro progettati per valorizzare il brand e generare nuove opportunità commerciali.',
            'cards': [
                {
                    'title': 'Design Strategico e Moderno',
                    'desc': 'Ogni interfaccia è studiata per garantire un\'esperienza utente fluida, piacevole e orientata alla fiducia del cliente.'
                },
                {
                    'title': 'Tecnologia e Performance',
                    'desc': 'Sviluppiamo con codice pulito e leggero, assicurando tempi di caricamento rapidi e conformità con i motori di ricerca.'
                },
                {
                    'title': 'Focalizzati sulla Conversione',
                    'desc': 'Ogni dettaglio è progettato per semplificare il contatto tra i potenziali clienti e la tua azienda.'
                }
            ]
        },
        'faq': {
            'path': 'it/faq/index.html',
            'title': 'Domande Frequenti (FAQ) | Magnani UP®',
            'meta_desc': 'Risposte alle domande più frequenti su realizzazione siti web, landing page, pubblicità online, SEO e sistemi su misura con Magnani UP®.',
            'h1': 'Domande Frequenti sui Nostri Servizi',
            'tag': 'DOMANDE E RISPOSTE',
            'hero_desc': 'Ecco le risposte ai dubbi più comuni su modalità di lavoro, tempistiche di consegna e modalità di collaborazione.',
            'faqs': [
                {
                    'q': 'Quanto tempo ci vuole per completare un sito web?',
                    'a': 'I tempi dipendono dalle dimensioni e dalla complessità del progetto. Dopo aver analizzato le tue esigenze, presentiamo una stima dettagliata per la consegna.'
                },
                {
                    'q': 'Cosa è incluso nelle landing page?',
                    'a': 'Le landing page sono sviluppate con focus sulla conversione, includendo una struttura strategica, design reattivo e contenuti orientati agli obiettivi della campagna.'
                },
                {
                    'q': 'Qual è l\'investimento richiesto per la pubblicità online?',
                    'a': 'L\'investimento in traffico a pagamento varia a seconda degli obiettivi, del pubblico di riferimento, delle piattaforme e del budget definito per la campagna.'
                },
                {
                    'q': 'Sviluppate sistemi personalizzati su misura?',
                    'a': 'Sì. Sviluppiamo sistemi personalizzati in base alle esigenze e ai processi operativi specifici di ogni azienda.'
                },
                {
                    'q': 'Come funziona il processo di collaborazione?',
                    'a': 'Dopo il primo contatto, analizziamo i requisiti del progetto, definiamo l\'ambito di lavoro e presentiamo la proposta corrispondente.'
                },
                {
                    'q': 'Il sito è ottimizzato per dispositivi mobili?',
                    'a': 'Assolutamente sì. Tutti i siti web sviluppati da Magnani UP® sono al 100% responsive e ottimizzati per smartphone, tablet e desktop.'
                },
                {
                    'q': 'Fornite supporto dopo la pubblicazione?',
                    'a': 'Sì, garantiamo assistenza tecnica durante il lancio e proponiamo soluzioni di manutenzione per garantire sicurezza e stabilità continua.'
                }
            ]
        },
        'contato': {
            'path': 'it/contatti/index.html',
            'title': 'Contatti & Preventivo | Magnani UP®',
            'meta_desc': 'Mettiti in contatto con il team di Magnani UP®. Scrivici su WhatsApp o richiedi un preventivo personalizzato per il tuo progetto digitale.',
            'h1': 'Parliamo del tuo prossimo progetto digitale?',
            'tag': 'CONTATTACI',
            'hero_desc': 'Siamo pronti ad ascoltare i tuoi obiettivi aziendali per studiare la soluzione digitale più adatta alla tua crescita.',
            'cards_tag': 'CANALI DI CONTATTO',
            'cards_title': 'Comunicazione rapida, chiara e trasparente',
            'cards_desc': 'Scegli la modalità che preferisci per iniziare a dialogare con noi.',
            'cards': [
                {
                    'title': 'WhatsApp Diretto',
                    'desc': 'Parla direttamente con i nostri specialisti per ricevere chiarimenti immediati sul tuo progetto.'
                },
                {
                    'title': 'Preventivo Personalizzato',
                    'desc': 'Elaboriamo proposte trasparenti e dettagliate, calibrate sulle reali esigenze operative della tua azienda.'
                },
                {
                    'title': 'Consulenza Dedicata',
                    'desc': 'Un dialogo professionale per individuare la combinazione di servizi più efficace per il tuo business.'
                }
            ]
        }
    }
}

def render_institutional(lang_code, page_type):
    d = DATA[lang_code]
    cfg = INSTITUTIONAL_CONFIG[lang_code][page_type]
    
    # URLs
    canonical_map = {
        'sobre': {
            'pt': 'https://dominio.com/pt/sobre/',
            'br': 'https://dominio.com/br/sobre/',
            'it': 'https://dominio.com/it/chi-siamo/'
        },
        'faq': {
            'pt': 'https://dominio.com/pt/faq/',
            'br': 'https://dominio.com/br/faq/',
            'it': 'https://dominio.com/it/faq/'
        },
        'contacto': {
            'pt': 'https://dominio.com/pt/contacto/',
            'br': 'https://dominio.com/br/contato/',
            'it': 'https://dominio.com/it/contatti/'
        },
        'contato': {
            'pt': 'https://dominio.com/pt/contacto/',
            'br': 'https://dominio.com/br/contato/',
            'it': 'https://dominio.com/it/contatti/'
        }
    }
    
    key = 'contacto' if page_type in ['contacto', 'contato'] else page_type
    pt_url = canonical_map[key]['pt']
    br_url = canonical_map[key]['br']
    it_url = canonical_map[key]['it']
    current_canonical = canonical_map[key][lang_code]

    if lang_code == 'pt':
        nav_items = [
            (d['base_url'], 'Início'),
            (d['servicos_url'], 'Serviços'),
            (d['sobre_url'], 'Sobre'),
            (d['faq_url'], 'FAQ'),
            (d['contato_url'], 'Contacto')
        ]
        footer_serv_links = [
            ('/pt/servicos/seo/', 'SEO'),
            ('/pt/servicos/landing-pages/', 'Landing Pages'),
            ('/pt/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/pt/servicos/sistemas/', 'Criação de Sistemas'),
            ('/pt/servicos/google-meu-negocio/', 'Google Perfil de Empresa')
        ]
        page_name_map = {'sobre': 'Sobre Nós', 'faq': 'Perguntas Frequentes', 'contacto': 'Contacto'}
    elif lang_code == 'br':
        nav_items = [
            (d['base_url'], 'Início'),
            (d['servicos_url'], 'Serviços'),
            (d['sobre_url'], 'Sobre'),
            (d['faq_url'], 'FAQ'),
            (d['contato_url'], 'Contato')
        ]
        footer_serv_links = [
            ('/br/servicos/seo/', 'SEO'),
            ('/br/servicos/landing-pages/', 'Landing Pages'),
            ('/br/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/br/servicos/sistemas/', 'Criação de Sistemas'),
            ('/br/servicos/google-meu-negocio/', 'Google Meu Negócio')
        ]
        page_name_map = {'sobre': 'Sobre', 'faq': 'FAQ', 'contato': 'Contato'}
    else:
        nav_items = [
            (d['base_url'], 'Home'),
            (d['servicos_url'], 'Servizi'),
            (d['sobre_url'], 'Chi Siamo'),
            (d['faq_url'], 'FAQ'),
            (d['contato_url'], 'Contatti')
        ]
        footer_serv_links = [
            ('/it/servizi/seo/', 'SEO'),
            ('/it/servizi/landing-page/', 'Landing Page'),
            ('/it/servizi/traffico-a-pagamento/', 'Traffico a Pagamento'),
            ('/it/servizi/sistemi/', 'Sviluppo Sistemi'),
            ('/it/servizi/google-business-profile/', 'Google Business Profile')
        ]
        page_name_map = {'sobre': 'Chi Siamo', 'faq': 'FAQ', 'contato': 'Contatti'}

    breadcrumb_cur = page_name_map.get(key, 'Página')

    # Schema JSON-LD
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
                    "name": breadcrumb_cur,
                    "item": current_canonical
                }
            ]
        }
    ]

    if page_type == 'faq':
        schema_graph.append({
            "@type": "FAQPage",
            "@id": f"{current_canonical}#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": f['q'],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f['a']
                    }
                } for f in cfg['faqs']
            ]
        })
    elif page_type in ['contacto', 'contato']:
        schema_graph.append({
            "@type": "ContactPage",
            "@id": f"{current_canonical}#contactpage",
            "name": cfg['title'],
            "description": cfg['meta_desc'],
            "url": current_canonical
        })
    else:
        schema_graph.append({
            "@type": "AboutPage",
            "@id": f"{current_canonical}#aboutpage",
            "name": cfg['title'],
            "description": cfg['meta_desc'],
            "url": current_canonical
        })

    schema_json = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, indent=2, ensure_ascii=False)

    # Body sections
    if page_type == 'faq':
        faq_items_html = ""
        for i, f in enumerate(cfg['faqs']):
            idx = i + 1
            faq_items_html += f'''
            <div class="faq-item">
              <button type="button" 
                      class="faq-question-btn" 
                      id="faq-page-btn-{idx}" 
                      aria-expanded="false" 
                      aria-controls="faq-page-ans-{idx}">
                <span class="faq-question-left">
                  <span class="faq-num-badge" aria-hidden="true">0{idx}</span>
                  <span class="faq-question-text">{f['q']}</span>
                </span>
                <svg class="faq-chevron-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                  <path d="M3.5 6L8 10.5L12.5 6"/>
                </svg>
              </button>
              <div class="faq-answer-panel" id="faq-page-ans-{idx}" role="region" aria-labelledby="faq-page-btn-{idx}">
                <div class="faq-answer-inner">
                  <div class="faq-answer-content">
                    <p class="faq-answer-text">{f['a']}</p>
                  </div>
                </div>
              </div>
            </div>'''
        content_section = f'''
      <section class="faq-section" id="duvidas" aria-labelledby="inst-h1">
        <div class="faq-container">
          <div class="faq-accordion-list" role="region" aria-label="{cfg['h1']}">
            {faq_items_html}
          </div>
        </div>
      </section>'''
    else:
        cards_html = ""
        for c in cfg['cards']:
            cards_html += f'''
            <article class="detail-card">
              <div class="detail-card-icon" aria-hidden="true">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
                </svg>
              </div>
              <h2 class="detail-card-title">{c['title']}</h2>
              <p class="detail-card-desc">{c['desc']}</p>
            </article>'''
        content_section = f'''
      <section class="detail-section" id="conteudo" aria-labelledby="inst-h1">
        <div class="detail-container">
          <div class="detail-header">
            <div class="detail-header-left">
              <div class="detail-tag">
                <span class="detail-tag-line" aria-hidden="true"></span>
                <span class="detail-tag-text">{cfg['cards_tag']}</span>
              </div>
              <h2 class="detail-section-title">
                {cfg['cards_title']}
              </h2>
              <p class="detail-section-desc">
                {cfg['cards_desc']}
              </p>
            </div>
          </div>

          <div class="detail-grid-3">
            {cards_html}
          </div>
        </div>
      </section>'''

    nav_links_html = "".join([f'<li class="nav-item"><a href="{href}" class="nav-link {"active" if href == current_canonical else ""}">{label}</a></li>\n' for href, label in nav_items])
    mobile_links_html = "".join([f'<li><a href="{href}" class="mobile-nav-link {"active" if href == current_canonical else ""}">{label}</a></li>\n' for href, label in nav_items])

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
  <link rel="canonical" href="{current_canonical}">
  
  <!-- Hreflang Rigoroso (pt-PT, pt-BR, it-IT, x-default) -->
  <link rel="alternate" hreflang="pt-PT" href="{pt_url}">
  <link rel="alternate" hreflang="pt-BR" href="{br_url}">
  <link rel="alternate" hreflang="it-IT" href="{it_url}">
  <link rel="alternate" hreflang="x-default" href="{pt_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{cfg['title']}">
  <meta property="og:description" content="{cfg['meta_desc']}">
  <meta property="og:url" content="{current_canonical}">
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
    <!-- Header -->
    <header class="site-header" id="site-header">
      <div class="header-container">
        
        <a href="{d['base_url']}" class="brand-logo" aria-label="Magnani UP® - {d['breadcrumb_home']}">
          <span class="brand-logo-content">
            <svg class="brand-symbol-svg" viewBox="0 0 56 36" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
              <defs>
                <linearGradient id="{lang_code}-inst-mGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#7045f5"/>
                  <stop offset="50%" stop-color="#8b5cf6"/>
                  <stop offset="100%" stop-color="#a78bfa"/>
                </linearGradient>
                <linearGradient id="{lang_code}-inst-upGrad" x1="0%" y1="100%" x2="0%" y2="0%">
                  <stop offset="0%" stop-color="#ffffff"/>
                  <stop offset="70%" stop-color="#ffffff"/>
                  <stop offset="100%" stop-color="#ede9fe"/>
                </linearGradient>
              </defs>
              <path d="M 4 29 L 10.8 9.5 C 11.8 6.8 14.8 6.8 15.8 9.5 L 20 18.5 C 21 20.8 23.8 20.8 24.8 18.5 L 29 9.5 C 30 6.8 33 6.8 34 9.5 L 38.5 20 C 39.2 21.8 41.5 22 42.5 20.5 L 46 14.5" 
                    stroke="url(#{lang_code}-inst-mGrad)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M 33.5 17.5 L 36.8 28.5 C 37.8 31.8 41.8 31.8 42.8 28.5 L 51.5 5.5 C 52 4.2 50.8 3.2 49.2 3.2 L 44 3.2 C 42.2 3.2 41 4.5 40.2 6.2 L 38 11" 
                    stroke="url(#{lang_code}-inst-upGrad)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
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
                {breadcrumb_cur}
              </li>
            </ol>
          </nav>
        </div>
      </section>

      <!-- Hero Interno -->
      <section class="internal-hero-section" aria-labelledby="inst-h1">
        <div class="internal-hero-container">
          <div class="internal-hero-kicker">
            <span class="internal-kicker-line" aria-hidden="true"></span>
            <span class="internal-kicker-text">{cfg['tag']}</span>
          </div>

          <h1 class="internal-hero-title" id="inst-h1">
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

      <!-- Bloco de Conteúdo -->
      {content_section}

      <!-- CTA Banner -->
      <section class="cta-section" id="contato" aria-labelledby="cta-inst-title">
        <div class="cta-container">
          <div class="cta-banner">
            <svg class="cta-bg-art" viewBox="0 0 1200 240" preserveAspectRatio="none" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
              <defs>
                <linearGradient id="{lang_code}-inst-ctaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#141a45" stop-opacity="0.95"/>
                  <stop offset="50%" stop-color="#0e1338" stop-opacity="0.98"/>
                  <stop offset="100%" stop-color="#080c25" stop-opacity="1"/>
                </linearGradient>
                <linearGradient id="{lang_code}-inst-stripeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%" stop-color="#7045f5" stop-opacity="0.35"/>
                  <stop offset="50%" stop-color="#8b5cf6" stop-opacity="0.2"/>
                  <stop offset="100%" stop-color="#f5711a" stop-opacity="0.35"/>
                </linearGradient>
              </defs>
              <rect width="1200" height="240" rx="20" fill="url(#{lang_code}-inst-ctaGrad)"/>
              <path d="M 680 -20 L 820 260 L 760 260 L 620 -20 Z" fill="url(#{lang_code}-inst-stripeGrad)"/>
              <path d="M 780 -20 L 920 260 L 880 260 L 740 -20 Z" fill="url(#{lang_code}-inst-stripeGrad)" opacity="0.6"/>
            </svg>

            <div class="cta-content-wrapper">
              <div class="cta-text-col">
                <h2 class="cta-title" id="cta-inst-title">
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
                    <linearGradient id="{lang_code}-instfoot-mGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                      <stop offset="0%" stop-color="#7045f5"/>
                      <stop offset="50%" stop-color="#8b5cf6"/>
                      <stop offset="100%" stop-color="#a78bfa"/>
                    </linearGradient>
                    <linearGradient id="{lang_code}-instfoot-upGrad" x1="0%" y1="100%" x2="0%" y2="0%">
                      <stop offset="0%" stop-color="#ffffff"/>
                      <stop offset="70%" stop-color="#ffffff"/>
                      <stop offset="100%" stop-color="#ede9fe"/>
                    </linearGradient>
                  </defs>
                  <path d="M 4 29 L 10.8 9.5 C 11.8 6.8 14.8 6.8 15.8 9.5 L 20 18.5 C 21 20.8 23.8 20.8 24.8 18.5 L 29 9.5 C 30 6.8 33 6.8 34 9.5 L 38.5 20 C 39.2 21.8 41.5 22 42.5 20.5 L 46 14.5" 
                        stroke="url(#{lang_code}-instfoot-mGrad)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M 33.5 17.5 L 36.8 28.5 C 37.8 31.8 41.8 31.8 42.8 28.5 L 51.5 5.5 C 52 4.2 50.8 3.2 49.2 3.2 L 44 3.2 C 42.2 3.2 41 4.5 40.2 6.2 L 38 11" 
                        stroke="url(#{lang_code}-instfoot-upGrad)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
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
  <script src="../../js/faq.js?v=20"></script>
  <script src="../../js/main.js?v=20"></script>
</body>
</html>'''
    return html

def main():
    for lang in ['pt', 'br', 'it']:
        for ptype in INSTITUTIONAL_CONFIG[lang].keys():
            content = render_institutional(lang, ptype)
            path = INSTITUTIONAL_CONFIG[lang][ptype]['path']
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Generated institutional page: {path}")

if __name__ == '__main__':
    main()
