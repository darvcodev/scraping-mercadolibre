import requests

def save_mercadolibre_html():
    # URL de la página de Mercado Libre
    url = 'https://listado.mercadolibre.com.co/apple'

    # Headers para evitar bloqueos
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    # Realizar la solicitud GET
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        with open('docs/index.html', 'w', encoding='utf-8') as file:
            file.write(response.text)

        print("HTML extraído y guardado como docs/index.html.")
    else:
        print(f"Error al obtener la página, código de estado: {response.status_code}")

if __name__ == "__main__":
    save_mercadolibre_html()