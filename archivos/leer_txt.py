#usando open para abrir un archivo
archivo_sin_leer = open('archivos\\texto_de_dani.txt',encoding='UTF-8')

#leer el archivo completo
#archivo_leido = archivo_sin_leer.read()

#leer linea por linea, creandome una lista separadas por cada linea
#lineas = archivo_sin_leer.readlines()

""" contents[]
with open('example.txt','r') as f:
    #contents = f.readlines()
print(contents[5]) Print the 6th line on the screen """

'''/////////////////////////////////////////////////////////////'''
#leer una sola linea (al poner un numero en el '(1)' indicamos la cantidad de caracteres que queremos q lea)
#lo que lee se guarda en la variable
linea = archivo_sin_leer.readline()

#cierrar el archivo
archivo_sin_leer.close()

print(linea)