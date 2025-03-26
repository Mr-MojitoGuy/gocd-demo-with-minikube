import requests
import logging

# Setup do logger
logging.basicConfig(
    filename='output.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch_cat_fact():
    url = "https://catfact.ninja/fact"
    try:
        response = requests.get(url)
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.status_code, response.json()
    except Exception as e:
        logging.error(f"Erro ao obter factos: {e}")
        return None, None

# Executar só se for chamado diretamente (e não via teste)
if __name__ == "__main__":
    fetch_cat_fact()

