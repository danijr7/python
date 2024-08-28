"string" #se usa para una sola linea
'string' #se usa para una sola linea

"""string
   string
   string""" #se usa para varias lineas que sino se le asigna ninguna variable se lee como un comentario
   
'''string
   string
   string''' #se usa para varias lineas que sino se le asigna ninguna variable se lee como un comentario
          
40
40.2

False
True



nombre = 'dani'
edad = 19
pi = 3.14159
ciudad = 'Maracaibo'
#los corchetes {} actúan como marcadores de posición
mensaje = 'me llamo {} y tengo {} de edad.'.format(nombre,edad)
print(mensaje)

#puedes especificar el indice de los argumenos dentro de los corchetes
mensaje = 'me llamo {0} y tengo {1} de edad. claramente mi noombre es {0}'.format(nombre,edad)
print(mensaje)

#puedes usar palabras claves en lugar de posiciones
mensaje = 'me llamo {nombre} y tengo {edad} de edad.'.format(nombre = 'juan',edad = 78)
print(mensaje)

#fijando la cantidad de decimales
mensaje = 'el valor de pi es aproximadamente {:.2f}'.format(pi)
print(mensaje)

#construir cadenas mas complejas
mensaje = 'me llamo {0}, tengo {1} de edad y soy de {2}.'.format(nombre,edad,ciudad)
print(mensaje)

