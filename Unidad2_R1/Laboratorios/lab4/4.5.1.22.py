from datetime import datetime

# Crear objeto datetime para el 4 de noviembre de 2020, 14:53:00
dt_obj = datetime(2020, 11, 4, 14, 53, 0)

# Imprimir resultados formateados
print(dt_obj.strftime("%Y/%m/%d %H:%M:%S"))
print(dt_obj.strftime("%y/%B/%d %I:%M:%S %p"))
print(dt_obj.strftime("%a, %Y %b %d"))
print(dt_obj.strftime("%A, %Y %B %d"))
print("Día de la semana:", dt_obj.strftime("%w"))
print("Día del año:", dt_obj.strftime("%j"))
print("Número de semana en el año:", dt_obj.strftime("%U"))
