import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv('archivos\\datos.csv')
df2 = pd.read_csv('archivos\\datos.csv')

#obteniendo los datos de la columna 'nombre'
nombres = df['nombre']

#especificamos desde donde hasta donde recorre la cadena utilizando slicing
cadena = '0123456789'
""" print(cadena[2:7]) """

#ordenando el dataFrame por la edad
df_ordenado_ascendente = df.sort_values('edad')

#ordenando el dataframe por la edad de mandera descendente
df_ordenado_descendente = df.sort_values('edad',ascending=False)

#concatenando los 2 dataFrames
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 filas con head()
primeras_filas = df.head(3)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataFrame:
df_info = df.describe()

#accediendo a un elemento especifico del df con loc[]
elemento_especifico_loc = df.loc[3,'edad']

#accediendo a un elemento especifico del df solo por el indice con iloc['fila','columna']
elemento_especifico_loc = df.iloc[3,2]

#accediendo a todos los apellidos con iloc
apellido = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad > 30
mayor_30 = df.loc[df['edad'] > 30,:]

print(mayor_30)