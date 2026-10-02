<<<<<<< HEAD
# Magnani UP® - Website Institucional Multirregional

Website institucional desenvolvido para a agência **Magnani UP®**, com foco em criação de websites de alta conversão, performance e serviços digitais.

## 🌍 Arquitetura Multirregional & SEO Internacional

O projeto é estruturado para atender três mercados independentes com conteúdo culturalmente adaptado e SEO individualizado:

| Mercado | Código | Idioma | URL Base | Contato | CTA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Portugal** | `pt-PT` | Português Europeu | `/pt/` | `/pt/contacto/` | *Vamos conversar* |
| **Brasil** | `pt-BR` | Português Brasileiro | `/br/` | `/br/contato/` | *Vamos conversar* |
| **Itália** | `it-IT` | Italiano Natural | `/it/` | `/it/contatti/` | *Parliamo* |

### Matriz de Equivalência Hreflang
Cada página possui suas contrapartes mapeadas com `hreflang="pt-PT"`, `hreflang="pt-BR"`, `hreflang="it-IT"` e `hreflang="x-default"`:

- Início: `/pt/` ↔ `/br/` ↔ `/it/`
- Serviços: `/pt/servicos/` ↔ `/br/servicos/` ↔ `/it/servizi/`
- Sobre: `/pt/sobre/` ↔ `/br/sobre/` ↔ `/it/chi-siamo/`
- FAQ: `/pt/faq/` ↔ `/br/faq/` ↔ `/it/faq/`
- Contato: `/pt/contacto/` ↔ `/br/contato/` ↔ `/it/contatti/`

## 📁 Estrutura de Diretórios

```
magnani-up/
├── index.html            # Gateway neutro de seleção de mercado
├── pt/                   # Versão Portugal (pt-PT)
├── br/                   # Versão Brasil (pt-BR)
├── it/                   # Versão Itália (it-IT)
├── css/
│   ├── reset.css         # Reset moderno e acessibilidade
│   ├── global.css        # Tokens, variáveis e atmosfera de fundo
│   ├── header.css        # Header e Menu fiéis ao mockup
│   └── responsive.css    # Drawer mobile e media queries
├── js/
│   ├── main.js           # Inicialização
│   └── navigation.js     # Router de equivalências e interações
├── images/
│   ├── logo/             # Vetores e raster do logotipo oficial
│   ├── hero/             # Recursos futuros da Hero
│   ├── services/         # Recursos futuros de Serviços
│   ├── icons/            # Ícones do sistema
│   └── backgrounds/      # Elementos atmosféricos
├── fonts/                # Plus Jakarta Sans
├── components/
│   └── header/           # Template modular do header
├── sitemap.xml           # Sitemap com mapeamento cruzado hreflang
├── robots.txt            # Regras para buscadores
└── README.md
```

## 🎯 Etapa Atual: Header / Menu
Nesta etapa, apenas o **Header** foi implementado, mantendo fidelidade visual absoluta ao mockup original e preparando o alicerce para as seções seguintes.
=======
# Magnani-UP
>>>>>>> 7dc8114d339dd4ea646e41616283eb0563f97a83
