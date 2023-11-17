'''
Programa: League of Legends Esports
Autor: Antonio Uribe Ramirez
Fecha de Creación: 16/11/2023
INGRESE: t1 para probar la api
KEY:1f71350e6dmsh8a8a1cb3f87e05cp167e02jsn1ad5190257b3
Descripción:
Este programa utiliza la API "league-of-legends-esports" a través de RapidAPI 
para obtener información detallada sobre equipos y jugadores de League of Legends. 
Los datos recuperados se presentan de manera organizada en la salida del programa.

Funciones:
make_api_request(team_id): Realiza una solicitud HTTP GET a la API para obtener información específica sobre un equipo. 
La respuesta se presenta en formato JSON.
print_team_info(team_data): Imprime de manera formateada en la salida estándar la información del equipo. 
Esta función toma los datos de la API como argumento.
main(): Función principal que maneja la interacción con el usuario. Utiliza un bucle para solicitar al usuario el ID del equipo, 
realiza la consulta a la API y presenta la información obtenida.

Variables y Estructuras de Control:
conn: Objeto de conexión HTTP a la API.
headers: Cabeceras requeridas para la autenticación en RapidAPI.
team_id: Almacena el ID del equipo ingresado por el usuario.
result: Almacena los datos devueltos por la API.
Bucle while: Permite al usuario realizar consultas múltiples hasta que decide salir.
Condición if: Verifica la entrada del usuario y gestiona la salida del programa.

Uso:
Ejecutar el programa e ingresar el ID del equipo cuando se solicite. 
La información del equipo se presentará de manera clara en la salida del programa.
'''

import http.client
import json

def make_api_request(team_id, api_key):
    conn = http.client.HTTPSConnection("league-of-legends-esports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': "league-of-legends-esports.p.rapidapi.com"
    }

    conn.request("GET", f"/teams?id={team_id}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode("utf-8"))

def print_team_info(team_data):
    team = team_data["data"]["teams"][0]
    print(f"Nombre del equipo: {team['name']}")
    print(f"Código del equipo: {team['code']}")
    print(f"Imagen del equipo: {team['image']}")
    print(f"Liga local: {team['homeLeague']['name']} ({team['homeLeague']['region']})")

    print("\nJugadores:")
    for player in team['players']:
        print(f"{player['summonerName']} ({player['role']})")

def main():
    api_key = input("Ingrese su clave de API: ").strip()

    while True:
        team_id = input("Ingrese el ID del equipo (o 'salir' para salir): ").strip()

        if team_id.lower() == 'salir':
            break

        if not team_id:
            print("Por favor, ingrese un ID de equipo válido.")
            continue

        try:
            result = make_api_request(team_id, api_key)
            print("\nInformación del equipo:")
            print_team_info(result)
        except Exception as e:
            print(f"Error al hacer la solicitud a la API: {e}")

if __name__ == "__main__":
    main()
