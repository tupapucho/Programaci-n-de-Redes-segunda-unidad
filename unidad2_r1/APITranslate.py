'''
ingrese llave: 1f71350e6dmsh8a8a1cb3f87e05cp167e02jsn1ad5190257b3
Programa: Detección de Idioma con API de Google Translate a través de RapidAPI.
Autor: Antonio Uribe Ramirez
Fecha de Creación: 16/11/2023

Descripción:
Este programa utiliza la API de Google Translate para detectar automáticamente el idioma de un texto ingresado por el usuario.
Se conecta a la API a través de RapidAPI, permitiendo al usuario realizar múltiples consultas hasta que decide salir.

Funciones:
- main(): Función principal que ejecuta el programa.
Variables Principales:
- api_url (str): URL de la API ingresada por el usuario.
- api_key (str): Clave de la API ingresada por el usuario.
- url (str): URL completa para la detección de idioma.
- headers (dict): Encabezados necesarios para la solicitud a la API.
- user_input (str): Texto ingresado por el usuario para detectar el idioma.
- response (obj): Respuesta de la solicitud a la API.
- json_data (dict): Datos de la respuesta en formato JSON.
- status_code (int): Código de estado de la respuesta.
'''
import requests

api_key = input("Ingrese su clave de la API: ")

if not api_key:
    print("Clave de API no válida. Saliendo del programa.")
    exit()

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'Accept-Encoding': "application/gzip",
    'X-RapidAPI-Key': api_key,
    'X-RapidAPI-Host': "google-translate1.p.rapidapi.com"
}

while True:
    user_input = input("Ingrese el texto que desea detectar (o 'S' para salir): ")

    if user_input.lower() == 's' or user_input.lower() == 'salir':
        print("¡Hasta luego!")
        break

    if not user_input:
        print("Entrada no válida. Por favor, ingrese un texto.")
        continue


    payload = f"q={user_input}"
    response = requests.post(url, data=payload, headers=headers)

    json_data = response.json()
    status_code = response.status_code


    if status_code == 200:
        detected_language = json_data['data']['detections'][0][0]['language']
        print(f"Texto: {user_input}\nIdioma detectado: {detected_language}\n")
    else:
        print(f"Error en la solicitud. Código de estatus: {status_code}")




