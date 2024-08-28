import random
#mostrando tabla
def mostrando_tabla(tabla):
          print(f'({tabla[0][0]}) | ({tabla[0][1]}) | ({tabla[0][2]}) \n')
          print('----------')
          print(f'({tabla[1][0]}) | ({tabla[1][1]}) | ({tabla[1][2]}) \n')
          print('----------')               
          print(f'({tabla[2][0]}) | ({tabla[2][1]}) | ({tabla[2][2]}) \n')
#modificando la tabla cada vez que toque
def actualizando_tabla(desicion_jugador,X_u_O):
          #recorriendo primera fila
          if desicion_jugador == posiciones[0][0]:
                    posiciones[0][0] =  f'{X_u_O}'
                    posibles[0].remove(1)
          elif desicion_jugador == posiciones[0][1]:
                    posiciones[0][1] =  f'{X_u_O}'
                    posibles[0].remove(2)
          elif desicion_jugador == posiciones[0][2]:
                    posiciones[0][2] =  f'{X_u_O}'
                    posibles[0].remove(3)
          #recorriendo segunda fila
          elif desicion_jugador == posiciones[1][0]:
                    posiciones[1][0] =  f'{X_u_O}'
                    posibles[1].remove(4)
          elif desicion_jugador == posiciones[1][1]:
                    posiciones[1][1] =  f'{X_u_O}'
                    posibles[1].remove(5)
          elif desicion_jugador == posiciones[1][2]:
                    posiciones[1][2] = f'{X_u_O}'
                    posibles[1].remove(6)
          #recorriendo tercela fila
          elif desicion_jugador == posiciones[2][0]:
                    posiciones[2][0] = f'{X_u_O}'
                    posibles[2].remove(7)
          elif desicion_jugador == posiciones[2][1]:
                    posiciones[2][1] = f'{X_u_O}'
                    posibles[2].remove(8)
          elif desicion_jugador == posiciones[2][2]:
                    posiciones[2][2] = f'{X_u_O}'
                    posibles[2].remove(9)
          else:
                    print('*~Esa posocion ya fue elegida~*')
#haciendo que la computadora elija re random una posicion
def eleccion_pc(X_u_O):
          #eligiendo una lista random
          lista = random.choice(posibles)
          #eligiendo el numero random de una lista random
          eleccion = random.choice(lista)
          actualizando_tabla(eleccion,X_u_O_pc)

def verificando_ganador():
    # Define las posibles líneas ganadoras (filas, columnas, diagonales)
    lineas_ganadoras = [
        [posiciones[0][0], posiciones[0][1], posiciones[0][2]],  # Fila 1
        [posiciones[1][0], posiciones[1][1], posiciones[1][2]],  # Fila 2
        [posiciones[2][0], posiciones[2][1], posiciones[2][2]],  # Fila 3
        [posiciones[0][0], posiciones[1][0], posiciones[2][0]],  # Columna 1
        [posiciones[0][1], posiciones[1][1], posiciones[2][1]],  # Columna 2
        [posiciones[0][2], posiciones[1][2], posiciones[2][2]],  # Columna 3
        [posiciones[0][0], posiciones[1][1], posiciones[2][2]],  # Diagonal principal
        [posiciones[0][2], posiciones[1][1], posiciones[2][0]],  # Diagonal secundaria
    ]

    for linea in lineas_ganadoras:
        if linea[0] == linea[1] == linea[2] and linea[0] in ('X', 'Y'):
            ganador = f'El ganador es ~{linea[0]}~'
            print(ganador)
            return ganador.startswith('El ganador es')
    
    return False  # No hay ganador


#accediendo_posicion = posiciones[fila][columna]
posiciones = [[1,2,3],[4,5,6],[7,8,9]]
posibles = [[1,2,3],[4,5,6],[7,8,9]]
ganador = False
X_u_O_pc = ''

#pidiendo al usuario el caracter con el que jugar
X_u_O_jugador = input('Elige X/Y para jugar: ')
X_u_O_jugador = X_u_O_jugador.upper()

#asegurando que la pc sea el caracter contrario a la persona
if X_u_O_jugador == 'X':
          X_u_O_pc = 'Y'
elif X_u_O_jugador == 'Y':
          X_u_O_pc = 'X'

#verificando que X/Y
if X_u_O_jugador == 'X' or X_u_O_jugador == 'Y':
          pass
else:
          while X_u_O_jugador != 'X' and X_u_O_jugador != 'Y':
                    X_u_O_jugador = input('Solo puedes elegir X/Y, vuelve a intentarlo: ')
                    X_u_O_jugador = X_u_O_jugador.upper()
mostrando_tabla(posiciones)

while ganador == False:
          desicion_jugador = int(input('*Elige una posicion de la tabla: '))
          actualizando_tabla(desicion_jugador,X_u_O_jugador)
          mostrando_tabla(posiciones)
          eleccion_pc(X_u_O_jugador)
          print('~~~~~~~Esta es la tabla actualizada~~~~~~~~~~~')
          mostrando_tabla(posiciones)
          verificando_ganador()