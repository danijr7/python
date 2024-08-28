#Funciones Integradas (Build In)

numeros = [1,2,3,4,5]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.345678,2) #despues de la coma se indica la cantidad de decimales
print(numero)

#retorna False--> 0, vacio, False, None / True--> distinto a 0, True, cadena, datos no vacios
resultado_bool = bool(None)
print(resultado_bool)

#retorna True, si todos los valores son verdaderos
resultado_all = all([123,'jijiji'])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)