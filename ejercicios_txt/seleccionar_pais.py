""" Ejercicio 6
    Objetivo: Buscar y mostrar la información de un país específico.
    Instrucciones:
    -Usa el archivo paises.txt.
    -Escribe un script que permita al usuario ingresar un código de país
    (por ejemplo, "US") y luego muestra toda la información sobre ese país. """

import re

def info_pais(lista):
    print(f'-Pais:  {lista[0]}\n'
          f'-Capital: {lista[1]}\n'
          f'-Dominio: {lista[2]}\n'
          f'-Poblacion: {lista[3]}')

with open('ejercicios_txt_lectura\\un_members.txt',encoding='UTF-8') as lista_paises:
    contenido = lista_paises.read() #todo el texto
    paises = contenido.split('\n') #lista con cada linea
    
diccionario_paises = {}
    
input = input('Introduce el codigo del pais: ').upper()
    
for pais in paises:
    codigo, info = re.split(':', pais, 1)
    detalles = info.split(',')
    diccionario_paises[codigo] = {
        'pais': detalles[0],
        'capital': detalles[1],
        'dominio': detalles[2],
        'poblacion': int(detalles[3])
    }
        
    if input == codigo:
        info_pais(detalles)