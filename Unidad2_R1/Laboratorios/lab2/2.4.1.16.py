'''
Autor: Antonio Uribe Ramirez
lab: 2.3.1.18
fecha: 22/11/10
'''
def display_siete_segmentos(numero):
    patrones = [
        ["###", "# #", "# #", "# #", "###"],
        ["  #", "  #", "  #", "  #", "  #"],
        ["###", "  #", "###", "#  ", "###"],
        ["###", "  #", "###", "  #", "###"],
        ["# #", "# #", "###", "  #", "  #"],
        ["###", "#  ", "###", "  #", "###"],
        ["###", "#  ", "###", "# #", "###"],
        ["###", "  #", "  #", "  #", "  #"],
        ["###", "# #", "###", "# #", "###"],
        ["###", "# #", "###", "  #", "###"]
    ]

    for i in range(5):
        fila = " ".join(patrones[int(digito)][i] for digito in str(numero))
        print(fila)

numero_ingresado = int(input("Ingresa un número no negativo: "))
display_siete_segmentos(numero_ingresado)
