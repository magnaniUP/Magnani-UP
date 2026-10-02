"""
Magnani UP® - IndexNow Submission Utility
Protocolo oficial para notificação instantânea de rastreamento no Bing, Yandex e outros motores de busca.

Instruções de Utilização:
1. Obtenha a sua chave de autenticação no Bing Webmaster Tools ou gere uma chave de 32 caracteres hexadecimais.
2. Crie o ficheiro de verificação na raiz do site com o nome {SUA_CHAVE}.txt contendo a própria chave.
3. Configure a variável INDEXNOW_KEY abaixo com a sua chave real.
4. Execute: python3 indexnow_submission.py
"""

import urllib.request
import json
import os

# Configurações do Projeto
HOST = "dominio.com"
KEY_LOCATION = f"https://{HOST}/"

# AVISO: Insira a sua chave real gerada no Bing Webmaster Tools. Não utilize chaves fictícias.
INDEXNOW_KEY = os.environ.get("INDEXNOW_KEY", "")

URL_LIST = [
    f"https://{HOST}/pt/",
    f"https://{HOST}/br/",
    f"https://{HOST}/it/",
    f"https://{HOST}/pt/servicos/",
    f"https://{HOST}/br/servicos/",
    f"https://{HOST}/it/servizi/",
    f"https://{HOST}/pt/servicos/seo/",
    f"https://{HOST}/br/servicos/seo/",
    f"https://{HOST}/it/servizi/seo/",
    f"https://{HOST}/pt/servicos/landing-pages/",
    f"https://{HOST}/br/servicos/landing-pages/",
    f"https://{HOST}/it/servizi/landing-page/",
    f"https://{HOST}/pt/servicos/trafego-pago/",
    f"https://{HOST}/br/servicos/trafego-pago/",
    f"https://{HOST}/it/servizi/traffico-a-pagamento/",
    f"https://{HOST}/pt/servicos/sistemas/",
    f"https://{HOST}/br/servicos/sistemas/",
    f"https://{HOST}/it/servizi/sistemi/",
    f"https://{HOST}/pt/servicos/google-meu-negocio/",
    f"https://{HOST}/br/servicos/google-meu-negocio/",
    f"https://{HOST}/it/servizi/google-business-profile/",
    f"https://{HOST}/pt/sobre/",
    f"https://{HOST}/br/sobre/",
    f"https://{HOST}/it/chi-siamo/",
    f"https://{HOST}/pt/faq/",
    f"https://{HOST}/br/faq/",
    f"https://{HOST}/it/faq/",
    f"https://{HOST}/pt/contacto/",
    f"https://{HOST}/br/contato/",
    f"https://{HOST}/it/contatti/"
]

def submit_indexnow():
    if not INDEXNOW_KEY:
        print("[IndexNow] Estrutura preparada. Configure a variável de ambiente INDEXNOW_KEY com a sua chave real do Bing.")
        return

    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{KEY_LOCATION}{INDEXNOW_KEY}.txt",
        "urlList": URL_LIST
    }

    endpoints = [
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow"
    ]

    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    data = json.dumps(payload).encode("utf-8")

    for endpoint in endpoints:
        try:
            req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req) as resp:
                print(f"[IndexNow] Submissão para {endpoint}: Código {resp.status} - Sucesso!")
        except Exception as e:
            print(f"[IndexNow] Erro ao submeter para {endpoint}: {e}")

if __name__ == "__main__":
    submit_indexnow()
