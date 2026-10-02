import re
import json
import os

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

pt_footer_desc = "A Magnani UP® desenvolve websites profissionais e soluções digitais para empresas que procuram construir uma presença online clara, moderna e preparada para crescer. Da criação de websites ao desenvolvimento de sistemas personalizados, trabalhamos diferentes áreas do digital para ajudar empresas a apresentar melhor os seus serviços e fortalecer a sua presença online."
br_footer_desc = "A Magnani UP® desenvolve sites profissionais e soluções digitais para empresas que buscam construir uma presença online clara, moderna e preparada para crescer. Da criação de sites ao desenvolvimento de sistemas personalizados, atuamos em múltiplas áreas do digital para ajudar empresas a apresentar melhor seus serviços e fortalecer sua presença online."
it_footer_desc = "Magnani UP® sviluppa siti web professionali e soluzioni digitali per aziende che desiderano costruire una presenza online chiara, moderna e orientata alla crescita. Dalla realizzazione di siti web allo sviluppo di software personalizzati, operiamo nelle principali aree del digitale per valorizzare la tua impresa sul mercato."

CONFIGS = {
    'pt': {
        'file_path': 'pt/index.html',
        'backup_path': '.backup/pt_index.html',
        'title': 'Criação de Sites e Soluções Digitais em Portugal | Magnani UP®',
        'meta_desc': 'Criação de websites profissionais, SEO, landing pages, tráfego pago e soluções digitais para empresas que pretendem fortalecer a sua presença online em Portugal.',
        'canonical': 'https://dominio.com/pt/',
        'og_locale': 'pt_PT',
        'og_alt': 'Magnani UP® - Agência Digital e Criação de Websites em Portugal',
        'hero_desc': 'Na Magnani UP®, criamos websites profissionais, rápidos e responsivos para empresas que querem fortalecer a sua presença digital, apresentar melhor os seus serviços e transformar o website num verdadeiro ponto de contacto com os seus clientes. Cada projeto combina estratégia, design e desenvolvimento web para criar uma experiência clara, moderna e alinhada aos objetivos do negócio.',
        'b1_title': 'Sites rápidos e preparados para pesquisa',
        'b1_desc': 'Estruturamos cada website pensando no desempenho, na organização do conteúdo e na facilidade de navegação. Uma boa base técnica contribui para uma experiência mais fluida para o utilizador e facilita a compreensão das páginas pelos motores de busca.',
        'b2_title': 'Design responsivo em todos os dispositivos',
        'b2_desc': 'O desenvolvimento considera diferentes tamanhos de ecrã para que o site funcione de forma consistente em computadores, tablets e smartphones. O resultado é uma experiência digital adaptada ao comportamento dos utilizadores atuais.',
        'b3_title': 'Suporte em todas as etapas',
        'b3_desc': 'Do planeamento inicial à publicação do website, acompanhamos as diferentes etapas do projeto. A nossa abordagem procura garantir que estrutura, conteúdo, design e tecnologia estejam alinhados com as necessidades da empresa.',
        'services_intro': [
            'Uma presença digital profissional vai muito além de ter um website online. É necessário apresentar a empresa de forma clara, facilitar o contacto com potenciais clientes, construir confiança e criar uma experiência coerente em diferentes canais.',
            'Na Magnani UP®, reunimos criação de sites, desenvolvimento de soluções digitais, SEO, tráfego pago e estratégias de presença local para ajudar empresas a estruturar melhor a sua comunicação online.',
            'Cada projeto é analisado de acordo com a realidade do negócio, permitindo definir as ferramentas, tecnologias e estratégias mais adequadas para os seus objetivos.'
        ],
        'service_cards': [
            {
                'icon': 'browser',
                'title': 'Criação de Websites',
                'desc': 'A criação de sites envolve muito mais do que desenvolver uma página visualmente atrativa. Um website profissional precisa apresentar os serviços de forma clara, facilitar a navegação, funcionar corretamente em diferentes dispositivos e transmitir confiança desde o primeiro contacto. Desenvolvemos websites pensados para representar a identidade de cada empresa e criar uma base sólida para a sua presença digital.',
                'link': '/pt/servicos/criacao-de-sites/',
                'aria': 'Saber mais sobre Criação de Websites'
            },
            {
                'icon': 'search',
                'title': 'SEO',
                'desc': 'Uma boa estratégia de SEO começa na própria estrutura do website. Organização das páginas, conteúdo relevante, arquitetura de informação, desempenho técnico e experiência do utilizador são elementos que ajudam os motores de busca a compreender melhor um projeto digital. Na Magnani UP®, trabalhamos esses elementos de forma integrada para criar uma base mais sólida para a pesquisa orgânica.',
                'link': '/pt/servicos/seo/',
                'aria': 'Saber mais sobre SEO'
            },
            {
                'icon': 'traffic',
                'title': 'Tráfego Pago',
                'desc': 'O tráfego pago permite apresentar anúncios a públicos definidos de acordo com diferentes objetivos comerciais. A estratégia pode envolver Google Ads, redes sociais, páginas de destino e diferentes formatos de campanha. O trabalho deve considerar não apenas o anúncio, mas também o percurso que o utilizador realiza depois do clique, desde a página de destino até ao contacto ou ação pretendida.',
                'link': '/pt/servicos/trafego-pago/',
                'aria': 'Saber mais sobre Tráfego Pago'
            },
            {
                'icon': 'code',
                'title': 'Criação de Sistemas',
                'desc': 'Nem todas as necessidades de uma empresa podem ser resolvidas através de um website institucional. Em alguns projetos, é necessário desenvolver ferramentas específicas para organizar informações, automatizar tarefas ou melhorar determinados processos internos. Por isso, desenvolvemos soluções digitais e sistemas personalizados de acordo com as necessidades identificadas em cada projeto.',
                'link': '/pt/servicos/sistemas/',
                'aria': 'Saber mais sobre Criação de Sistemas'
            },
            {
                'icon': 'store',
                'title': 'Google Perfil de Empresa',
                'desc': 'Para empresas que dependem de clientes de uma determinada região, a presença local pode desempenhar um papel importante na descoberta dos seus serviços. Informações corretas, localização, descrição dos serviços e uma presença organizada no Google ajudam potenciais clientes a compreender melhor o negócio e entrar em contacto.',
                'link': '/pt/servicos/google-meu-negocio/',
                'aria': 'Saber mais sobre Google Perfil de Empresa'
            }
        ],
        'process_intro': [
            'Cada projeto digital possui necessidades diferentes. Por isso, antes de iniciar o desenvolvimento, procuramos compreender o negócio, o público, os serviços oferecidos e os objetivos que a empresa pretende alcançar.',
            'A partir dessas informações, estruturamos o projeto em etapas claras, permitindo que estratégia, conteúdo, design e tecnologia evoluam de forma coordenada.'
        ],
        'process_steps': [
            ('Descoberta', 'Conhecemos o seu negócio, os serviços que oferece, o público que pretende alcançar e os objetivos da sua presença digital. Esta etapa ajuda a definir uma direção clara para o projeto.'),
            ('Planeamento', 'Organizamos a estrutura do website, definimos as páginas necessárias, analisamos o conteúdo e estabelecemos a melhor forma de apresentar as informações. O objetivo é criar uma navegação simples e uma comunicação coerente.'),
            ('Desenvolvimento', 'Transformamos o planeamento em uma experiência digital funcional. Trabalhamos design responsivo, estrutura de páginas, tecnologia, desempenho e elementos necessários para que o website funcione corretamente em diferentes dispositivos.'),
            ('Entrega e suporte', 'Após a conclusão do desenvolvimento, colocamos o projeto online e acompanhamos os próximos passos. O website pode continuar a evoluir à medida que surgem novas necessidades, serviços ou objetivos para a empresa.')
        ],
        'faq_items': [
            {
                'q': 'Quanto tempo demora para o website ficar pronto?',
                'a': 'O prazo varia de acordo com a dimensão do projeto, o número de páginas, a complexidade das funcionalidades e os materiais disponíveis. Um website institucional com uma estrutura mais simples pode ter um processo diferente de um projeto com várias páginas ou funcionalidades específicas. Depois de compreendermos os objetivos da empresa, analisamos o escopo necessário e definimos um prazo adequado para o desenvolvimento.'
            },
            {
                'q': 'Como funciona a criação de um site?',
                'a': 'O processo começa com a compreensão do negócio, dos serviços e dos objetivos da empresa. Em seguida, definimos a estrutura do website, organizamos o conteúdo, desenvolvemos o design e implementamos o projeto de forma responsiva. Durante o desenvolvimento, consideramos também aspetos como navegação, desempenho, estrutura das páginas e preparação técnica para pesquisa.'
            },
            {
                'q': 'Qual é o investimento em tráfego pago e quando são utilizadas landing pages?',
                'a': 'O investimento em tráfego pago varia de acordo com os objetivos, público, plataformas e orçamento definido para a campanha. O orçamento pode ser direcionado para Google Ads ou redes sociais. Em determinados projetos de tráfego pago, uma landing page pode ser utilizada como página de destino para uma campanha específica, concentrando a atenção do utilizador e facilitando o contacto.'
            },
            {
                'q': 'Desenvolvem sistemas e ferramentas digitais personalizadas?',
                'a': 'Sim. Nem todas as necessidades de uma empresa podem ser resolvidas através de um website institucional. Em alguns projetos, é necessário desenvolver ferramentas específicas para organizar informações, automatizar tarefas ou melhorar determinados processos internos. Por isso, desenvolvemos soluções digitais e sistemas personalizados de acordo com as necessidades identificadas em cada projeto.'
            },
            {
                'q': 'Como funciona o processo de contratação e início do projeto?',
                'a': 'Após o primeiro contacto, realizamos uma conversa para analisar as necessidades da sua empresa, compreender os serviços pretendidos e avaliar o escopo do projeto. Em seguida, estruturamos uma proposta transparente com prazos, etapas e investimento correspondente. Uma vez aprovada, iniciamos imediatamente a fase de descoberta e planeamento.'
            }
        ],
        'cta_desc': 'Conte-nos sobre o seu negócio, os seus objetivos e o que pretende melhorar na sua presença digital. Podemos analisar as suas necessidades e identificar se o projeto envolve criação de sites, desenvolvimento de soluções digitais, SEO, tráfego pago ou outra necessidade específica.',
        'footer_desc': pt_footer_desc,
        'footer_serv_links': [
            ('/pt/servicos/criacao-de-sites/', 'Criação de Websites'),
            ('/pt/servicos/seo/', 'SEO'),
            ('/pt/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/pt/servicos/sistemas/', 'Criação de Sistemas'),
            ('/pt/servicos/google-meu-negocio/', 'Google Perfil de Empresa')
        ],
        'wa_link': 'https://wa.me/393313882760',
        'lang_code': 'pt'
    },
    'br': {
        'file_path': 'br/index.html',
        'backup_path': '.backup/br_index.html',
        'title': 'Criação de Sites e Soluções Digitais | Magnani UP®',
        'meta_desc': 'Criação de sites profissionais, SEO, landing pages, tráfego pago e soluções digitais para empresas que desejam expandir seus negócios e presença online.',
        'canonical': 'https://dominio.com/br/',
        'og_locale': 'pt_BR',
        'og_alt': 'Magnani UP® - Agência Digital e Criação de Sites no Brasil',
        'hero_desc': 'Na Magnani UP®, criamos sites profissionais, rápidos e responsivos para empresas que querem fortalecer sua presença digital, apresentar melhor seus serviços e transformar o site em um verdadeiro canal de vendas e contato com clientes. Cada projeto combina estratégia, design e desenvolvimento web para criar uma experiência clara, moderna e alinhada aos objetivos do seu negócio.',
        'b1_title': 'Sites rápidos e preparados para busca',
        'b1_desc': 'Estruturamos cada site pensando no desempenho, na organização do conteúdo e na facilidade de navegação. Uma boa base técnica contribui para uma experiência mais fluida para o usuário e facilita a compreensão das páginas pelos mecanismos de busca.',
        'b2_title': 'Design responsivo em todos os dispositivos',
        'b2_desc': 'O desenvolvimento considera diferentes tamanhos de tela para que o site funcione de forma consistente em computadores, tablets e smartphones. O resultado é uma experiência digital adaptada ao comportamento dos usuários atuais.',
        'b3_title': 'Suporte em todas as etapas',
        'b3_desc': 'Do planejamento inicial à publicação do site, acompanhamos as diferentes etapas do projeto. Nossa abordagem procura garantir que estrutura, conteúdo, design e tecnologia estejam alinhados com as necessidades da sua empresa.',
        'services_intro': [
            'Uma presença digital profissional vai muito além de ter um site online. É necessário apresentar a empresa de forma clara, facilitar o contato com potenciais clientes, construir confiança e criar uma experiência coerente em diferentes canais.',
            'Na Magnani UP®, reunimos criação de sites, desenvolvimento de soluções digitais, SEO, tráfego pago e estratégias de presença local para ajudar empresas a estruturar melhor a sua comunicação online.',
            'Cada projeto é analisado de acordo com a realidade do negócio, permitindo definir as ferramentas, tecnologias e estratégias mais adequadas para os seus objetivos.'
        ],
        'service_cards': [
            {
                'icon': 'browser',
                'title': 'Criação de Sites',
                'desc': 'A criação de sites envolve muito mais do que desenvolver uma página visualmente atraente. Um site profissional precisa apresentar os serviços de forma clara, facilitar a navegação, funcionar corretamente em diferentes dispositivos e transmitir confiança desde o primeiro contato. Desenvolvemos sites pensados para representar a identidade de cada empresa e criar uma base sólida para a sua presença digital.',
                'link': '/br/servicos/criacao-de-sites/',
                'aria': 'Saber mais sobre Criação de Sites'
            },
            {
                'icon': 'search',
                'title': 'SEO',
                'desc': 'Uma boa estratégia de SEO começa na própria estrutura do site. Organização das páginas, conteúdo relevante, arquitetura de informação, desempenho técnico e experiência do usuário são elementos que ajudam os mecanismos de busca a compreender melhor um projeto digital. Na Magnani UP®, trabalhamos esses elementos de forma integrada para criar uma base mais sólida para a busca orgânica.',
                'link': '/br/servicos/seo/',
                'aria': 'Saber mais sobre SEO'
            },
            {
                'icon': 'traffic',
                'title': 'Tráfego Pago',
                'desc': 'O tráfego pago permite apresentar anúncios a públicos definidos de acordo com diferentes objetivos comerciais. A estratégia pode envolver Google Ads, redes sociais, páginas de destino e diferentes formatos de campanha. O trabalho deve considerar não apenas o anúncio, mas também o percurso que o usuário realiza após o clique, desde a página de destino até o contato ou ação pretendida.',
                'link': '/br/servicos/trafego-pago/',
                'aria': 'Saber mais sobre Tráfego Pago'
            },
            {
                'icon': 'code',
                'title': 'Desenvolvimento de Sistemas',
                'desc': 'Nem todas as necessidades de uma empresa podem ser resolvidas através de um site institucional. Em alguns projetos, é necessário desenvolver ferramentas específicas para organizar informações, automatizar tarefas ou melhorar determinados processos internos. Por isso, desenvolvemos soluções digitais e sistemas personalizados de acordo com as necessidades identificadas em cada projeto.',
                'link': '/br/servicos/sistemas/',
                'aria': 'Saber mais sobre Desenvolvimento de Sistemas'
            },
            {
                'icon': 'store',
                'title': 'Google Meu Negócio',
                'desc': 'Para empresas que dependem de clientes de uma determinada região, a presença local desempenha um papel fundamental na descoberta dos seus serviços. Informações corretas, localização, descrição dos serviços e presença organizada no Google ajudam potenciais clientes a encontrar sua empresa e solicitar contato.',
                'link': '/br/servicos/google-meu-negocio/',
                'aria': 'Saber mais sobre Google Meu Negócio'
            }
        ],
        'process_intro': [
            'Cada projeto digital possui necessidades diferentes. Por isso, antes de iniciar o desenvolvimento, procuramos compreender o negócio, o público, os serviços oferecidos e os objetivos que a empresa pretende alcançar.',
            'A partir dessas informações, estruturamos o projeto em etapas claras, permitindo que estratégia, conteúdo, design e tecnologia evoluam de forma coordenada.'
        ],
        'process_steps': [
            ('Descoberta', 'Conhecemos o seu negócio, os serviços que oferece, o público que pretende alcançar e os objetivos da sua presença digital. Esta etapa ajuda a definir uma direção clara para o projeto.'),
            ('Planejamento', 'Organizamos a estrutura do site, definimos as páginas necessárias, analisamos o conteúdo e estabelecemos a melhor forma de apresentar as informações. O objetivo é criar uma navegação simples e uma comunicação coerente.'),
            ('Desenvolvimento', 'Transformamos o planejamento em uma experiência digital funcional. Trabalhamos design responsivo, estrutura de páginas, tecnologia, desempenho e elementos necessários para que o site funcione corretamente em diferentes dispositivos.'),
            ('Entrega e suporte', 'Após a conclusão do desenvolvimento, colocamos o projeto online e acompanhamos os próximos passos. O site pode continuar a evoluir à medida que surgem novas necessidades, serviços ou objetivos para a empresa.')
        ],
        'faq_items': [
            {
                'q': 'Quanto tempo demora para o site ficar pronto?',
                'a': 'O prazo varia de acordo com a dimensão do projeto, o número de páginas, a complexidade das funcionalidades e os materiais disponíveis. Um site institucional com uma estrutura mais simples pode ter um processo diferente de um projeto com várias páginas ou funcionalidades específicas. Depois de compreendermos os objetivos da empresa, analisamos o escopo necessário e definimos um prazo adequado para o desenvolvimento.'
            },
            {
                'q': 'Como funciona a criação de um site?',
                'a': 'O processo começa com a compreensão do negócio, dos serviços e dos objetivos da empresa. Em seguida, definimos a estrutura do site, organizamos o conteúdo, desenvolvemos o design e implementamos o projeto de forma responsiva. Durante o desenvolvimento, consideramos também aspectos como navegação, desempenho, estrutura das páginas e preparação técnica para busca.'
            },
            {
                'q': 'Qual é o investimento em tráfego pago e quando são utilizadas landing pages?',
                'a': 'O investimento em tráfego pago varia de acordo com os objetivos, público, plataformas e orçamento definido para a campanha. O orçamento pode ser direcionado para Google Ads ou redes sociais. Em determinados projetos de tráfego pago, uma landing page pode ser utilizada como página de destino para uma campanha específica, concentrando a atenção do usuário e facilitando o contato.'
            },
            {
                'q': 'Desenvolvem sistemas e soluções digitais sob medida?',
                'a': 'Sim. Nem todas as necessidades de uma empresa podem ser resolvidas através de um site institucional. Em alguns projetos, é necessário desenvolver ferramentas específicas para organizar informações, automatizar tarefas ou melhorar determinados processos internos. Por isso, desenvolvemos soluções digitais e sistemas personalizados de acordo com as necessidades identificadas em cada projeto.'
            },
            {
                'q': 'Como funciona o processo de contratação e início do projeto?',
                'a': 'Após o primeiro contato, realizamos uma conversa para analisar as necessidades da sua empresa, compreender os serviços pretendidos e avaliar o escopo do projeto. Em seguida, estruturamos uma proposta transparente com prazos, etapas e investimento correspondente. Uma vez aprovada, iniciamos imediatamente a fase de descoberta e planejamento.'
            }
        ],
        'cta_desc': 'Conte-nos sobre o seu negócio, os seus objetivos e o que pretende melhorar na sua presença digital. Podemos analisar as suas necessidades e identificar se o projeto envolve criação de sites, desenvolvimento de soluções digitais, SEO, tráfego pago ou outra necessidade específica.',
        'footer_desc': br_footer_desc,
        'footer_serv_links': [
            ('/br/servicos/criacao-de-sites/', 'Criação de Sites'),
            ('/br/servicos/seo/', 'SEO'),
            ('/br/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/br/servicos/sistemas/', 'Desenvolvimento de Sistemas'),
            ('/br/servicos/google-meu-negocio/', 'Google Meu Negócio')
        ],
        'wa_link': 'https://wa.me/5544998018242',
        'lang_code': 'br'
    },
    'it': {
        'file_path': 'it/index.html',
        'backup_path': '.backup/it_index.html',
        'title': 'Creazione Siti Web e Soluzioni Digitali | Magnani UP®',
        'meta_desc': 'Creazione siti web professionali, SEO, landing page, traffico a pagamento e soluzioni digitali su misura per aziende che vogliono crescere online.',
        'canonical': 'https://dominio.com/it/',
        'og_locale': 'it_IT',
        'og_alt': 'Magnani UP® - Agenzia Digitale e Creazione Siti Web in Italia',
        'hero_desc': 'In Magnani UP®, sviluppiamo siti web professionali, veloci e reattivi per aziende che desiderano rafforzare la presenza digitale, valorizzare i propri servizi e trasformare il sito web in un vero punto di contatto con i clienti. Ogni progetto unisce strategia, design e sviluppo web per creare un\'esperienza chiara, moderna e perfettamente allineata agli obiettivi di business.',
        'b1_title': 'Siti veloci e pronti per i motori di ricerca',
        'b1_desc': 'Strutturiamo ogni sito web puntando su prestazioni elevate, organizzazione dei contenuti e facilità di navigazione. Una solida base tecnica offre un\'esperienza utente più fluida e favorisce l\'indicizzazione da parte dei motori di ricerca.',
        'b2_title': 'Design reattivo su tutti i dispositivi',
        'b2_desc': 'Lo sviluppo considera le diverse dimensioni dello schermo affinché il sito funzioni in modo coerente su computer, tablet e smartphone. Il risultato è un\'esperienza digitale su misura per il comportamento degli utenti moderni.',
        'b3_title': 'Supporto in tutte le fasi',
        'b3_desc': 'Dalla pianificazione iniziale alla pubblicazione del sito web, accompagniamo le diverse fasi del progetto. Il nostro approccio assicura che struttura, contenuti, design e tecnologia siano perfettamente allineati alle esigenze dell\'azienda.',
        'services_intro': [
            'Una presenza digitale professionale va molto oltre la semplice pubblicazione di un sito web. È fondamentale presentare l\'azienda con chiarezza, facilitare il contatto con potenziali clienti, costruire fiducia e creare un\'esperienza coerente su diversi canali.',
            'In Magnani UP®, uniamo creazione di siti web, sviluppo di soluzioni digitali, SEO, traffico a pagamento e strategie di visibilità locale per aiutare le imprese a strutturare al meglio la propria comunicazione online.',
            'Ogni progetto viene analizzato in base alla realtà aziendale, definendo gli strumenti, le tecnologie e le strategie più idonee per raggiungere i suoi obiettivi.'
        ],
        'service_cards': [
            {
                'icon': 'browser',
                'title': 'Creazione Siti Web',
                'desc': 'La creazione di siti web va ben oltre lo sviluppo di una pagina visivamente accattivante. Un sito web professionale deve presentare i servizi con chiarezza, facilitare la navigazione, funzionare correttamente sui diversi dispositivi e trasmettere affidabilità fin dal primo contatto. Sviluppiamo siti web pensati per rappresentare l\'identità aziendale e creare una solida base per la presenza digitale.',
                'link': '/it/servizi/creazione-siti-web/',
                'aria': 'Scopri di più sulla Creazione Siti Web'
            },
            {
                'icon': 'search',
                'title': 'SEO',
                'desc': 'Una valida strategia SEO nasce dalla struttura stessa del sito web. Organizzazione delle pagine, contenuti pertinenti, architettura delle informazioni, prestazioni tecniche ed esperienza utente consentono ai motori di ricerca di comprendere al meglio il progetto digitale. In Magnani UP®, curiamo questi elementi in modo integrato per consolidare la visibilità organica.',
                'link': '/it/servizi/seo/',
                'aria': 'Scopri di più sulla SEO'
            },
            {
                'icon': 'traffic',
                'title': 'Traffico a Pagamento',
                'desc': 'Il traffico a pagamento consente di presentare annunci a segmenti di pubblico mirati in base agli obiettivi commerciali. La strategia comprende Google Ads, social network, landing page e formati pubblicitari avanzati. Il lavoro analizza l\'intero percorso dell\'utente dopo il clic, dalla pagina di atterraggio fino al contatto commerciale.',
                'link': '/it/servizi/traffico-a-pagamento/',
                'aria': 'Scopri di più sul Traffico a Pagamento'
            },
            {
                'icon': 'code',
                'title': 'Sviluppo Sistemi Web',
                'desc': 'Non tutte le esigenze aziendali possono essere risolte attraverso un semplice sito istituzionale. In diversi progetti è indispensabile sviluppare strumenti dedicati per gestire informazioni, automatizzare attività o velocizzare procedure interne. Per questa ragione realizziamo soluzioni digitali e sistemi personalizzati in base alle necessità del cliente.',
                'link': '/it/servizi/sistemi/',
                'aria': 'Scopri di più sullo Sviluppo Sistemi'
            },
            {
                'icon': 'store',
                'title': 'Google Business Profile',
                'desc': 'Per le aziende che si rivolgono a clienti di una specifica area territoriale, la visibilità locale gioca un ruolo decisivo. Informazioni accurate, posizione sulla mappa, descrizione dei servizi e presenza ben strutturata su Google permettono ai potenziali clienti di scoprire l\'attività e mettersi in contatto.',
                'link': '/it/servizi/google-business-profile/',
                'aria': 'Scopri di più su Google Business Profile'
            }
        ],
        'process_intro': [
            'Ogni progetto digitale possiede esigenze differenti. Per questo, prima di avviare lo sviluppo, analizziamo nel dettaglio l\'attività, il pubblico di riferimento, i servizi offerti e i traguardi aziendali.',
            'Sulla base di queste informazioni, strutturiamo il progetto in fasi chiare, consentendo a strategia, contenuti, web design e tecnologia di procedere in perfetta armonia.'
        ],
        'process_steps': [
            ('Analisi e Scoperta', 'Approfondiamo la tua attività, i servizi che offri, il pubblico a cui ti rivolgi e gli obiettivi della tua presenza digitale. Questa fase iniziale definisce una direzione chiara per il progetto.'),
            ('Progettazione', 'Organizziamo la struttura del sito web, stabiliamo le sezioni necessarie, impostiamo l\'architettura dei contenuti e pianifichiamo la disposizione ideale delle informazioni per garantire una navigazione fluida e intuitiva.'),
            ('Sviluppo', 'Trasformiamo la pianificazione in un\'esperienza digitale perfettamente funzionante. Curiamo il design reattivo, la struttura delle pagine, la tecnologia, le prestazioni e gli aspetti necessari per un\'usabilità ideale.'),
            ('Consegna e supporto', 'Completato lo sviluppo, pubblichiamo il progetto online e monitoriamo la fase di avvio. Il sito rimane aperto a continue evoluzioni man mano che crescono le esigenze e gli orizzonti della tua impresa.')
        ],
        'faq_items': [
            {
                'q': 'Quanto tempo ci vuole per completare il sito web?',
                'a': 'I tempi variano in base alla complessità del progetto, al numero di pagine, alle funzionalità richieste e ai materiali forniti. Un sito web aziendale con una struttura lineare richiede tempistiche diverse rispetto a un progetto con molte sezioni o moduli personalizzati. Dopo aver analizzato le necessità dell\'impresa, definiamo una stima realistica e trasparente per la consegna.'
            },
            {
                'q': 'Come funziona la realizzazione di un sito web?',
                'a': 'Il percorso comincia con la comprensione dell\'attività, dei servizi offerti e degli obiettivi dell\'azienda. Successivamente definiamo la struttura del sito web, organizziamo i contenuti, sviluppiamo il design e implementiamo il progetto in modo reattivo. Durante lo sviluppo teniamo conto anche di navigazione, prestazioni, architettura delle pagine e predisposizione tecnica per i motori di ricerca.'
            },
            {
                'q': 'Qual è l\'investimento per il traffico a pagamento e quando servono le landing page?',
                'a': 'L\'investimento in traffico a pagamento varia a seconda degli obiettivi, del pubblico, delle piattaforme e del budget stabilito per la campagna su Google Ads o social media. In determinati contesti promozionali, una landing page dedicata può essere utilizzata come pagina di atterraggio per una campagna specifica, concentrando l\'attenzione dell\'utente e facilitando il contatto.'
            },
            {
                'q': 'Sviluppate sistemi personalizzati e software web su misura?',
                'a': 'Sì. Non tutte le necessità di un\'azienda possono essere risolte attraverso un semplice sito istituzionale. In molti progetti è opportuno creare strumenti dedicati per organizzare dati, automatizzare mansioni o ottimizzare procedure interne. Per questo sviluppiamo soluzioni digitali e sistemi personalizzati in base alle necessità identificate.'
            },
            {
                'q': 'Come funziona la collaborazione e l\'avvio del progetto?',
                'a': 'Dopo il primo contatto, effettuiamo un confronto conoscitivo per esaminare le necessità aziendali, approfondire i servizi richiesti e valutare il perimetro del progetto. Presentiamo quindi una proposta chiara e trasparente con tempistiche, tappe e investimenti. Con la conferma, diamo subito inizio alla fase di scoperta e progettazione.'
            }
        ],
        'cta_desc': 'Raccontaci della tua azienda, dei tuoi obiettivi e di cosa desideri migliorare nella presenza digitale. Analizzeremo le tue esigenze per individuare se il progetto richiede la creazione di un sito web, lo sviluppo di soluzioni digitali, SEO, traffico a pagamento o un intervento specifico.',
        'footer_desc': it_footer_desc,
        'footer_serv_links': [
            ('/it/servizi/creazione-siti-web/', 'Creazione Siti Web'),
            ('/it/servizi/seo/', 'SEO'),
            ('/it/servizi/traffico-a-pagamento/', 'Traffico a Pagamento'),
            ('/it/servizi/sistemi/', 'Sviluppo Sistemi Web'),
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

    # 1. Update <title>, meta description, canonical, robots
    content = re.sub(r'<title>.*?</title>', f'<title>{cfg["title"]}</title>', content)
    content = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']>', f'<meta name="description" content="{cfg["meta_desc"]}">', content)
    content = re.sub(r'<link\s+rel=["\']canonical["\']\s+href=["\'].*?["\']>', f'<link rel="canonical" href="{cfg["canonical"]}">', content)

    # 2. Update JSON-LD Schema
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

    # 3. Hero Description
    content = re.sub(r'<p class="hero-description">.*?</p>', f'<p class="hero-description">\n                {cfg["hero_desc"]}\n              </p>', content, flags=re.DOTALL)

    # 4. Benefits section: replace the 3 items cleanly
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

    # 5. Services Intro (3 paragraphs in .services-header-right)
    serv_intro_html = "\n".join([f'              <p class="services-intro-text">\n                {p}\n              </p>' for p in cfg["services_intro"]])
    content = re.sub(r'<div class="services-header-right">.*?</div>', f'<div class="services-header-right">\n{serv_intro_html}\n            </div>', content, flags=re.DOTALL)

    # 6. Service Cards (5 cards in .services-cards-grid)
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

    # 7. Process Intro (2 paragraphs)
    proc_intro_html = "\n".join([f'              <p class="process-intro-text">\n                {p}\n              </p>' for p in cfg["process_intro"]])
    content = re.sub(r'<div class="process-header-right">.*?</div>', f'<div class="process-header-right">\n{proc_intro_html}\n            </div>', content, flags=re.DOTALL)

    # 8. Process Steps
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

    # 9. FAQ Accordion Items
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

    # 10. CTA Description
    content = re.sub(r'<p class="cta-desc">.*?</p>', f'<p class="cta-desc">\n                {cfg["cta_desc"]}\n              </p>', content, flags=re.DOTALL)

    # 11. Footer Institutional Description
    content = re.sub(r'<p class="footer-institutional-desc">.*?</p>', f'<p class="footer-institutional-desc">\n              {cfg["footer_desc"]}\n            </p>', content, flags=re.DOTALL)

    # 12. Footer Services Navigation Links
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
    print(f"Successfully updated {file_path} and backup {cfg['backup_path']}")

# Run for pt, br, it
for lang in ['pt', 'br', 'it']:
    update_home_file(CONFIGS[lang])

# Also update gateway index.html
with open('index.html', 'r', encoding='utf-8') as f:
    root_html = f.read()

# Update root_html hero, benefits, services, process, faq, cta, footer using pt config
cfg_pt = CONFIGS['pt']
root_html = re.sub(r'<p class="hero-description">.*?</p>', f'<p class="hero-description">\n                {cfg_pt["hero_desc"]}\n              </p>', root_html, flags=re.DOTALL)
root_html = re.sub(r'<p class="cta-desc">.*?</p>', f'<p class="cta-desc">\n                {cfg_pt["cta_desc"]}\n              </p>', root_html, flags=re.DOTALL)
root_html = re.sub(r'<p class="footer-institutional-desc">.*?</p>', f'<p class="footer-institutional-desc">\n              {cfg_pt["footer_desc"]}\n            </p>', root_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(root_html)
with open('.backup/root_index.html', 'w', encoding='utf-8') as f:
    f.write(root_html)
print("Successfully updated root index.html and backup.")
