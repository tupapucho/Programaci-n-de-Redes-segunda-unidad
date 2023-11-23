def contar_letras(nombre_archivo):
    try:
        with open(nombre_archivo.lower(), 'r') as archivo:
            conteo_letras = {letra: 0 for letra in 'abcdefghijklmnopqrstuvwxyz'}

            for letra in archivo.read():
                if letra.isalpha():
                    conteo_letras[letra.lower()] += 1

            return conteo_letras
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no se encontró.')
        return {}

def imprimir_histograma(conteo_letras):
    for letra, cantidad in sorted(conteo_letras.items()):
        if cantidad > 0:
            print(f'{letra} -> {cantidad}')

def main():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    conteo_letras = contar_letras(nombre_archivo)
    
    if conteo_letras:
        imprimir_histograma(conteo_letras)

if __name__ == "__main__":
    main()


