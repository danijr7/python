""" Ejercicio 2
    Objetivo: Cuenta el número de líneas en el archivo de texto.
    Instrucciones:
    -Usa el archivo paises.txt.
    -Escribe un script en Python que cuente cuántas líneas hay en el archivo y muestre ese número. """

with open('ejercicios_txt_lectura\\un_members.txt',encoding='UTF-8') as lista_paises:
    linea = lista_paises.read()
    lista = linea.split('\n')
    cant_lineas = len(lista)
    print(cant_lineas) #output: 191