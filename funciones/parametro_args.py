#utilizando * como argumento(*args)
def suma(nombre,*numero): #se puede poner varios items
          return f'{nombre}, tu suma es: {sum(numero)}'

resultado = suma('tony',2,4,52,4,5)
print(resultado)

""" ------------------------ """

def suma_total(numeros):
          return sum([*numeros])

resultado_2 = suma_total([1,6563,129,5])
print(resultado_2)