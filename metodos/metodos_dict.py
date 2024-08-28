diccionario = {
          'nombre': 'daniel',
          'apellido': 'acevedo',
          'edad': 19
}

claves = diccionario.keys() #devuelve el nombre de las claves (tamb nos sirve para iterar)
claves = diccionario.get('edad') #devuelve el contenido de las claves y sino encuentra nada devuelve 'none' y continua con el programa
diccionario.pop('apellido') #elimina un elemento del diccionario
claves = diccionario.items() #lo estamos iterando, es decir estamos recorriendo el elemento

#diccionario.clear() #elimina todo el diccionario

print(claves)