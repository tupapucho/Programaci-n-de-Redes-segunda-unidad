# Descripción de la API: Acceso a información de precios y productos de Amazon.
# Autor: Antonio Uribe Ramirez
# Fecha de creación: 30/10/2023

import requests

url = "https://amazon-pricing-and-product-info.p.rapidapi.com/"
headers = {
    'X-RapidAPI-Key': "1f71350e6dmsh8a8a1cb3f87e05cp167e02jsn1ad5190257b3",  
    'X-RapidAPI-Host': "amazon-pricing-and-product-info.p.rapidapi.com"
}

while True:
    asin = input("Ingresa el ASIN del producto de Amazon (o escribe 'Salir' o 'S' para terminar): ")

    if asin.lower() in ['salir', 's']:
        print("¡Programa terminado!")
        break

    try:
        params = {
            "asin": asin,
            "domain": "de"  # Cambia este dominio si es necesario
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            json_data = response.json()
            print(f"Código de estado: {response.status_code}")
            print(json_data)
        else:
            print(f"Error al hacer la solicitud. Código de estado: {response.status_code}")

    except Exception as e:
        print(f"Error: {str(e)}")
