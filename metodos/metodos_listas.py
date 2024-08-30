#creando una lista con list()
lista = list(['hola', 'daniel', 18])
lista2 = list([3,True,6,9,False,2,5,8,True,1,4,7])

resultado = len(lista) #me devuelve la cantidad de elementos de la lista
lista.append("JAJAJAJAJJAJAA") #agrega un elemento a la lista
lista.insert(3, 'madre mia el bicho') #agrega un elemento a la lista en una posicion especifica
lista.extend([False,5269]) #agrega una lista a otra lista
lista.pop(2) #elimina un elemento de la lista por su posicion (para eliminar el ultimo indice ponemos -1, penultimo -2,...)
lista.remove('daniel') #remueve un elemento de la lista por su valor, si encuentra una coincidencia lo elimina sino lanza una excepcion
lista2.sort(reverse = True) #ordena la lista de manera ascendente (si usamos el parametro <reverse = True> los ordena en reversa)
lista.reverse() #invierte los elementos de una lista
#lista.clear() #elimina todos los elementos de la lista
print(lista)

#creando una lista con un rango especifico
numbers = [x for x in range(100)]
print(numbers)
