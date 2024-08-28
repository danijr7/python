import csv

with open('archivos\\datos.csv',encoding='UTF-8') as archivo:
          reader = csv.reader(archivo)
          for fila in reader:
                    print(fila)