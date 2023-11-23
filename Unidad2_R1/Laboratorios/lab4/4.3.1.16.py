'''
Autor: Antonio Uribe Ramirez
lab: 4.3.1.16
fecha: 22/11/10
'''
def contar_letras(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            conteo_letras = {letra: 0 for letra in 'abcdefghijklmnopqrstuvwxyz'}

            for letra in archivo.read():
                if letra.isalpha():
                    conteo_letras[letra.lower()] += 1

            return conteo_letras
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no se encontró.')
        return {}

def main():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    conteo_letras = contar_letras(nombre_archivo)

    if conteo_letras:
        histograma = sorted(conteo_letras.items(), key=lambda item: item[1], reverse=True)
        for letra, cantidad in histograma:
            if cantidad > 0:
                print(f'{letra} -> {cantidad}')

        nombre_salida = nombre_archivo + '.hist'
        with open(nombre_salida, 'w') as archivo_salida:
            archivo_salida.writelines([f'{letra} -> {cantidad}\n' for letra, cantidad in histograma])

if __name__ == "__main__":
    main()
