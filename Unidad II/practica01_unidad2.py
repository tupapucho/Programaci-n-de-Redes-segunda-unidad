'''
Descripción de la API: Acceso a la información de una pista de SoundCloud a través de RapidAPI.
Autor: Antonio Uribe Ramirez
Fecha de creación: 30/10/2023
'''
import urllib.parse
import requests
import time

main_api = "https://soundcloud4.p.rapidapi.com/song/info"

while True:
    user_input = input("Ingresa la URL de la pista de SoundCloud (o escribe 'Salir' o 'S' para terminar): ")
    
    if user_input.lower() in ['salir', 's']:
        print("¡Programa terminado!")
        break

    track_url = user_input
    querystring = urllib.parse.urlencode({"track_url": track_url})

    url = f"{main_api}?{querystring}"

    headers = {
        "X-RapidAPI-Key": "1f71350e6dmsh8a8a1cb3f87e05cp167e02jsn1ad5190257b3",
        "X-RapidAPI-Host": "soundcloud4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 429:
        print("Demasiadas solicitudes. Espera un momento antes de intentar nuevamente.")
        time.sleep(10)  # Esperar 10 segundos (puedes ajustar el tiempo de espera)
        continue
    elif response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Error al hacer la solicitud:", response.status_code)
