#crear una funcion que devuelva los numeros primos entre el 0 y el numero ingresado
#un número primo es un número natural mayor que 1 que tiene únicamente dos divisores positivos distintos: él mismo y el 1

def es_primos(num):
          for i in range(2,num-1): #'i' incrementa con cada vuelta y empieza a partir del 2 hasta el anterior numero del ingresado
                    if num%i==0: return False
          return True

def primos_hasta(num):
          primos = [] #creando la lista para agregar los numeros primos
          for i in range(3,num+1): #que recorra cada numero desde el 1 hasta el numero ingresado
                    resultado = es_primos(i) #guardar el resultado de la funcion
                    if resultado == True: #si es Trues es pq es primo
                              primos.append(i) #agregando el numero a la lista
          return primos

resultado = primos_hasta(98)
print(resultado)