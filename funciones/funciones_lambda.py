numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

#creando una funcion lambda
multiplicacion = lambda x : x*2

#creando una funcion para determinar si es par o no
def es_par(num):
          if (num%2==0):
                    return True

numero_pares = filter(es_par,numeros)

#haciendo los mismo pero com lambda
numero_pares =  filter(lambda numero:numero % 2 == 0,numeros) #filtra los numeros que son pares
print(list(numero_pares)) #lo muestra en forma de lista