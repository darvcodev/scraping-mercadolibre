import requests
from bs4 import BeautifulSoup
import json

def scrape_mercadolibre():
    # URL de la página de Mercado Libre
    url = 'https://listado.mercadolibre.com.co/apple'

    # Headers para evitar bloqueos
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    # Realizar la solicitud GET
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parsear el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar los productos
        productos = soup.find_all('li', {'class': lambda x: x and 'ui-search-layout__item' in x})

        resultados = []

        # Extraer información de cada producto
        for producto in productos:
            titulo_elemento = producto.find('h2', class_='poly-component__title')
            titulo = titulo_elemento.text.strip() if titulo_elemento else 'N/A'

            precio_elemento = producto.find('div', class_='poly-price__current')
            if precio_elemento:
                precio = precio_elemento.find('span', class_='andes-money-amount__fraction')
                precio = precio.text.strip() if precio else 'N/A'
            else:
                precio = 'N/A'

            resultados.append({'Título': titulo, 'Precio': precio})

        # Guardar resultados en JSON
        with open('data/output.json', 'w', encoding='utf-8') as file:
            json.dump(resultados, file, ensure_ascii=False, indent=4)

        print("Scraping completado. Resultados guardados en data/output.json.")
    else:
        print(f"Error al obtener la página, código de estado: {response.status_code}")

if __name__ == "__main__":
    scrape_mercadolibre()