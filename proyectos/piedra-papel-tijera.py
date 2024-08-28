import random

# Lista de opciones posibles
opciones = ['piedra', 'papel', 'tijera']

# Función para la elección de la máquina
def eleccion_maquina():
    # Devuelve una elección aleatoria de la lista de opciones
    return random.choice(opciones)

# Función para determinar el ganador del juego
def determinar_ganador(eleccion_jugador, eleccion_pc):
    # Si ambas elecciones son iguales, es un empate
    if eleccion_jugador == eleccion_pc:
        return "Hay un empate..."
    # Se determina el ganador según las reglas del juego
    elif (eleccion_jugador == 'piedra' and eleccion_pc == 'tijera') or \
         (eleccion_jugador == 'papel' and eleccion_pc == 'piedra') or \
         (eleccion_jugador == 'tijera' and eleccion_pc == 'papel'):
        return "¡Ganas tú!"
    else:
        return "Gana la máquina :("

# Función principal para ejecutar el juego
def jugar():
    # Pregunta al usuario si quiere empezar el juego
    entrar_al_juego = input('¿Empezamos? (S/N) ').strip().lower()
    
    # Bucle que continúa mientras el usuario quiera seguir jugando
    while entrar_al_juego == 'si':
        # Pregunta al jugador por su elección
        eleccion_jugador = input('Elige piedra, papel o tijera: ').strip().lower()
        
        # Validación de la elección del jugador
        if eleccion_jugador not in opciones:
            print("Elección no válida. Por favor, elige entre piedra, papel o tijera.")
            continue
        
        # Elección de la máquina
        eleccion_pc = eleccion_maquina()
        print(f'La elección de la máquina es {eleccion_pc}')
        
        # Determina y muestra el resultado del juego
        resultado = determinar_ganador(eleccion_jugador, eleccion_pc)
        print(resultado)
        
        # Pregunta al usuario si quiere seguir jugando
        entrar_al_juego = input('¿Quieres seguir jugando? (S/N) ').strip().lower()
    
    # Mensaje de despedida
    print('El juego terminó. ¡Gracias por jugar!')

# Llamada a la función principal para iniciar el juego
jugar()