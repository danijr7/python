#creando una funcion que muestre la serie fibonacci entre el 0 y el numero dado

def nums_fibonacci(num):
          sums = []
          num1,num2 = 0,1 #inicializamos las variables
          while num2 < num:
                    sums.append(num2) #integramos a la lista cada suma
                    num1,num2 = num2,num1 + num2 #actualizamos las variables a sumar
          return sums

resultado = nums_fibonacci(100)
print(resultado)