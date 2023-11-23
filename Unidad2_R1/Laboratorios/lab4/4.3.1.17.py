class StudentsDataException(Exception):
    pass

class WrongLine(StudentsDataException):
    def __init__(self, line):
        self.line = line
        super().__init__("Línea incorrecta")

    def __str__(self):
        return f"{super().__str__()}: {self.line}"

class FileEmpty(StudentsDataException):
    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__("El archivo está vacío")

    def __str__(self):
        return f"{super().__str__()}: {self.file_name}"


def leer_notas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            if not archivo.readable():
                raise FileEmpty("El archivo no es legible.")

            notas = {}
            for linea in archivo:
                try:
                    nombre, apellido, puntos = linea.split()
                    puntos = float(puntos)
                    clave = f'{nombre} {apellido}'

                    if clave in notas:
                        notas[clave] += puntos
                    else:
                        notas[clave] = puntos
                except ValueError:
                    raise WrongLine(linea)

            if not notas:
                raise FileEmpty("El archivo está vacío.")
            
            return notas

    except FileNotFoundError:
        raise FileEmpty(f"El archivo {nombre_archivo} no se encontró.")


def imprimir_informe(notas):
    for clave, puntos in sorted(notas.items()):
        print(f'{clave.ljust(15)} {puntos}')


def main():
    try:
        nombre_archivo = input("Ingrese el nombre del archivo del profesor Jekyll: ")
        notas = leer_notas(nombre_archivo)
        imprimir_informe(notas)

    except StudentsDataException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
