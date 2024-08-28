""" Ejercicio 8
    Objetivo: Ordenar y mostrar los países por su población.
    Instrucciones:
    -Usa el archivo paises.txt.
    -Lee el archivo, ordena los países por su población en orden descendente
    y muestra los resultados. """

import re

with open('ejercicios_txt\\un_members.txt','r',encoding='UTF-8') as lista_paises:
    contenido = lista_paises.read()
    paises = contenido.split('\n')

lista_paises_dict = []

for pais in paises:
    codigo, info = re.split(':', pais, 1)
    detalles = info.split(',')
    pais_dict = {
        'codigo': codigo,
        'pais': detalles[0],
        'capital': detalles[1],
        'dominio': detalles[2],
        'poblacion': int(detalles[3])
    }
    lista_paises_dict.append(pais_dict) #guardo con cada vuelta el pais

#ordenando los paises de formas descendente
lista_paises_ordenada = sorted(lista_paises_dict, key=lambda x:x['poblacion'], reverse=True)

for pais in lista_paises_ordenada:
    print(f'{pais['pais']}: {pais['poblacion']}')

'''
# Si quieres escribir los países ordenados a un archivo
with open('ejercicios_txt/paises_ordenados_por_poblacion.txt', 'w', encoding='UTF-8') as archivo:
    for pais in lista_paises_ordenada:
        archivo.write(f"{pais['codigo']}: {pais['pais']},{pais['capital']},{pais['dominio']},{pais['poblacion']}\n")
'''