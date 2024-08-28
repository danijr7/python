#viene por defecto 'read'
#abriendo el archivo con 'with open'
with open('archivos\\texto_de_dani.txt',encoding='UTF-8') as archivo:
    #leemos el archivo
    contenido = archivo.read()
    print(contenido)
          
#no es necesario cerrarlo cuando usamos 'with open'