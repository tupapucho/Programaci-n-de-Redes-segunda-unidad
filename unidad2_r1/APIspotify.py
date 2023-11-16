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

while True:
    # Solicitar la clave de la API al usuario
    api_key = input("Ingrese su clave de API de Spotify (o 'salir' para salir): ").strip()

    # Verificar si el usuario quiere salir
    if api_key.lower() == 'salir':
        break

    # Verificar si la entrada de la clave de API está vacía
    if not api_key:
        print("Por favor, ingrese una clave de API válida.")
        continue

    # Construir la conexión y las cabeceras
    conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
    }

    # Solicitar la consulta de búsqueda al usuario
    search_query = input("Ingrese su consulta de búsqueda en Spotify (o 'salir' para salir): ").strip()

    # Verificar si el usuario quiere salir
    if search_query.lower() == 'salir':
        break

    # Verificar si la entrada de la consulta de búsqueda está vacía
    if not search_query:
        print("Por favor, ingrese una consulta de búsqueda válida.")
        continue

    # Codificar la consulta de búsqueda para la URL
    encoded_search_query = quote(search_query)

    # Construir la URL de la consulta de búsqueda
    url = f"/search/?q={encoded_search_query}&type=multi&offset=0&limit=10&numberOfTopResults=5"

    # Realizar la solicitud HTTP
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()

    # Verificar si la respuesta es un JSON válido
    try:
        response_json = json.loads(data.decode("utf-8"))
    except json.JSONDecodeError as e:
        print(f"Error al decodificar la respuesta JSON: {e}")
        continue

    # Imprimir la información extraída de la respuesta JSON
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

# Mensaje de despedida al salir del bucle
print("Gracias por usar la aplicación. ¡Hasta luego!")


