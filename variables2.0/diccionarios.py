#creando diccionarios con dic() (solo se pueden crear datos vacios de esta manera)
diccionario = dict(nombre = 'dani', apellido = 'gu')

#las listas/conjunto no pueden ser claves pq son mutables (amenos que se use la funcion <frozenset()>), pero las tuplas si pueden
diccionario = {('daniel','barto'):"jsjsjs"}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(['ABCD','HGIJK','MADRE'])
diccionario = dict.fromkeys('abcd','hola')#da el valor de 'hola' a todas las keys del primero('abcd')
#print(diccionario['MADRE'])

print(diccionario)