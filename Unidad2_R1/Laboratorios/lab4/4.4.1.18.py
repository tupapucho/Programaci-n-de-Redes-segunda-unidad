'''
Autor: Antonio Uribe Ramirez
lab: 4.4.1.18
fecha: 22/11/10
'''
import os

def buscar_directorio(ruta, dir_objetivo):
    if not os.path.exists(ruta):
        print("El directorio dado no existe.")
        return

    resultados = [os.path.join(raiz, dir_objetivo) for raiz, directorios, archivos in os.walk(ruta) if dir_objetivo in directorios]

    for resultado in resultados:
        print(resultado)

ruta = "./tree"
dir_objetivo = "python"

buscar_directorio(ruta, dir_objetivo)

