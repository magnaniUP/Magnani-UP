import os
import re
import json

print("=== Starting Comprehensive Content Expansion ===")

# ==============================================================================
# 1. Update scratch_services_data.py to add criacao-de-sites and update footers
# ==============================================================================
with open('scratch_services_data.py', 'r', encoding='utf-8') as f:
    sdata_content = f.read()

# Expanded footer descriptions from Section 55
pt_footer_desc = "A Magnani UP® desenvolve websites profissionais e soluções digitais para empresas que procuram construir uma presença online clara, moderna e preparada para crescer. Da criação de websites ao desenvolvimento de sistemas personalizados, trabalhamos diferentes áreas do digital para ajudar empresas a apresentar melhor os seus serviços e fortalecer a sua presença online."
br_footer_desc = "A Magnani UP® desenvolve sites profissionais e soluções digitais para empresas que buscam construir uma presença online clara, moderna e preparada para crescer. Da criação de sites ao desenvolvimento de sistemas personalizados, atuamos em múltiplas áreas do digital para ajudar empresas a apresentar melhor seus serviços e fortalecer sua presença online."
it_footer_desc = "Magnani UP® sviluppa siti web professionali e soluzioni digitali per aziende che desiderano costruire una presenza online chiara, moderna e orientata alla crescita. Dalla realizzazione di siti web allo sviluppo di software personalizzati, operiamo nelle principali aree del digitale per valorizzare la tua impresa sul mercato."

# Service data for criacao-de-sites / creazione-siti-web
pt_criacao_data = {
    'slug': 'criacao-de-sites',
    'title': 'Criação de Websites Profissionais em Portugal | Magnani UP®',
    'meta_desc': 'Criação de websites profissionais, rápidos e responsivos em Portugal. Desenvolvimento web sob medida, SEO integrado e foco na experiência do utilizador.',
    'h1': 'Criação de Websites Profissionais em Portugal',
    'tagline': 'Websites modernos, rápidos e pensados para representar a identidade da sua empresa.',
    'hero_desc': 'Na Magnani UP®, criamos websites profissionais, rápidos e responsivos para empresas que pretendem fortalecer a sua presença digital, apresentar melhor os seus serviços e transformar o website num verdadeiro ponto de contacto com os seus clientes. Cada projeto combina estratégia, design e desenvolvimento web para criar uma experiência clara, moderna e alinhada aos objetivos do negócio.',
    'benefits_tag': 'EXCELÊNCIA DIGITAL',
    'benefits_title': 'Estrutura sólida para a presença digital da sua empresa',
    'benefits': [
        {
            'title': 'Design Responsivo e Moderno',
            'desc': 'O desenvolvimento considera diferentes tamanhos de ecrã para que o site funcione de forma consistente em computadores, tablets e smartphones.'
        },
        {
            'title': 'Preparado para Motores de Busca (SEO)',
            'desc': 'Estruturamos cada página com código limpo, semântica correta e tempos de resposta rápidos, facilitando a indexação e a compreensão pelo Google.'
        },
        {
            'title': 'Navegação Fluida e Foco no Utilizador',
            'desc': 'Arquitetura de informação pensada para orientar o visitante com clareza, facilitando o contacto e a conversão de oportunidades de negócio.'
        }
    ],
    'steps': [
        {'num': '01', 'title': 'Descoberta', 'desc': 'Conhecemos o seu negócio, os serviços que oferece, o público que pretende alcançar e os objetivos da sua presença digital.'},
        {'num': '02', 'title': 'Planeamento', 'desc': 'Organizamos a estrutura do website, definimos as páginas necessárias, analisamos o conteúdo e estabelecemos a navegação ideal.'},
        {'num': '03', 'title': 'Desenvolvimento', 'desc': 'Transformamos o planeamento numa experiência funcional com design responsivo, alta performance e preparação técnica para pesquisa.'},
        {'num': '04', 'title': 'Entrega e Suporte', 'desc': 'Colocamos o projeto online com rigor técnico e acompanhamos a sua evolução contínua conforme as metas da sua empresa.'}
    ],
    'faqs': [
        {
            'q': 'Quanto tempo demora para o website ficar pronto?',
            'a': 'O prazo varia de acordo com a dimensão do projeto, o número de páginas, a complexidade das funcionalidades e os materiais disponíveis. Um website institucional com uma estrutura essencial pode ser concluído em poucas semanas, enquanto projetos com integrações específicas ou múltiplas páginas exigem um cronograma proporcional. Após compreendermos os objetivos da empresa, analisamos o âmbito necessário e apresentamos um prazo realista e acordado para a entrega.'
        },
        {
            'q': 'Como funciona a criação de um website profissional?',
            'a': 'O processo começa com a compreensão detalhada do negócio, dos serviços e dos objetivos da empresa. Em seguida, desenhamos a estrutura do website, organizamos os textos e elementos visuais, criamos um design moderno e implementamos a programação de forma responsiva. Durante todo o desenvolvimento, otimizamos o desempenho técnico, a velocidade de carregamento, a experiência do utilizador e a preparação para pesquisa orgânica.'
        },
        {
            'q': 'O website já vem preparado para dispositivos móveis e motores de busca?',
            'a': 'Sim. Todos os nossos projetos são desenvolvidos com design 100% responsivo, adaptando-se a qualquer dispositivo móvel, e incluem as melhores práticas técnicas de SEO (código limpo, metatags, headings semânticos e dados estruturados Schema.org).'
        }
    ]
}

