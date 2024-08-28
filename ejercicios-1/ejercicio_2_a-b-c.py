texto = input('porfavor inserte una frase o texto que quiera: ')
texto = texto.split(' ')
cant_palabras = len(texto)
tiempo = cant_palabras / 2

if tiempo > 60:
          print(f'{cant_palabras} palabras!!! hdp... tampoco me contes tu vida...')
else:
          print(f'>Esta frase se tarda {tiempo}s en ser dicha.')
          print(f'>Por lo que dice un a en total {cant_palabras} de palabras')

tiempo_dalto = (0.7 * cant_palabras) / 2
print(f'y dalto lo diria en {tiempo_dalto}s jijijijiji')