'''
Programa: Spotify API Client
Autor: Antonio Uribe Ramirez
Fecha de Creación: 16/11/2023

Descripción:
Este programa utiliza la API de Spotify para buscar información. El usuario proporciona la clave de API
e introduce consultas de búsqueda. La respuesta se imprime en formato legible.

Funciones:
- solicitar_clave_api(): Solicita y valida la clave de la API.
- solicitar_consulta(): Solicita y valida consultas de búsqueda.
- realizar_solicitud(api_key, search_query): Realiza la solicitud a la API y devuelve la respuesta.
- imprimir_respuesta(response_json): Imprime información extraída de la respuesta JSON.

Variables:
- api_key (str): Almacena la clave de la API ingresada por el usuario.
- search_query (str): Almacena la consulta de búsqueda ingresada por el usuario.
- conn (HTTPConnection): Objeto de conexión para solicitudes HTTP.
- headers (dict): Cabeceras de la solicitud HTTP con la clave de la API.
- url (str): URL de la consulta de búsqueda construida para la solicitud.
- res (HTTPResponse): Respuesta de la solicitud HTTP.
- data (bytes): Datos de la respuesta en formato binario.
- response_json (dict): Datos de la respuesta JSON convertidos a un diccionario.

Estructuras de Control:
- Bucle while: Mantiene la interactividad con el usuario hasta que decide salir.
- Condiciones if: Verifican entradas vacías y manejan salidas del bucle.

'''
import http.client
from urllib.parse import quote
import json

api_key = "1f71350e6dmsh8a8a1cb3f87e05cp167e02jsn1ad5190257b3"

while True:
    conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
    }

    search_query = input("Ingrese su consulta de búsqueda en Spotify (o 'salir' para salir): ").strip()

    if search_query.lower() == 'salir':
        break

    if not search_query:
        print("Por favor, ingrese una consulta de búsqueda válida.")
        continue

    encoded_search_query = quote(search_query)
    url = f"/search/?q={encoded_search_query}&type=multi&offset=0&limit=10&numberOfTopResults=5"

    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    try:
        response_json = json.loads(data.decode("utf-8"))
    except json.JSONDecodeError as e:
        print(f"Error al decodificar la respuesta JSON: {e}")
        continue

    if "albums" in response_json:
        albums = response_json["albums"]["items"]
        for album in albums:
            album_name = album["data"]["name"]
            artist_name = album["data"]["artists"]["items"][0]["profile"]["name"]
            cover_art_url = album["data"]["coverArt"]["sources"][0]["url"]

            print(f"Álbum: {album_name}")
            print(f"Artista: {artist_name}")
            print(f"URL de portada: {cover_art_url}")
            print("\n")

print("Gracias por usar la aplicación. ¡Hasta luego!")