br_criacao_data = {
    'slug': 'criacao-de-sites',
    'title': 'Criação de Sites Profissionais | Magnani UP®',
    'meta_desc': 'Criação de sites profissionais, rápidos e responsivos. Desenvolvimento web sob medida, SEO integrado e foco na experiência do usuário para empresas no Brasil.',
    'h1': 'Criação de Sites Profissionais para Empresas',
    'tagline': 'Sites modernos, velozes e estrategicamente desenhados para gerar resultados.',
    'hero_desc': 'Na Magnani UP®, criamos sites profissionais, rápidos e responsivos para empresas que querem fortalecer sua presença digital, apresentar melhor seus serviços e transformar o site em um verdadeiro canal de vendas e contato com clientes. Cada projeto combina estratégia, design e desenvolvimento web para criar uma experiência clara, moderna e alinhada aos objetivos do seu negócio.',
    'benefits_tag': 'BASE DIGITAL SÓLIDA',
    'benefits_title': 'Desenvolvimento web focado em autoridade, performance e resultados',
    'benefits': [
        {
            'title': 'Design Responsivo em Todos os Dispositivos',
            'desc': 'O desenvolvimento considera diferentes tamanhos de tela para que o site funcione de forma consistente em computadores, tablets e smartphones.'
        },
        {
            'title': 'Otimização para Mecanismos de Busca (SEO)',
            'desc': 'Estruturamos cada página pensando em velocidade, organização de conteúdo e facilidade de navegação, facilitando a indexação no Google.'
        },
        {
            'title': 'Comunicação Clara e Foco em Conversão',
            'desc': 'Apresentamos os diferenciais dos seus serviços de forma evidente, guiando o visitante naturalmente para a solicitação de orçamento ou contato.'
        }
    ],
    'steps': [
        {'num': '01', 'title': 'Descoberta', 'desc': 'Conhecemos o seu negócio, os serviços que você oferece, o público que pretende alcançar e os objetivos da sua presença digital.'},
        {'num': '02', 'title': 'Planejamento', 'desc': 'Organizamos a estrutura do site, definimos as páginas necessárias, analisamos o conteúdo e estabelecemos a navegação ideal.'},
        {'num': '03', 'title': 'Desenvolvimento', 'desc': 'Transformamos o planejamento em uma experiência digital funcional com design responsivo, alto desempenho e boas práticas técnicas.'},
        {'num': '04', 'title': 'Entrega e Suporte', 'desc': 'Publicamos o site online e acompanhamos o lançamento, mantendo o projeto preparado para evoluir continuamente.'}
    ],
    'faqs': [
        {
            'q': 'Quanto tempo demora para o site ficar pronto?',
            'a': 'O prazo varia conforme a dimensão do projeto, o volume de páginas, a complexidade das funcionalidades e o fornecimento dos materiais. Um site institucional enxuto tem um ciclo de produção mais ágil, enquanto projetos robustos com integrações ou sistemas demandam um cronograma planejado. Logo após a análise inicial das necessidades da sua empresa, definimos um cronograma claro e transparente para cada entrega.'
        },
        {
            'q': 'Como funciona o desenvolvimento de um site profissional?',
            'a': 'O processo tem início na compreensão aprofundada do seu negócio, dos diferenciais dos serviços e das metas comerciais. A partir disso, planejamos a arquitetura do site, estruturamos a comunicação visual e textual, produzimos o layout e codificamos o projeto de forma responsiva. Durante toda a execução, priorizamos velocidade de carregamento, usabilidade em smartphones e conformidade técnica com as boas práticas dos buscadores.'
        },
        {
            'q': 'O site funciona perfeitamente em celulares e tablets?',
            'a': 'Sim. Criamos layouts adaptativos que se ajustam automaticamente a qualquer tamanho de tela, garantindo navegação rápida e experiência agradável para usuários de smartphones e computadores.'
        }
    ]
}

