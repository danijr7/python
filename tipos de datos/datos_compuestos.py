#el tipo de dato es list
#el elemento empieza desde el 1 y el indice desde el 0
lista = ["Daniel Enrique", "Madre mia", True, 1.73]
tupla = ("Daniel Enrique", "Madre mia", True, 1.73) #las tuplas no se pueden modificar \ tupla[2] = False

print(lista[0])
print(tupla[0])

#creando un conjunto (set), no se puede cambiar ningun elemento pero se pueden reconstruir por completo al igual que las tuplas, se diferencia por no almacenar datos duplicados, no se accede a elementos por el indice
conjunto = lista = {"Daniel Enrique", "Madre mia", True, 1.73}
#print(conjunto[3])-> no puede acceder al elemento

#creando un diccionario (dict) la estructura es key: valor y separamos con comas
diccionario = {
          'nombre': "Daniel Enrique",
          'frase': "Madre mia",
          'situacion': True,
          'altura': 1.73,
          'duplicado': "Madre mia"
}