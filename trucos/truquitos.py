#redondeo
pi = 3.14159
print(f'el numero de PI es: {pi:.4f}')

#uniendo elementos de una lista
colores = ['verde','azul','rojo']
print(' - '.join(colores))

#combinando bucles con salida
frutas = ['manzana','pera','mango']
print(*(f'Fruta: {fruta}' for fruta in frutas), sep=', ')

#formate de fechas
from datetime import datetime
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

#salida condicional
nota = 7
print('Aprobado' if nota >= 5 else 'Reporbado')

#salida de clave-valor en un diccionario
alumno = {'nombre': 'dani', 'promedio': 9.5}
print(' - '.join(f'{k}: {v}' for k, v in alumno.items()))

#repeticion de cadenas
cadena = 'ola'
print(cadena*9)