it_criacao_data = {
    'slug': 'creazione-siti-web',
    'title': 'Creazione Siti Web Professionali | Magnani UP®',
    'meta_desc': 'Creazione di siti web professionali, veloci e reattivi in Italia. Sviluppo web su misura, SEO integrata e design curato per aziende che vogliono crescere online.',
    'h1': 'Creazione di Siti Web Professionali per Aziende',
    'tagline': 'Siti web moderni, veloci e progettati per valorizzare l\'identità del tuo brand.',
    'hero_desc': 'In Magnani UP®, sviluppiamo siti web professionali, veloci e reattivi per aziende che desiderano rafforzare la presenza digitale, valorizzare i propri servizi e trasformare il sito web in un vero punto di contatto con i clienti. Ogni progetto unisce strategia, design e sviluppo web per creare un\'esperienza chiara, moderna e perfettamente allineata agli obiettivi di business.',
    'benefits_tag': 'ECCELLENZA DIGITALE',
    'benefits_title': 'Una solida base per la presenza online della tua azienda',
    'benefits': [
        {
            'title': 'Design Reattivo su Tutti i Dispositivi',
            'desc': 'Lo sviluppo considera le diverse dimensioni dello schermo affinché il sito funzioni in modo impeccabile su computer, tablet e smartphone.'
        },
        {
            'title': 'Predisposizione per i Motori di Ricerca (SEO)',
            'desc': 'Strutturiamo ogni pagina curando prestazioni elevate, organizzazione dei contenuti e facilità di navigazione per agevolare l\'indicizzazione Google.'
        },
        {
            'title': 'Navigazione Fluida ed Esperienza Utente',
            'desc': 'Architettura informativa concepita per presentare i servizi con chiarezza, instaurare fiducia e facilitare il contatto commerciale.'
        }
    ],
    'steps': [
        {'num': '01', 'title': 'Analisi e Scoperta', 'desc': 'Approfondiamo la tua attività, i servizi che offri, il pubblico a cui ti rivolgi e gli obiettivi della tua presenza digitale.'},
        {'num': '02', 'title': 'Progettazione', 'desc': 'Organizziamo la struttura del sito web, stabiliamo le pagine necessarie, pianifichiamo i contenuti e impostiamo la navigazione ideale.'},
        {'num': '03', 'title': 'Web Design e Sviluppo', 'desc': 'Trasformiamo il piano progettuale in un\'esperienza digitale pienamente funzionale con codice pulito, velocità e design reattivo.'},
        {'num': '04', 'title': 'Consegna e Supporto', 'desc': 'Pubblichiamo il sito online e monitoriamo la fase di avvio, mantenendo il progetto aperto a future evoluzioni aziendali.'}
    ],
    'faqs': [
        {
            'q': 'Quanto tempo ci vuole per completare il sito web?',
            'a': 'I tempi variano in base alle dimensioni del progetto, al numero di pagine, alla complessità delle funzionalità richieste e ai contenuti disponibili. Un sito aziendale con una struttura lineare richiede tempi differenti rispetto a un portale complesso o con moduli personalizzati. Dopo aver compreso le tue esigenze, analizziamo l\'ambito del lavoro e concordiamo una stima chiara per la consegna.'
        },
        {
            'q': 'Come si svolge la realizzazione di un sito web?',
            'a': 'Il percorso comincia con la comprensione dell\'attività, dei servizi offerti e degli obiettivi dell\'azienda. Successivamente definiamo la struttura del sito web, organizziamo i contenuti, curiamo il web design e sviluppiamo il progetto in modo reattivo. Durante lo sviluppo teniamo conto anche di navigazione, velocità, architettura delle pagine e predisposizione tecnica per i motori di ricerca.'
        },
        {
            'q': 'Il sito è compatibile con tutti gli smartphone e i browser moderni?',
            'a': 'Certamente. Tutti i progetti sono realizzati con responsive design avanzato, assicurando visualizzazione perfetta e tempi di caricamento rapidi su qualsiasi dispositivo mobile e desktop.'
        }
    ]
}

# Update scratch_services_data.py via import / dict manipulation
from scratch_services_data import DATA

