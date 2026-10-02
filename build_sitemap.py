import xml.etree.ElementTree as ET
from datetime import datetime

# Symmetrical URL triples: (PT, BR, IT, priority, changefreq)
URL_GROUPS = [
    # 2.5 Service: Criação de Sites
    (
        "https://www.magnaniup.com/pt/servicos/criacao-de-sites/",
        "https://www.magnaniup.com/br/servicos/criacao-de-sites/",
        "https://www.magnaniup.com/it/servizi/creazione-siti-web/",
        "0.9",
        "weekly"
    ),
    # 1. Home
    (
        "https://www.magnaniup.com/pt/",
        "https://www.magnaniup.com/br/",
        "https://www.magnaniup.com/it/",
        "1.0",
        "weekly"
    ),
    # 2. Service Hubs
    (
        "https://www.magnaniup.com/pt/servicos/",
        "https://www.magnaniup.com/br/servicos/",
        "https://www.magnaniup.com/it/servizi/",
        "0.9",
        "monthly"
    ),
    # 3. Service: SEO
    (
        "https://www.magnaniup.com/pt/servicos/seo/",
        "https://www.magnaniup.com/br/servicos/seo/",
        "https://www.magnaniup.com/it/servizi/seo/",
        "0.85",
        "monthly"
    ),
    # 4. Service: Landing Pages
    (
        "https://www.magnaniup.com/pt/servicos/landing-pages/",
        "https://www.magnaniup.com/br/servicos/landing-pages/",
        "https://www.magnaniup.com/it/servizi/landing-page/",
        "0.85",
        "monthly"
    ),
    # 5. Service: Tráfego Pago
    (
        "https://www.magnaniup.com/pt/servicos/trafego-pago/",
        "https://www.magnaniup.com/br/servicos/trafego-pago/",
        "https://www.magnaniup.com/it/servizi/traffico-a-pagamento/",
        "0.85",
        "monthly"
    ),
    # 6. Service: Sistemas
    (
        "https://www.magnaniup.com/pt/servicos/sistemas/",
        "https://www.magnaniup.com/br/servicos/sistemas/",
        "https://www.magnaniup.com/it/servizi/sistemi/",
        "0.85",
        "monthly"
    ),
    # 7. Service: Google Meu Negócio / Business Profile
    (
        "https://www.magnaniup.com/pt/servicos/google-meu-negocio/",
        "https://www.magnaniup.com/br/servicos/google-meu-negocio/",
        "https://www.magnaniup.com/it/servizi/google-business-profile/",
        "0.85",
        "monthly"
    ),
    # 8. Sobre / Chi Siamo
    (
        "https://www.magnaniup.com/pt/sobre/",
        "https://www.magnaniup.com/br/sobre/",
        "https://www.magnaniup.com/it/chi-siamo/",
        "0.7",
        "monthly"
    ),
    # 9. FAQ
    (
        "https://www.magnaniup.com/pt/faq/",
        "https://www.magnaniup.com/br/faq/",
        "https://www.magnaniup.com/it/faq/",
        "0.7",
        "monthly"
    ),
    # 10. Contacto / Contato / Contatti
    (
        "https://www.magnaniup.com/pt/contacto/",
        "https://www.magnaniup.com/br/contato/",
        "https://www.magnaniup.com/it/contatti/",
        "0.8",
        "monthly"
    )
]

def generate_sitemap():
    today = datetime.now().strftime("%Y-%m-%d")
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">'
    ]

    for pt_url, br_url, it_url, priority, changefreq in URL_GROUPS:
        triples = [
            (pt_url, 'pt-PT'),
            (br_url, 'pt-BR'),
            (it_url, 'it-IT')
        ]
        
        for loc, current_lang in triples:
            xml_lines.append('  <url>')
            xml_lines.append(f'    <loc>{loc}</loc>')
            xml_lines.append(f'    <lastmod>{today}</lastmod>')
            xml_lines.append(f'    <changefreq>{changefreq}</changefreq>')
            xml_lines.append(f'    <priority>{priority}</priority>')
            xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="pt-PT" href="{pt_url}"/>')
            xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="pt-BR" href="{br_url}"/>')
            xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="it-IT" href="{it_url}"/>')
            xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{pt_url}"/>')
            xml_lines.append('  </url>')

    xml_lines.append('</urlset>')
    sitemap_content = '\n'.join(xml_lines) + '\n'

    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print("sitemap.xml generated successfully with 30 URLs.")

if __name__ == '__main__':
    generate_sitemap()
