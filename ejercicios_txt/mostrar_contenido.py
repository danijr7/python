'''
Ejercicio 1
    Objetivo: Lee el archivo de texto y muestra todo su contenido en la consola.
    Instrucciones:
    -Crea un archivo de texto llamado paises.txt con el contenido proporcionado.
    -Escribe un script en Python que abra el archivo, lea todo su contenido y lo imprima.
'''
with open('ejercicios_txt_lectura\\un_members.txt',encoding='UTF-8') as lista_paises:
    contenido = lista_paises.read()
    print(contenido)