DATA['pt']['footer_desc'] = pt_footer_desc
DATA['br']['footer_desc'] = br_footer_desc
DATA['it']['footer_desc'] = it_footer_desc

DATA['pt']['services']['criacao-de-sites'] = pt_criacao_data
DATA['br']['services']['criacao-de-sites'] = br_criacao_data
DATA['it']['services']['creazione-siti-web'] = it_criacao_data

# Re-serialize scratch_services_data.py
with open('scratch_services_data.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\nDATA = " + json.dumps(DATA, indent=4, ensure_ascii=False) + "\n")
print("1. Updated scratch_services_data.py successfully.")

# ==============================================================================
# 2. Update generate_services.py
# ==============================================================================
with open('generate_services.py', 'r', encoding='utf-8') as f:
    gen_serv = f.read()

# Add ('criacao-de-sites', 'criacao-de-sites', 'creazione-siti-web') to SERVICE_KEYS if not present
if "('criacao-de-sites'" not in gen_serv:
    gen_serv = gen_serv.replace(
        "SERVICE_KEYS = [",
        "SERVICE_KEYS = [\n    ('criacao-de-sites', 'criacao-de-sites', 'creazione-siti-web'),"
    )

# Add icon for criacao-de-sites and creazione-siti-web if not present
browser_icon = """    'criacao-de-sites': '''<svg class="service-svg-icon" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
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
    </svg>''',"""

if "'criacao-de-sites':" not in gen_serv:
    gen_serv = gen_serv.replace(
        "SERVICE_ICONS = {",
        "SERVICE_ICONS = {\n" + browser_icon
    )

# Update footer_serv_links in generate_services.py
pt_footer_serv_code = """        footer_serv_links = [
            ('/pt/servicos/criacao-de-sites/', 'Criação de Websites'),
            ('/pt/servicos/seo/', 'SEO'),
            ('/pt/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/pt/servicos/sistemas/', 'Criação de Sistemas'),
            ('/pt/servicos/google-meu-negocio/', 'Google Perfil de Empresa')
        ]"""

br_footer_serv_code = """        footer_serv_links = [
            ('/br/servicos/criacao-de-sites/', 'Criação de Sites'),
            ('/br/servicos/seo/', 'SEO'),
            ('/br/servicos/trafego-pago/', 'Tráfego Pago'),
            ('/br/servicos/sistemas/', 'Desenvolvimento de Sistemas'),
            ('/br/servicos/google-meu-negocio/', 'Google Meu Negócio')
        ]"""

it_footer_serv_code = """        footer_serv_links = [
            ('/it/servizi/creazione-siti-web/', 'Creazione Siti Web'),
            ('/it/servizi/seo/', 'SEO'),
            ('/it/servizi/traffico-a-pagamento/', 'Traffico a Pagamento'),
            ('/it/servizi/sistemi/', 'Sviluppo Sistemi Web'),
            ('/it/servizi/google-business-profile/', 'Google Business Profile')
        ]"""

gen_serv = re.sub(r'if lang_code == [\'"]pt[\'"]:\s*nav_items = \[.*?\]\s*footer_serv_links = \[.*?\]',
                  lambda m: m.group(0).split('footer_serv_links = [')[0] + pt_footer_serv_code.strip(),
                  gen_serv, flags=re.DOTALL)

gen_serv = re.sub(r'elif lang_code == [\'"]br[\'"]:\s*nav_items = \[.*?\]\s*footer_serv_links = \[.*?\]',
                  lambda m: m.group(0).split('footer_serv_links = [')[0] + br_footer_serv_code.strip(),
                  gen_serv, flags=re.DOTALL)

gen_serv = re.sub(r'else:\s*nav_items = \[.*?\]\s*footer_serv_links = \[.*?\]',
                  lambda m: m.group(0).split('footer_serv_links = [')[0] + it_footer_serv_code.strip(),
                  gen_serv, flags=re.DOTALL)

with open('generate_services.py', 'w', encoding='utf-8') as f:
    f.write(gen_serv)
print("2. Updated generate_services.py successfully.")

# Run generate_services.py
os.system("python3 generate_services.py")

# ==============================================================================
# 3. Update generate_hubs.py
# ==============================================================================
with open('generate_hubs.py', 'r', encoding='utf-8') as f:
    gen_hubs = f.read()

# Add icon for criacao-de-sites and creazione-siti-web if not in SERVICE_ICONS in generate_hubs.py
if "'criacao-de-sites':" not in gen_hubs:
    gen_hubs = gen_hubs.replace(
        "SERVICE_ICONS = {",
        "SERVICE_ICONS = {\n" + browser_icon
    )

# Update footer_serv_links in generate_hubs.py
gen_hubs = re.sub(r'if lang_code == [\'"]pt[\'"]:\s*nav_items = \[.*?\]\s*footer_serv_links = \[.*?\]',
                  lambda m: m.group(0).split('footer_serv_links = [')[0] + pt_footer_serv_code.strip(),
                  gen_hubs, flags=re.DOTALL)

gen_hubs = re.sub(r'elif lang_code == [\'"]br[\'"]:\s*nav_items = \[.*?\]\s*footer_serv_links = \[.*?\]',
                  lambda m: m.group(0).split('footer_serv_links = [')[0] + br_footer_serv_code.strip(),
                  gen_hubs, flags=re.DOTALL)

gen_hubs = re.sub(r'else:\s*nav_items = \[.*?\]\s*footer_serv_links = \[.*?\]',
                  lambda m: m.group(0).split('footer_serv_links = [')[0] + it_footer_serv_code.strip(),
                  gen_hubs, flags=re.DOTALL)

# Add criacao-de-sites as first card in HUB_CONFIG for pt, br, it
pt_criacao_card_code = """            {
                'slug': 'criacao-de-sites',
                'title': 'Criação de Websites Profissionais',
                'desc': 'Desenvolvimento de websites modernos, rápidos e responsivos para fortalecer a presença digital e transformar o site num verdadeiro ponto de contacto.',
                'link': '/pt/servicos/criacao-de-sites/',
                'link_label': 'Conhecer Criação de Websites'
            },"""

br_criacao_card_code = """            {
                'slug': 'criacao-de-sites',
                'title': 'Criação de Sites Profissionais',
                'desc': 'Desenvolvimento de sites modernos, rápidos e responsivos para empresas que querem apresentar seus serviços com clareza e transformar visitantes em clientes.',
                'link': '/br/servicos/criacao-de-sites/',
                'link_label': 'Conhecer Criação de Sites'
            },"""

it_criacao_card_code = """            {
                'slug': 'creazione-siti-web',
                'title': 'Creazione Siti Web Professionali',
                'desc': 'Sviluppo di siti web moderni, veloci e reattivi per valorizzare l\'identità aziendale e trasformare il sito in un vero punto di contatto con i clienti.',
                'link': '/it/servizi/creazione-siti-web/',
                'link_label': 'Scopri Creazione Siti Web'
            },"""

if "'slug': 'criacao-de-sites'" not in gen_hubs:
    # insert in pt cards
    gen_hubs = gen_hubs.replace("'cards': [\n            {\n                'slug': 'seo'",
                                "'cards': [\n" + pt_criacao_card_code + "\n            {\n                'slug': 'seo'")
    # insert in br cards
    gen_hubs = gen_hubs.replace("'cards': [\n            {\n                'slug': 'seo'",
                                "'cards': [\n" + br_criacao_card_code + "\n            {\n                'slug': 'seo'")
    # insert in it cards
    gen_hubs = gen_hubs.replace("'cards': [\n            {\n                'slug': 'seo'",
                                "'cards': [\n" + it_criacao_card_code + "\n            {\n                'slug': 'seo'")

with open('generate_hubs.py', 'w', encoding='utf-8') as f:
    f.write(gen_hubs)
print("3. Updated generate_hubs.py successfully.")

os.system("python3 generate_hubs.py")

# ==============================================================================
# 4. Update build_sitemap.py and rebuild sitemap.xml
# ==============================================================================
with open('build_sitemap.py', 'r', encoding='utf-8') as f:
    sitemap_py = f.read()

if 'criacao-de-sites' not in sitemap_py:
    criacao_entry = """    # 2.5 Service: Criação de Sites
    (
        "https://dominio.com/pt/servicos/criacao-de-sites/",
        "https://dominio.com/br/servicos/criacao-de-sites/",
        "https://dominio.com/it/servizi/creazione-siti-web/",
        "0.9",
        "weekly"
    ),"""
    sitemap_py = sitemap_py.replace('URL_GROUPS = [', 'URL_GROUPS = [\n' + criacao_entry)

with open('build_sitemap.py', 'w', encoding='utf-8') as f:
    f.write(sitemap_py)

os.system("python3 build_sitemap.py")
print("4. Rebuilt sitemap.xml with Criação de Sites.")

print("=== Part 1 Complete ===")
