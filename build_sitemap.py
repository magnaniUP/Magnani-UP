import xml.etree.ElementTree as ET
from datetime import datetime

# Symmetrical URL triples: (PT, BR, IT, priority, changefreq)
URL_GROUPS = [
    # 2.5 Service: Criação de Sites
    (
        "https://dominio.com/pt/servicos/criacao-de-sites/",
        "https://dominio.com/br/servicos/criacao-de-sites/",
        "https://dominio.com/it/servizi/creazione-siti-web/",
        "0.9",
        "weekly"
    ),
    # 1. Home
    (
        "https://dominio.com/pt/",
        "https://dominio.com/br/",
        "https://dominio.com/it/",
        "1.0",
        "weekly"
    ),
    # 2. Service Hubs
    (
        "https://dominio.com/pt/servicos/",
        "https://dominio.com/br/servicos/",
        "https://dominio.com/it/servizi/",
        "0.9",
        "monthly"
    ),
    # 3. Service: SEO
    (
        "https://dominio.com/pt/servicos/seo/",
        "https://dominio.com/br/servicos/seo/",
        "https://dominio.com/it/servizi/seo/",
        "0.85",
        "monthly"
    ),
    # 4. Service: Landing Pages
    (
        "https://dominio.com/pt/servicos/landing-pages/",
        "https://dominio.com/br/servicos/landing-pages/",
        "https://dominio.com/it/servizi/landing-page/",
        "0.85",
        "monthly"
    ),
    # 5. Service: Tráfego Pago
    (
        "https://dominio.com/pt/servicos/trafego-pago/",
        "https://dominio.com/br/servicos/trafego-pago/",
        "https://dominio.com/it/servizi/traffico-a-pagamento/",
        "0.85",
        "monthly"
    ),
    # 6. Service: Sistemas
    (
        "https://dominio.com/pt/servicos/sistemas/",
        "https://dominio.com/br/servicos/sistemas/",
        "https://dominio.com/it/servizi/sistemi/",
        "0.85",
        "monthly"
    ),
    # 7. Service: Google Meu Negócio / Business Profile
    (
        "https://dominio.com/pt/servicos/google-meu-negocio/",
        "https://dominio.com/br/servicos/google-meu-negocio/",
        "https://dominio.com/it/servizi/google-business-profile/",
        "0.85",
        "monthly"
    ),
    # 8. Sobre / Chi Siamo
    (
        "https://dominio.com/pt/sobre/",
        "https://dominio.com/br/sobre/",
        "https://dominio.com/it/chi-siamo/",
        "0.7",
        "monthly"
    ),
    # 9. FAQ
    (
        "https://dominio.com/pt/faq/",
        "https://dominio.com/br/faq/",
        "https://dominio.com/it/faq/",
        "0.7",
        "monthly"
    ),
    # 10. Contacto / Contato / Contatti
    (
        "https://dominio.com/pt/contacto/",
        "https://dominio.com/br/contato/",
        "https://dominio.com/it/contatti/",
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
