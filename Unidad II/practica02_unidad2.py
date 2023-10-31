import http.client
import urllib.parse

while True:
    user_input = input("Ingresa el nombre de la canción que deseas buscar en Spotify (o escribe 'Salir' o 'S' para terminar): ")

    if user_input.lower() in ['salir', 's']:
        print("¡Programa terminado!")
        break

    try:
        conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")
        
        querystring = urllib.parse.urlencode({
            "q": user_input,
            "type": "track",
            "limit": "10",
            "offset": "0"
        })
        
        headers = {
            'X-RapidAPI-Key': "1f71350e6dmsh8a8a1cb3f87e05cp167e02jsn1ad5190257b3", 
            'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
        }

        conn.request("GET", "/search/?" + querystring, headers=headers)
        res = conn.getresponse()

        # Verifica el código de estado de la respuesta
        if res.status == 200:
            data = res.read()
            print(f"Código de estado: {res.status}")
            print(data.decode("utf-8"))
        else:
            print(f"Error al hacer la solicitud. Código de estado: {res.status}")

    except Exception as e:
        print(f"Error: {str(e)}")



