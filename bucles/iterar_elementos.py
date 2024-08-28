animales =  ['gato','perro','loro','cocodrilo','pez']
numeros = [1,2,3,4,5]
          
for numero,animal in zip(animales,numeros):
          print(numero)
          print(animal)

#forma para recorretr un elemento con su indice
for num in enumerate(numeros):
          indice = num[0]
          valor = num[1]
          print(f'el indice es: {indice} y el valor es: {valor}')
          
#usando el for/else
for numero in numeros:
          print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
          print('el bucle termino')