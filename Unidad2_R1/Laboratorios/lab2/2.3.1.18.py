'''
Autor: Antonio Uribe Ramirez
lab: 2.3.1.18
fecha: 22/11/10
'''
def mysplit(strng):
    return strng.split() if strng else []

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
