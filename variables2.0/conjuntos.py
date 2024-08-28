#creando un conjunto con set()
conjunto = set(['dato1','dato en lista 1','dato en lista 2'])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1','dato2'])
conjunto2 = {conjunto1,'dato3','dato4'}

#print(conjunto2)

#teoria de conjunto

conjunto1 = {1,2,3,4,5,6,7,8,9}
conjunto2 = {1,3,5,7,9}

#verificnado si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificnado si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 >= conjunto2

#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1) #para que de True no tiene q haber ninguna coincidencia, si  la hay da False

print(resultado)