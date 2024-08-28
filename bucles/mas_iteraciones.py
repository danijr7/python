frutas = ['banana','manzana','ciruela','pera','naranja','granada','durazno']
cadena = 'hola dani'
numeros = [1,2,3,4,5,6,7,8,9]

#saltando un valor dentro del bucle
for fruta in frutas:
          if fruta == 'granada':
                    continue
          print(f'-me voy a comer una {fruta}')
          
#poner un limite en el bucle con un valor (el 'else' no se ejecuta desp de un break)
for fruta in frutas:
          if fruta == 'pera':
                    break
          print(f'*yo como {fruta}')
          
print('*bucle terminado')

#recorrer una cadena de texto
for letra in cadena:
          print(letra)
          
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)