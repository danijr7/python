""" Ejercicio 3
    Objetivo: Muestre el nombre de cada pais.
    Instrucciones:
    -Usa el archivo paises.txt.
    -Cada línea representa un país. Escribe un script en Python
    que cuente el número de líneas (países) y muestre el total. """

import re

with open('ejercicios_txt_lectura\\un_members.txt',encoding='UTF-8') as lista_paises:
    contenido = lista_paises.read() #todo el texto
    paises = contenido.split('\n') #lista con cada linea
    
diccionario_paises = {}

for pais in paises:
    codigo, info = re.split(':', pais, 1)
    detalles = info.split(',')
    diccionario_paises[codigo] = {
        'pais': detalles[0],
        'capital': detalles[1],
        'dominio': detalles[2],
        'poblacion': int(detalles[3])
    }
    print(detalles[0])