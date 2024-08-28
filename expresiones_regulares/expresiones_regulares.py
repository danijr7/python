import re

texto = '''hola chaval. #$ esta es 1. 7. una cadena 48, q pasa tio? 456872 final
          esta es la segunda 265f linea @%^. aababbb ababbb final
          esta es (&*) la 9. linea final. final'''

#haciendo una busqueda simple
""" resultado = re.findall('esta',texto) """

#\d --> busca digitos numericos del 0 - 9
""" resultado = re.findall(r'\d',texto) """

#\D --> busca TODO MENOS digitos numericos del 0 - 9
""" resultado = re.findall(r'\D',texto) """

#\w --> busca caracteres alphanumericos [a-z A-Z 0-9 '_']
""" resultado = re.findall(r'\w',texto) """

#\W --> busca TODO MENOS caracteres alphanumericos [a-z A-Z 0-9 '_']
""" resultado = re.findall(r'\W',texto) """

#\s --> busca espacios en blanco --> espacios, tabs, saltos de linea
""" resultado = re.findall(r'\s',texto) """

#\S --> busca TODO MENOS espacios en blanco --> espacios, tabs, saltos de linea
""" resultado = re.findall(r'\S',texto) """

#. --> busca TODO MENOS saltos en linea
""" resultado = re.findall(r'.',texto) """

#\n --> busca espacios en blanco --> espacios, tabs, saltos de linea
""" resultado = re.findall(r'\n',texto) """

#\ --> cancela caracteres especiales, cancelando la funcion del punto y buscnado puntos
""" resultado = re.findall(r'\.',texto) """

#armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(f'\d\.\s',texto)

#^ --> busca el comienzo de una linea. (flags=re.M) analiza varias lineas
resultado = re.findall(f'^esta',texto,flags=re.M)

#$ --> busca el final de una linea
resultado = re.findall(f'final$',texto,flags=re.M)

#{n} --> busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}\s',texto)

#{n,m} --> al menos 'n' veces, como maximo 'm' veces (cortando un calor que haya de mas)
resultado = re.findall(r'\d{1,5}',texto)

#{n,m} --> al menos 'n' veces, como maximo 'm' veces (cortando un calor que haya de mas)
#los parametros solo afectan a caracter que este a la izquierda, a menos que lo volvamos un grupo co '()'
resultado = re.findall(r'(ab){2,4}',texto) #devuelva (1) por cada vez que se cumpla el parametro

# | --> busca una u otra
resultado = re.findall(r'\d{1,5}|esta',texto)

print(resultado)