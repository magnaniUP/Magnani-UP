import os
import re
import json

print("=== Starting PROMPT FINAL Implementation ===")

ICONS = {
    'browser': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
                    <rect x="3.5" y="4.5" width="21" height="18" rx="3" stroke="#ffffff" stroke-width="1.8"/>
                    <line x1="3.5" y1="9.5" x2="24.5" y2="9.5" stroke="#a78bfa" stroke-width="1.6"/>
                    <rect x="13.5" y="12.5" width="8" height="7.5" rx="1.5" fill="#1e295d" stroke="#f5711a" stroke-width="1.6"/>
                    <line x1="6.5" y1="13.5" x2="10.5" y2="13.5" stroke="#a78bfa" stroke-width="1.6" stroke-linecap="round"/>
                    <line x1="6.5" y1="17" x2="10.5" y2="17" stroke="#ffffff" stroke-width="1.4" stroke-linecap="round" opacity="0.8"/>
                  </svg>''',
    'search': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
                    <circle cx="12" cy="12" r="7" stroke="#a78bfa" stroke-width="2.2"/>
                    <path d="M17 17L23.5 23.5" stroke="#f5711a" stroke-width="2.4" stroke-linecap="round"/>
                  </svg>''',
    'traffic': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
                    <path d="M5 12V16H8L14 20V8L8 12H5Z" stroke="#f5711a" stroke-width="2" stroke-linejoin="round"/>
                    <path d="M7 16L8.5 21H11L9.8 16" stroke="#f5711a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M17.5 10C18.8 11.2 19.5 12.8 19.5 14C19.5 15.2 18.8 16.8 17.5 18" stroke="#a78bfa" stroke-width="2" stroke-linecap="round"/>
                    <path d="M20.5 7C22.8 9 24 11.5 24 14C24 16.5 22.8 19 20.5 21" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/>
                  </svg>''',
    'code': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
                    <path d="M8.5 9L3.5 14L8.5 19" stroke="#a78bfa" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M19.5 9L24.5 14L19.5 19" stroke="#a78bfa" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M16 6.5L12 21.5" stroke="#f5711a" stroke-width="2.2" stroke-linecap="round"/>
                  </svg>''',
    'store': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
                    <path d="M4 7H24L22 13H6L4 7Z" stroke="#a78bfa" stroke-width="2" stroke-linejoin="round" fill="#1c2156"/>
                    <path d="M10 7V13" stroke="#a78bfa" stroke-width="1.5"/>
                    <path d="M14 7V13" stroke="#a78bfa" stroke-width="1.5"/>
                    <path d="M18 7V13" stroke="#a78bfa" stroke-width="1.5"/>
                    <path d="M6 13V22H22V13" stroke="#f5711a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <rect x="11.5" y="16" width="5" height="6" stroke="#ffffff" stroke-width="1.6" fill="none"/>
                  </svg>'''
}

CONFIGS = {
    'pt': {
        'file_path': 'pt/index.html',
        'backup_path': '.backup/pt_index.html',
        'title': 'Criação de Sites e Soluções Digitais em Portugal | Magnani UP®',
        'meta_desc': 'Criação de sites profissionais, SEO, tráfego pago, desenvolvimento de sistemas e soluções digitais para empresas em Portugal.',
        'canonical': 'https://dominio.com/pt/',
        'og_locale': 'pt_PT',
        'og_alt': 'Magnani UP® - Agência Digital e Criação de Sites em Portugal',
        'kicker_text': 'AGÊNCIA DIGITAL &bull; CRIAÇÃO DE SITES E SOLUÇÕES DIGITAIS',
        'hero_desc': 'Na Magnani UP®, criamos sites profissionais, rápidos e responsivos para empresas que querem fortalecer a sua presença digital, apresentar melhor os seus serviços e transformar o website num verdadeiro ponto de contacto com os seus clientes.',
        'b1_title': 'Sites rápidos e preparados para pesquisa',
        'b1_desc': 'Estrutura técnica pensada para facilitar a navegação, o carregamento e a compreensão do conteúdo pelos motores de busca.',
        'b2_title': 'Design responsivo em todos os dispositivos',
        'b2_desc': 'Uma experiência consistente em computadores, tablets e smartphones, com foco em usabilidade e conversão.',
        'b3_title': 'Suporte em todas as etapas',
        'b3_desc': 'Acompanhamento desde o planeamento e desenvolvimento até à publicação e evolução do projeto.',
        'services_kicker': 'OS NOSSOS SERVIÇOS',
        'services_title': 'Soluções completas para<br><span class="services-title-highlight">o seu crescimento digital.</span>',
        'services_intro': 'Da criação de sites e desenvolvimento de soluções digitais ao SEO, tráfego pago e presença local, reunimos diferentes competências para ajudar empresas a construir uma presença online profissional, clara e preparada para crescer.',
        'service_cards': [
            {
                'icon': 'search',
                'title': 'SEO',
                'desc': 'Otimizamos a estrutura, o conteúdo e a experiência do seu site para facilitar a compreensão pelos motores de busca e aumentar as oportunidades de encontrar clientes através da pesquisa orgânica.',
                'link': '/pt/servicos/seo/',
                'aria': 'Saber mais sobre SEO'
            },
            {
                'icon': 'browser',
                'title': 'Criação de Sites',
                'desc': 'Criamos sites profissionais, modernos e responsivos, desenvolvidos para apresentar a sua empresa de forma clara, transmitir confiança e fortalecer a sua presença digital.',
                'link': '/pt/servicos/criacao-de-sites/',
                'aria': 'Saber mais sobre Criação de Sites'
            },
            {
                'icon': 'traffic',
                'title': 'Tráfego Pago',
                'desc': 'Planeamos campanhas de tráfego pago em plataformas como Google Ads e redes sociais, ligando anúncios, páginas de destino e objetivos comerciais para alcançar públicos relevantes.',
                'link': '/pt/servicos/trafego-pago/',
                'aria': 'Saber mais sobre Tráfego Pago'
            },
            {
                'icon': 'code',
                'title': 'Criação de Sistemas',
                'desc': 'Desenvolvemos soluções digitais à medida das necessidades de cada empresa, desde websites e ferramentas internas até sistemas personalizados que ajudam a simplificar processos.',
                'link': '/pt/servicos/sistemas/',
                'aria': 'Saber mais sobre Criação de Sistemas'
            },
            {
                'icon': 'store',
                'title': 'Google Meu Negócio',
                'desc': 'Ajudamos empresas a melhorar a sua presença local no Google, organizando informações importantes do negócio e facilitando que potenciais clientes encontrem os seus serviços.',
                'link': '/pt/servicos/google-meu-negocio/',
                'aria': 'Saber mais sobre Google Meu Negócio'
            }
        ],
        'process_kicker': 'COMO TRABALHAMOS',
        'process_title': 'Do planeamento à entrega,<br>com foco em <span class="process-title-highlight">resultados.</span>',
        'process_intro': 'Cada projeto começa com uma compreensão clara do negócio, do público e dos objetivos. A partir daí, estruturamos cada etapa para criar uma solução digital coerente, funcional e alinhada com a realidade da empresa.',
        'process_steps': [
            ('Descoberta', 'Conhecemos o seu negócio, os seus serviços, o público que pretende alcançar e os objetivos que pretende atingir com a sua presença digital.'),
            ('Planeamento', 'Definimos a estrutura do projeto, organizamos o conteúdo e estabelecemos uma estratégia clara para que o website tenha uma navegação simples e uma comunicação eficiente.'),
            ('Desenvolvimento', 'Transformamos a estratégia em uma experiência digital com design responsivo, tecnologia adequada, boa performance e uma estrutura preparada para mecanismos de pesquisa.'),
            ('Entrega e suporte', 'Publicamos o projeto e acompanhamos os próximos passos, permitindo que o website continue a evoluir conforme as necessidades do negócio.')
        ],
        'faq_kicker': 'PERGUNTAS FREQUENTES',
        'faq_title': 'Tire as suas <span class="faq-title-highlight">dúvidas.</span>',
        'faq_intro': 'Reunimos aqui as principais respostas sobre a criação de sites e soluções digitais da Magnani UP®. Se pretender saber mais, contacte a nossa equipa.',
        'faq_items': [
            {
                'q': 'Quanto tempo demora para o site ficar pronto?',
                'a': 'O prazo depende da dimensão do projeto, da quantidade de páginas e dos materiais necessários. Depois de conhecermos os objetivos da empresa e a estrutura do website, definimos um prazo adequado para o desenvolvimento.'
            },
            {
                'q': 'O que está incluído na criação de sites?',
                'a': 'A criação de sites envolve a definição da estrutura, organização do conteúdo, design, desenvolvimento responsivo e implementação das funcionalidades necessárias para apresentar a empresa de forma profissional. Cada website é estruturado de acordo com os objetivos e necessidades do projeto.'
            },
            {
                'q': 'Qual é o investimento em tráfego pago?',
                'a': 'O investimento depende dos objetivos da campanha, do mercado, do público e das plataformas utilizadas. O orçamento de mídia é definido separadamente do trabalho de gestão das campanhas.'
            },
            {
                'q': 'Desenvolvem sistemas à medida?',
                'a': 'Sim. Desenvolvemos soluções digitais personalizadas de acordo com as necessidades de cada empresa, desde websites e ferramentas específicas até sistemas que ajudam a organizar e automatizar processos.'
            },
            {
                'q': 'Como funciona o processo de contratação?',
                'a': 'O processo começa com uma conversa para compreender o negócio, os objetivos e o que precisa de ser desenvolvido. Depois analisamos o projeto, definimos o escopo e apresentamos uma proposta adequada às necessidades identificadas.'
            }
        ],
        'cta_title': 'O seu projeto digital começa<br>com uma <span class="cta-title-highlight">conversa.</span>',
        'cta_desc': 'Conte-nos sobre o seu negócio, os seus objetivos e o que pretende melhorar na sua presença digital. A partir daí, podemos identificar a solução mais adequada para o seu projeto.',
        'cta_btn_text': 'Falar com a equipa &rarr;',
        'footer_desc': 'A Magnani UP® desenvolve sites profissionais e soluções digitais para empresas que procuram construir uma presença online clara, moderna e preparada para crescer.',
        'footer_sub': 'Criação de sites, soluções digitais e estratégias para empresas que querem fortalecer a sua presença online.',
        'footer_serv_links': [
            ('/pt/servicos/seo/', 'SEO'),
            ('/pt/servicos/criacao-de-sites/', 'Criação de Sites'),
            ('/pt/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/pt/servicos/sistemas/', 'Criação de Sistemas'),
            ('/pt/servicos/google-meu-negocio/', 'Google Meu Negócio')
        ],
        'wa_link': 'https://wa.me/393313882760',
        'lang_code': 'pt'
    },
    'br': {
        'file_path': 'br/index.html',
        'backup_path': '.backup/br_index.html',
        'title': 'Criação de Sites e Soluções Digitais | Magnani UP®',
        'meta_desc': 'Criação de sites profissionais, SEO, tráfego pago, desenvolvimento de sistemas e soluções digitais para empresas no Brasil.',
        'canonical': 'https://dominio.com/br/',
        'og_locale': 'pt_BR',
        'og_alt': 'Magnani UP® - Agência Digital e Criação de Sites no Brasil',
        'kicker_text': 'AGÊNCIA DIGITAL &bull; CRIAÇÃO DE SITES E SOLUÇÕES DIGITAIS',
        'hero_desc': 'Na Magnani UP®, criamos sites profissionais, rápidos e responsivos para empresas que querem fortalecer a sua presença digital, apresentar melhor os seus serviços e transformar o website em um verdadeiro ponto de contato com os seus clientes.',
        'b1_title': 'Sites rápidos e preparados para busca',
        'b1_desc': 'Estrutura técnica pensada para facilitar a navegação, o carregamento e a compreensão do conteúdo pelos mecanismos de busca.',
        'b2_title': 'Design responsivo em todos os dispositivos',
        'b2_desc': 'Uma experiência consistente em computadores, tablets e smartphones, com foco em usabilidade e conversão.',
        'b3_title': 'Suporte em todas as etapas',
        'b3_desc': 'Acompanhamento desde o planejamento e desenvolvimento até a publicação e evolução do projeto.',
        'services_kicker': 'NOSSOS SERVIÇOS',
        'services_title': 'Soluções completas para<br><span class="services-title-highlight">o seu crescimento digital.</span>',
        'services_intro': 'Da criação de sites e desenvolvimento de soluções digitais ao SEO, tráfego pago e presença local, reunimos diferentes competências para ajudar empresas a construir uma presença online profissional, clara e preparada para crescer.',
        'service_cards': [
            {
                'icon': 'search',
                'title': 'SEO',
                'desc': 'Otimizamos a estrutura, o conteúdo e a experiência do seu site para facilitar a compreensão pelos mecanismos de busca e aumentar as oportunidades de encontrar clientes através da busca orgânica.',
                'link': '/br/servicos/seo/',
                'aria': 'Saber mais sobre SEO'
            },
            {
                'icon': 'browser',
                'title': 'Criação de Sites',
                'desc': 'Criamos sites profissionais, modernos e responsivos, desenvolvidos para apresentar a sua empresa de forma clara, transmitir confiança e fortalecer a sua presença digital.',
                'link': '/br/servicos/criacao-de-sites/',
                'aria': 'Saber mais sobre Criação de Sites'
            },
            {
                'icon': 'traffic',
                'title': 'Tráfego Pago',
                'desc': 'Planejamos campanhas de tráfego pago em plataformas como Google Ads e redes sociais, conectando anúncios, páginas de destino e objetivos comerciais para alcançar públicos relevantes.',
                'link': '/br/servicos/trafego-pago/',
                'aria': 'Saber mais sobre Tráfego Pago'
            },
            {
                'icon': 'code',
                'title': 'Criação de Sistemas',
                'desc': 'Desenvolvemos soluções digitais sob medida para as necessidades de cada empresa, desde websites e ferramentas internas até sistemas personalizados que ajudam a simplificar processos.',
                'link': '/br/servicos/sistemas/',
                'aria': 'Saber mais sobre Criação de Sistemas'
            },
            {
                'icon': 'store',
                'title': 'Google Meu Negócio',
                'desc': 'Ajudamos empresas a melhorar sua presença local no Google, organizando informações importantes do negócio e facilitando que potenciais clientes encontrem seus serviços.',
                'link': '/br/servicos/google-meu-negocio/',
                'aria': 'Saber mais sobre Google Meu Negócio'
            }
        ],
        'process_kicker': 'COMO TRABALHAMOS',
        'process_title': 'Do planejamento à entrega,<br>com foco em <span class="process-title-highlight">resultados.</span>',
        'process_intro': 'Cada projeto começa com uma compreensão clara do negócio, do público e dos objetivos. A partir daí, estruturamos cada etapa para criar uma solução digital coerente, funcional e alinhada com a realidade da empresa.',
        'process_steps': [
            ('Descoberta', 'Conhecemos o seu negócio, os seus serviços, o público que pretende alcançar e os objetivos que pretende atingir com a sua presença digital.'),
            ('Planejamento', 'Definimos a estrutura do projeto, organizamos o conteúdo e estabelecemos uma estratégia clara para que o website tenha uma navegação simples e uma comunicação eficiente.'),
            ('Desenvolvimento', 'Transformamos a estratégia em uma experiência digital com design responsivo, tecnologia adequada, boa performance e uma estrutura preparada para mecanismos de busca.'),
            ('Entrega e suporte', 'Publicamos o projeto e acompanhamos os próximos passos, permitindo que o website continue a evoluir conforme as necessidades do negócio.')
        ],
        'faq_kicker': 'PERGUNTAS FREQUENTES',
        'faq_title': 'Tire suas <span class="faq-title-highlight">dúvidas.</span>',
        'faq_intro': 'Reunimos aqui as principais respostas sobre a criação de sites e soluções digitais da Magnani UP®. Se desejar saber mais, entre em contato com nossa equipe.',
        'faq_items': [
            {
                'q': 'Quanto tempo demora para o site ficar pronto?',
                'a': 'O prazo depende da dimensão do projeto, da quantidade de páginas e dos materiais necessários. Depois de conhecermos os objetivos da empresa e a estrutura do website, definimos um prazo adequado para o desenvolvimento.'
            },
            {
                'q': 'O que está incluído na criação de sites?',
                'a': 'A criação de sites envolve a definição da estrutura, organização do conteúdo, design, desenvolvimento responsivo e implementação das funcionalidades necessárias para apresentar a empresa de forma profissional. Cada website é estruturado de acordo com os objetivos e necessidades do projeto.'
            },
            {
                'q': 'Qual é o investimento em tráfego pago?',
                'a': 'O investimento depende dos objetivos da campanha, do mercado, do público e das plataformas utilizadas. O orçamento de mídia é definido separadamente do trabalho de gestão das campanhas.'
            },
            {
                'q': 'Desenvolvem sistemas sob medida?',
                'a': 'Sim. Desenvolvemos soluções digitais personalizadas de acordo com as necessidades de cada empresa, desde websites e ferramentas específicas até sistemas que ajudam a organizar e automatizar processos.'
            },
            {
                'q': 'Como funciona o processo de contratação?',
                'a': 'O processo começa com uma conversa para compreender o negócio, os objetivos e o que precisa de ser desenvolvido. Depois analisamos o projeto, definimos o escopo e apresentamos uma proposta adequada às necessidades identificadas.'
            }
        ],
        'cta_title': 'Seu projeto digital começa<br>com uma <span class="cta-title-highlight">conversa.</span>',
        'cta_desc': 'Conte-nos sobre o seu negócio, os seus objetivos e o que pretende melhorar na sua presença digital. A partir daí, podemos identificar a solução mais adequada para o seu projeto.',
        'cta_btn_text': 'Falar com a equipe &rarr;',
        'footer_desc': 'A Magnani UP® desenvolve sites profissionais e soluções digitais para empresas que buscam construir uma presença online clara, moderna e preparada para crescer.',
        'footer_sub': 'Criação de sites, soluções digitais e estratégias para empresas que querem fortalecer a sua presença online.',
        'footer_serv_links': [
            ('/br/servicos/seo/', 'SEO'),
            ('/br/servicos/criacao-de-sites/', 'Criação de Sites'),
            ('/br/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/br/servicos/sistemas/', 'Criação de Sistemas'),
            ('/br/servicos/google-meu-negocio/', 'Google Meu Negócio')
        ],
        'wa_link': 'https://wa.me/5544998018242',
        'lang_code': 'br'
    },
    'it': {
        'file_path': 'it/index.html',
        'backup_path': '.backup/it_index.html',
        'title': 'Creazione Siti Web e Soluzioni Digitali | Magnani UP®',
        'meta_desc': 'Creazione siti web professionali, SEO, traffico a pagamento, sviluppo di sistemi e soluzioni digitali su misura per aziende.',
        'canonical': 'https://dominio.com/it/',
        'og_locale': 'it_IT',
        'og_alt': 'Magnani UP® - Agenzia Digitale e Creazione Siti Web in Italia',
        'kicker_text': 'AGENZIA DIGITALE &bull; CREAZIONE SITI WEB E SOLUZIONI DIGITALI',
        'hero_desc': 'In Magnani UP®, sviluppiamo siti web professionali, veloci e reattivi per aziende che desiderano rafforzare la propria presenza digitale, valorizzare i propri servizi e trasformare il sito web in un vero punto di contatto con i clienti.',
        'b1_title': 'Siti veloci e pronti per i motori di ricerca',
        'b1_desc': 'Struttura tecnica pensata per facilitare la navigazione, il caricamento e la comprensione dei contenuti da parte dei motori di ricerca.',
        'b2_title': 'Design reattivo su tutti i dispositivi',
        'b2_desc': 'Un\'esperienza coerente su computer, tablet e smartphone, con focus su usabilità e conversione.',
        'b3_title': 'Supporto in tutte le fasi',
        'b3_desc': 'Affiancamento dalla pianificazione e sviluppo fino alla pubblicazione ed evoluzione del progetto.',
        'services_kicker': 'I NOSTRI SERVIZI',
        'services_title': 'Soluzioni complete per<br><span class="services-title-highlight">la tua crescita digitale.</span>',
        'services_intro': 'Dalla creazione di siti web e sviluppo di soluzioni digitali alla SEO, traffico a pagamento e visibilità locale, uniamo diverse competenze per aiutare le aziende a costruire una presenza online professionale, chiara e pronta a crescere.',
        'service_cards': [
            {
                'icon': 'search',
                'title': 'SEO',
                'desc': 'Ottimizziamo la struttura, i contenuti e l\'esperienza del tuo sito web per agevolare l\'indicizzazione da parte dei motori di ricerca e aumentare le opportunità di trovare clienti tramite la ricerca organica.',
                'link': '/it/servizi/seo/',
                'aria': 'Scopri di più sulla SEO'
            },
            {
                'icon': 'browser',
                'title': 'Creazione di Siti Web',
                'desc': 'Sviluppiamo siti web professionali, moderni e reattivi, progettati per presentare la tua azienda con chiarezza, trasmettere affidabilità e consolidare la presenza digitale.',
                'link': '/it/servizi/creazione-siti-web/',
                'aria': 'Scopri di più sulla Creazione di Siti Web'
            },
            {
                'icon': 'traffic',
                'title': 'Traffico a Pagamento',
                'desc': 'Pianifichiamo campagne di traffico a pagamento su piattaforme come Google Ads e social network, collegando annunci, landing page e obiettivi commerciali per raggiungere pubblici mirati.',
                'link': '/it/servizi/traffico-a-pagamento/',
                'aria': 'Scopri di più sul Traffico a Pagamento'
            },
            {
                'icon': 'code',
                'title': 'Sviluppo di Sistemi',
                'desc': 'Sviluppiamo soluzioni digitali su misura per le esigenze di ogni azienda, da strumenti interni a sistemi personalizzati che aiutano a semplificare i processi operativi.',
                'link': '/it/servizi/sistemi/',
                'aria': 'Scopri di più sullo Sviluppo di Sistemi'
            },
            {
                'icon': 'store',
                'title': 'Google Business Profile',
                'desc': 'Aiutiamo le aziende a migliorare la propria visibilità locale su Google, organizzando le informazioni aziendali chiave e facilitando la scoperta dei servizi da parte dei potenziali clienti.',
                'link': '/it/servizi/google-business-profile/',
                'aria': 'Scopri di più su Google Business Profile'
            }
        ],
        'process_kicker': 'COME LAVORIAMO',
        'process_title': 'Dalla pianificazione alla consegna,<br>con focus sui <span class="process-title-highlight">risultati.</span>',
        'process_intro': 'Ogni progetto inizia con una chiara comprensione dell\'attività, del pubblico e degli obiettivi. Da qui strutturiamo ogni fase per creare una soluzione digitale coerente, funzionale e allineata alle reali esigenze aziendali.',
        'process_steps': [
            ('Scoperta', 'Approfondiamo la tua attività, i tuoi servizi, il pubblico che desideri raggiungere e gli obiettivi che intendi conseguire con la presenza digitale.'),
            ('Pianificazione', 'Definiamo la struttura del progetto, organizziamo i contenuti e impostiamo una strategia chiara affinché il sito web garantisca una navigazione semplice e una comunicazione efficace.'),
            ('Sviluppo', 'Trasformiamo la strategia in un\'esperienza digitale con design reattivo, tecnologia idonea, prestazioni elevate e una struttura ottimizzata per i motori di ricerca.'),
            ('Consegna e supporto', 'Pubblichiamo il progetto e seguiamo le fasi successive, consentendo al sito web di continuare a evolversi in base alle esigenze del business.')
        ],
        'faq_kicker': 'DOMANDE FREQUENTI',
        'faq_title': 'Rispondiamo alle tue <span class="faq-title-highlight">domande.</span>',
        'faq_intro': 'Abbiamo raccolto qui le risposte principali sui nostri servizi di creazione siti web e soluzioni digitali. Per maggiori dettagli, contatta il nostro team.',
        'faq_items': [
            {
                'q': 'Quanto tempo ci vuole per completare il sito web?',
                'a': 'I tempi dipendono dalle dimensioni del progetto, dal numero di pagine e dai materiali necessari. Dopo aver compreso gli obiettivi aziendali e la struttura del sito web, stabiliamo tempistiche adeguate per lo sviluppo.'
            },
            {
                'q': 'Cosa comprende la creazione di siti web?',
                'a': 'La creazione di siti web comprende la progettazione della struttura, l\'organizzazione dei contenuti, il web design, lo sviluppo reattivo e l\'implementazione delle funzionalità necessarie per valorizzare l\'azienda. Ogni sito web è sviluppato in funzione degli obiettivi e dei requisiti del progetto.'
            },
            {
                'q': 'Qual è l\'investimento richiesto per il traffico a pagamento?',
                'a': 'L\'investimento dipende dagli obiettivi della campagna, dal settore di mercato, dal target e dalle piattaforme impiegate. Il budget pubblicitario viene stabilito separatamente rispetto alla gestione operativa delle campagne.'
            },
            {
                'q': 'Sviluppate sistemi personalizzati su misura?',
                'a': 'Sì. Sviluppiamo soluzioni digitali personalizzate in base alle esigenze di ogni azienda, da strumenti specifici a sistemi gestionali che aiutano a organizzare e automatizzare le procedure.'
            },
            {
                'q': 'Come funziona il processo di contrattazione e avvio?',
                'a': 'Il processo comincia con un confronto per comprendere l\'attività, gli obiettivi e ciò che deve essere sviluppato. Successivamente esaminiamo il progetto, definiamo l\'ambito di lavoro e presentiamo una proposta su misura.'
            }
        ],
        'cta_title': 'Il tuo progetto digitale inizia<br>con una <span class="cta-title-highlight">conversazione.</span>',
        'cta_desc': 'Raccontaci della tua azienda, dei tuoi obiettivi e di cosa desideri migliorare nella presenza digitale. Insieme possiamo individuare la soluzione più idonea per il tuo progetto.',
        'cta_btn_text': 'Parla con il team &rarr;',
        'footer_desc': 'Magnani UP® sviluppa siti web professionali e soluzioni digitali per aziende che desiderano costruire una presenza online chiara, moderna e pronta a crescere.',
        'footer_sub': 'Creazione di siti web, soluzioni digitali e strategie per aziende che desiderano rafforzare la presenza online.',
        'footer_serv_links': [
            ('/it/servizi/seo/', 'SEO'),
            ('/it/servizi/creazione-siti-web/', 'Creazione di Siti Web'),
            ('/it/servizi/traffico-a-pagamento/', 'Traffico a Pagamento'),
            ('/it/servizi/sistemi/', 'Sviluppo di Sistemi'),
            ('/it/servizi/google-business-profile/', 'Google Business Profile')
        ],
        'wa_link': 'https://wa.me/393313882760',
        'lang_code': 'it'
    }
}

def update_home_file(cfg):
    file_path = cfg['file_path']
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title, meta, canonical
    content = re.sub(r'<title>.*?</title>', f'<title>{cfg["title"]}</title>', content)
    content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']>', f'<meta name="description" content="{cfg["meta_desc"]}">', content)
    content = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\'].*?["\']>', f'<link rel="canonical" href="{cfg["canonical"]}">', content)

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
            "description": cfg["meta_desc"],
            "sameAs": [
                "https://instagram.com",
                "https://linkedin.com"
            ],
            "contactPoint": {
                "@type": "ContactPoint",
                "telephone": cfg["wa_link"].replace("https://wa.me/", "+"),
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
            "inLanguage": cfg["lang_code"] if cfg["lang_code"] == 'it' else f"pt-{cfg['lang_code'].upper()}"
        },
        {
            "@type": "WebPage",
            "@id": f"{cfg['canonical']}#webpage",
            "url": cfg["canonical"],
            "name": cfg["title"],
            "description": cfg["meta_desc"],
            "isPartOf": {
                "@id": "https://dominio.com/#website"
            },
            "inLanguage": cfg["lang_code"] if cfg["lang_code"] == 'it' else f"pt-{cfg['lang_code'].upper()}",
            "about": {
                "@id": "https://dominio.com/#organization"
            }
        },
        {
            "@type": "FAQPage",
            "@id": f"{cfg['canonical']}#faq",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": item["q"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": item["a"]
                    }
                } for item in cfg["faq_items"]
            ]
        }
    ]

    schema_json = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, indent=2, ensure_ascii=False)
    new_schema_tag = f'''  <!-- Schema.org Internacionalizado (Organization, WebSite, WebPage, FAQPage) -->
  <script type="application/ld+json">
{schema_json}
  </script>'''
    content = re.sub(r'<!-- Schema\.org.*?-->\s*<script type="application/ld\+json">.*?</script>', new_schema_tag, content, flags=re.DOTALL)

    # Hero Kicker & Description
    content = re.sub(r'<span class="kicker-text">.*?</span>', f'<span class="kicker-text">{cfg["kicker_text"]}</span>', content)
    content = re.sub(r'<p class="hero-description">.*?</p>', f'<p class="hero-description">\n                {cfg["hero_desc"]}\n              </p>', content, flags=re.DOTALL)

    # Benefits section
    benefits_html = f'''              <!-- Bloco 1: Alvo / Buscadores -->
              <li class="benefits-item">
                <div class="benefits-icon-badge" aria-hidden="true">
                  <svg class="benefits-svg-icon" viewBox="0 0 28 28" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                    <circle cx="13" cy="15" r="8" stroke="#ffffff" stroke-width="1.9"/>
                    <circle cx="13" cy="15" r="4.5" stroke="#ffffff" stroke-width="1.8"/>
                    <circle cx="13" cy="15" r="1.4" fill="#ffffff" stroke="none"/>
                    <path d="M17 11L24 4" stroke="#ffffff" stroke-width="2"/>
                    <path d="M20 4H24V8" stroke="#ffffff" stroke-width="2"/>
                  </svg>
                </div>
                <div class="benefits-text">
                  <span class="benefits-text-title">{cfg["b1_title"]}</span>
                  <span class="benefits-text-desc">{cfg["b1_desc"]}</span>
                </div>
              </li>

              <!-- Divisória Vertical 1 -->
              <li class="benefits-divider" aria-hidden="true"></li>

              <!-- Bloco 2: Dispositivo / Design Responsivo -->
              <li class="benefits-item">
                <div class="benefits-icon-badge" aria-hidden="true">
                  <svg class="benefits-svg-icon" viewBox="0 0 28 28" fill="none" stroke="#ffffff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                    <rect x="3" y="4" width="22" height="17" rx="3" stroke="#ffffff" stroke-width="1.9"/>
                    <line x1="3" y1="9.5" x2="25" y2="9.5" stroke="#ffffff" stroke-width="1.5" opacity="0.7"/>
                    <rect x="15" y="12" width="7" height="9" rx="1.5" fill="#1e295d" stroke="#a78bfa" stroke-width="1.6"/>
                    <circle cx="18.5" cy="19.2" r="0.6" fill="#ffffff" stroke="none"/>
                  </svg>
                </div>
                <div class="benefits-text">
                  <span class="benefits-text-title">{cfg["b2_title"]}</span>
                  <span class="benefits-text-desc">{cfg["b2_desc"]}</span>
                </div>
              </li>

              <!-- Divisória Vertical 2 -->
              <li class="benefits-divider" aria-hidden="true"></li>

              <!-- Bloco 3: Escudo / Suporte -->
              <li class="benefits-item">
                <div class="benefits-icon-badge" aria-hidden="true">
                  <svg class="benefits-svg-icon" viewBox="0 0 28 28" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                    <path d="M14 3.5L5 7.5V13.5C5 19.2 8.8 24.3 14 25.5C19.2 24.3 23 19.2 23 13.5V7.5L14 3.5Z" stroke="#ffffff" stroke-width="1.9" stroke-linejoin="round"/>
                    <path d="M9.5 14L12.5 17L18.5 11" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </div>
                <div class="benefits-text">
                  <span class="benefits-text-title">{cfg["b3_title"]}</span>
                  <span class="benefits-text-desc">{cfg["b3_desc"]}</span>
                </div>
              </li>'''
    content = re.sub(r'<ul class="benefits-list">.*?</ul>', f'<ul class="benefits-list">\n{benefits_html}\n            </ul>', content, flags=re.DOTALL)

    # Services Header Kicker, Title & Intro
    content = re.sub(r'<span class="services-tag-text">.*?</span>', f'<span class="services-tag-text">{cfg["services_kicker"]}</span>', content)
    content = re.sub(r'<h2 class="services-title"[^>]*>.*?</h2>', f'<h2 class="services-title" id="services-title">\n                {cfg["services_title"]}\n              </h2>', content, flags=re.DOTALL)
    content = re.sub(r'<div class="services-header-right">.*?</div>', f'<div class="services-header-right">\n              <p class="services-intro-text">\n                {cfg["services_intro"]}\n              </p>\n            </div>', content, flags=re.DOTALL)

    # 5 Service Cards in Order: SEO, Criação de Sites, Tráfego Pago, Criação de Sistemas, Google Meu Negócio
    cards_html_list = []
    for idx, c in enumerate(cfg["service_cards"], 1):
        icon_svg = ICONS[c['icon']]
        card_html = f'''            <!-- Card 0{idx}: {c["title"]} -->
            <article class="service-card">
              <div class="service-card-content">
                <div class="service-icon-badge" aria-hidden="true">
                  {icon_svg}
                </div>
                <h3 class="service-card-title">{c["title"]}</h3>
                <p class="service-card-desc">
                  {c["desc"]}
                </p>
              </div>
              <a href="{c["link"]}" class="service-card-btn" aria-label="{c["aria"]}">
                <svg class="service-btn-arrow" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                  <path d="M3 8H13M13 8L8.5 3.5M13 8L8.5 12.5"/>
                </svg>
              </a>
            </article>'''
        cards_html_list.append(card_html)

    services_grid_html = "\n\n".join(cards_html_list)
    content = re.sub(r'<div class="services-cards-grid">.*?</div>\s*</div>\s*</section>',
                     f'<div class="services-cards-grid">\n\n{services_grid_html}\n\n          </div>\n        </div>\n      </section>',
                     content, flags=re.DOTALL)

    # Process Kicker, Title & Intro
    content = re.sub(r'<span class="process-tag-text">.*?</span>', f'<span class="process-tag-text">{cfg["process_kicker"]}</span>', content)
    content = re.sub(r'<h2 class="process-title"[^>]*>.*?</h2>', f'<h2 class="process-title" id="process-title">\n                {cfg["process_title"]}\n              </h2>', content, flags=re.DOTALL)
    content = re.sub(r'<div class="process-header-right">.*?</div>', f'<div class="process-header-right">\n              <p class="process-intro-text">\n                {cfg["process_intro"]}\n              </p>\n            </div>', content, flags=re.DOTALL)

    # Process Steps
    p_steps = cfg["process_steps"]
    step_icons = [
        '''<svg class="process-svg-icon" viewBox="0 0 28 28" fill="none" stroke="#ffffff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                  <path d="M14 4C9.58 4 6 7.58 6 12C6 14.8 7.4 17.2 9.6 18.6V20.5C9.6 21.3 10.3 22 11.1 22H16.9C17.7 22 18.4 21.3 18.4 20.5V18.6C20.6 17.2 22 14.8 22 12C22 7.58 18.42 4 14 4Z"/>
                  <path d="M11 25H17" stroke="#a78bfa" stroke-width="1.8"/>
                  <path d="M12 18H16" stroke="#a78bfa" stroke-width="1.6"/>
                  <path d="M14 10V14" stroke="#ffffff" stroke-width="1.6"/>
                </svg>''',
        '''<svg class="process-svg-icon" viewBox="0 0 28 28" fill="none" stroke="#ffffff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                  <rect x="4" y="4" width="15" height="12" rx="2.5" stroke="#a78bfa" stroke-width="1.7" opacity="0.75"/>
                  <rect x="9" y="9" width="15" height="15" rx="2.5" stroke="#ffffff" stroke-width="1.9" fill="#161e56"/>
                  <line x1="9" y1="14" x2="24" y2="14" stroke="#a78bfa" stroke-width="1.5"/>
                  <rect x="12" y="16.5" width="4.5" height="4.5" rx="1" stroke="#ffffff" stroke-width="1.3"/>
                  <line x1="19" y1="17" x2="22" y2="17" stroke="#ffffff" stroke-width="1.3"/>
                  <line x1="19" y1="20" x2="22" y2="20" stroke="#ffffff" stroke-width="1.3"/>
                </svg>''',
        '''<svg class="process-svg-icon" viewBox="0 0 28 28" fill="none" stroke="#ffffff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                  <path d="M12.2 4.2C12.5 3.5 13.2 3 14 3C14.8 3 15.5 3.5 15.8 4.2L16.2 5.2C16.8 5.4 17.4 5.8 17.9 6.2L18.9 5.8C19.7 5.5 20.6 5.8 21.1 6.5C21.6 7.2 21.6 8.1 21.1 8.8L20.5 9.6C20.8 10.2 21.1 10.9 21.2 11.6L22.2 11.9C23 12.2 23.6 12.9 23.6 13.7C23.6 14.5 23 15.2 22.2 15.5L21.2 15.8C21.1 16.5 20.8 17.2 20.5 17.8L21.1 18.6C21.6 19.3 21.6 20.2 21.1 20.9C20.6 21.6 19.7 21.9 18.9 21.6L17.9 21.2C17.4 21.6 16.8 22 16.2 22.2L15.8 23.2C15.5 23.9 14.8 24.4 14 24.4C13.2 24.4 12.5 23.9 12.2 23.2L11.8 22.2C11.2 22 10.6 21.6 10.1 21.2L9.1 21.6C8.3 21.9 7.4 21.6 6.9 20.9C6.4 20.2 6.4 19.3 6.9 18.6L7.5 17.8C7.2 17.2 6.9 16.5 6.8 15.8L5.8 15.5C5 15.2 4.4 14.5 4.4 13.7C4.4 12.9 5 12.2 5.8 11.9L6.8 11.6C6.9 10.9 7.2 10.2 7.5 9.6L6.9 8.8C6.4 8.1 6.4 7.2 6.9 6.5C7.4 5.8 8.3 5.5 9.1 5.8L10.1 6.2C10.6 5.8 11.2 5.4 11.8 5.2L12.2 4.2Z" stroke="#ffffff" stroke-width="1.8"/>
                  <circle cx="14" cy="13.7" r="3.4" stroke="#a78bfa" stroke-width="1.8"/>
                </svg>''',
        '''<svg class="process-svg-icon" viewBox="0 0 28 28" fill="none" stroke="#ffffff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                  <rect x="5.5" y="16" width="4.5" height="8" rx="1.5" fill="#1e295d" stroke="#a78bfa" stroke-width="1.8"/>
                  <rect x="12" y="11" width="4.5" height="13" rx="1.5" fill="#223275" stroke="#ffffff" stroke-width="1.8"/>
                  <rect x="18.5" y="6" width="4.5" height="18" rx="1.5" fill="#2b3f94" stroke="#a78bfa" stroke-width="1.8"/>
                </svg>'''
    ]
    connector_html = '''            <!-- Seta Conectora -->
            <li class="process-flow-connector" aria-hidden="true">
              <svg class="process-arrow-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                <path d="M6 3.5L10.5 8L6 12.5"/>
              </svg>
            </li>'''

    flow_items = []
    for idx, (stitle, sdesc) in enumerate(p_steps):
        flow_items.append(f'''            <!-- Etapa 0{idx+1}: {stitle} -->
            <li class="process-step-item">
              <div class="process-icon-badge" aria-hidden="true">
                {step_icons[idx]}
              </div>
              <h3 class="process-step-title">{stitle}</h3>
              <p class="process-step-desc">
                {sdesc}
              </p>
            </li>''')
        if idx < len(p_steps) - 1:
            flow_items.append(connector_html)

    flow_list_html = "\n\n".join(flow_items)
    content = re.sub(r'<ol class="process-flow-list">.*?</ol>', f'<ol class="process-flow-list">\n{flow_list_html}\n          </ol>', content, flags=re.DOTALL)

    # FAQ Accordion
    content = re.sub(r'<span class="faq-tag-text">.*?</span>', f'<span class="faq-tag-text">{cfg["faq_kicker"]}</span>', content)
    content = re.sub(r'<h2 class="faq-title"[^>]*>.*?</h2>', f'<h2 class="faq-title" id="faq-title">\n                {cfg["faq_title"]}\n              </h2>', content, flags=re.DOTALL)
    content = re.sub(r'<div class="faq-header-right">\s*<p class="faq-intro-text">.*?</p>\s*</div>',
                     f'<div class="faq-header-right">\n              <p class="faq-intro-text">\n                {cfg["faq_intro"]}\n              </p>\n            </div>', content, flags=re.DOTALL)

    faq_html_list = []
    for idx, fitem in enumerate(cfg["faq_items"], 1):
        faq_html_list.append(f'''            <!-- Pergunta 0{idx} -->
            <div class="faq-item">
              <button type="button" 
                      class="faq-question-btn" 
                      id="faq-btn-{idx}" 
                      aria-expanded="false" 
                      aria-controls="faq-ans-{idx}">
                <span class="faq-question-left">
                  <span class="faq-num-badge" aria-hidden="true">0{idx}</span>
                  <span class="faq-question-text">{fitem["q"]}</span>
                </span>
                <svg class="faq-chevron-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                  <path d="M3.5 6L8 10.5L12.5 6"/>
                </svg>
              </button>
              <div class="faq-answer-panel" id="faq-ans-{idx}" role="region" aria-labelledby="faq-btn-{idx}">
                <div class="faq-answer-inner">
                  <div class="faq-answer-content">
                    <p class="faq-answer-text">
                      {fitem["a"]}
                    </p>
                  </div>
                </div>
              </div>
            </div>''')

    faq_accordion_html = "\n\n".join(faq_html_list)
    content = re.sub(r'<div class="faq-accordion-list"[^>]*>.*?</div>\s*</div>\s*</section>',
                     f'<div class="faq-accordion-list" role="region" aria-label="Lista de perguntas frequentes">\n\n{faq_accordion_html}\n\n          </div>\n        </div>\n      </section>',
                     content, flags=re.DOTALL)

    # CTA Section
    content = re.sub(r'<h2 class="cta-title"[^>]*>.*?</h2>', f'<h2 class="cta-title" id="cta-title">\n                  {cfg["cta_title"]}\n                </h2>', content, flags=re.DOTALL)
    content = re.sub(r'<p class="cta-desc">.*?</p>', f'<p class="cta-desc">\n                {cfg["cta_desc"]}\n              </p>', content, flags=re.DOTALL)
    content = re.sub(r'<a href="https://wa\.me/[0-9]+"[^>]*class="cta-btn">\s*<span>.*?</span>',
                     f'<a href="{cfg["wa_link"]}" target="_blank" rel="noopener noreferrer" class="cta-btn">\n                  <span>{cfg["cta_btn_text"]}</span>', content)

    # Footer Section
    content = re.sub(r'<p class="footer-institutional-desc">.*?</p>',
                     f'<p class="footer-institutional-desc">\n              {cfg["footer_desc"]}<br><br>\n              <span class="footer-sub-highlight" style="opacity: 0.85; font-size: 0.875rem;">{cfg["footer_sub"]}</span>\n            </p>',
                     content, flags=re.DOTALL)

    footer_links_html = "".join([f'          <li><a href="{href}" class="footer-link">{label}</a></li>\n' for href, label in cfg["footer_serv_links"]])
    footer_col3_regex = r'(<nav class="footer-col" aria-label="[^"]*">\s*<h3 class="footer-col-title">[^<]*</h3>\s*<ul class="footer-links-list">)(.*?)(</ul>\s*</nav>)'
    matches = list(re.finditer(footer_col3_regex, content, re.DOTALL))
    if len(matches) >= 2:
        m = matches[1] # second nav is Serviços
        replacement = m.group(1) + "\n" + footer_links_html + "        " + m.group(3)
        content = content[:m.start()] + replacement + content[m.end():]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(cfg['backup_path'], 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path} and backup {cfg['backup_path']}")

# Run on pt, br, it
for lang in ['pt', 'br', 'it']:
    update_home_file(CONFIGS[lang])

# Update root index.html
with open('index.html', 'r', encoding='utf-8') as f:
    root_html = f.read()

cfg_pt = CONFIGS['pt']
root_html = re.sub(r'<p class="hero-description">.*?</p>', f'<p class="hero-description">\n                {cfg_pt["hero_desc"]}\n              </p>', root_html, flags=re.DOTALL)
root_html = re.sub(r'<p class="cta-desc">.*?</p>', f'<p class="cta-desc">\n                {cfg_pt["cta_desc"]}\n              </p>', root_html, flags=re.DOTALL)
root_html = re.sub(r'<p class="footer-institutional-desc">.*?</p>',
                   f'<p class="footer-institutional-desc">\n              {cfg_pt["footer_desc"]}<br><br>\n              <span class="footer-sub-highlight" style="opacity: 0.85; font-size: 0.875rem;">{cfg_pt["footer_sub"]}</span>\n            </p>',
                   root_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(root_html)
with open('.backup/root_index.html', 'w', encoding='utf-8') as f:
    f.write(root_html)
print("Updated index.html and backup.")

print("=== PROMPT FINAL Implementation Finished Successfully ===")
