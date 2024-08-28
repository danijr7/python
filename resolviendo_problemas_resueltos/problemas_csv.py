#cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv('resolviendo_problemas_resueltos\\datos.csv')

#convertir a 'string' los datos de una columna
df ['edad'] = df['edad'].astype(str)

#reemplazando un valor de la columna nombre
""" df['apellido'].replace('mitre','ElBarto',inplace=True) """

#eliminando las filas con datos vacios
""" df = df.dropna() """

#eliminandoo columnas
""" df = df.dropna(axis='numero_de_fila') """

#eliminamos filas repetidas
df = df.drop_duplicates()

#creando un CSV con el dataFrame resultante (limpio)
df.to_csv('resolviendo_problemas_resueltos\\datos_limpios.csv')
