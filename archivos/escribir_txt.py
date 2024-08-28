with open('archivos\\texto_de_dani.txt','w',encoding='UTF-8') as archivo:
    #sobreescribiendo el archivo
    #archivo.write('jiijijij puto el que lee') solo escribe 1 linea
    archivo.writelines(['hola putito\n','ronaldo mas q messi\n','chupala\n'])
    #agregando otras 2 lineas
    archivo.writelines(['3era linea de prueba\n','esta es la ultima vez'])