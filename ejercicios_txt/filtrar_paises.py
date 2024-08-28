""" Ejercicio 7
    Objetivo: Filtrar la información y guardarla en un nuevo archivo.
    Instrucciones:
    -Usa el archivo paises.txt.
    -Escribe un script que filtre los países con una población mayor a
    50 millones y guarda esa información en un nuevo archivo llamado
    paises_grandes.txt. """

import re

with open('ejercicios_txt\\un_members.txt',encoding='UTF-8') as lista_paises:
    contenido = lista_paises.read() #todo el texto
    paises = contenido.split('\n') #lista con cada linea
    
diccionario_paises = {}
paises_filtrados = []
    
for pais in paises:
    codigo, info = re.split(':', pais, 1)
    detalles = info.split(',')
    diccionario_paises[codigo] = {
        'pais': detalles[0],
        'capital': detalles[1],
        'dominio': detalles[2],
        'poblacion': int(detalles[3])
    }
    
    if int(detalles[3]) >= 50000000:
        paises_filtrados.append(detalles)

with open('ejercicios_txt\\paises_de_50m+.txt','w',encoding='UTF-8') as archivo:
    for detalles in paises_filtrados:
        archivo.write(','.join(detalles) + '\n')