import tkinter as tk
from tkinter import messagebox

# Variables del juego
player = 'X'  # Variable que almacena el jugador actual ('X' o 'O')
game_over = False  # Variable para determinar si el juego ha terminado

# Función para verificar si hay un ganador
def check_winner():
    # Verifica filas y columnas
    for i in range(3):
        # Verifica si todas las casillas de una fila son iguales y no están vacías
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        # Verifica si todas las casillas de una columna son iguales y no están vacías
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
    # Verifica las diagonales
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    # Si no se encuentra un ganador, retorna False
    return False

# Función que se llama al hacer clic en un botón (casilla)
def button_click(row, col):
    global player, game_over
    
    # Si la casilla está vacía y el juego no ha terminado
    if buttons[row][col]['text'] == '' and not game_over:
        # Coloca el símbolo del jugador en la casilla
        buttons[row][col]['text'] = player
        # Cambia el color de fondo según el jugador
        buttons[row][col]['bg'] = '#37474F' if player == 'X' else '#455A64'
        
        # Verifica si hay un ganador después de la jugada
        if check_winner():
            messagebox.showinfo('Ganador', f'Jugador {player} gana!!!')  # Muestra un mensaje indicando el ganador
            game_over = True  # Marca el juego como terminado
        # Verifica si todas las casillas están llenas sin que haya un ganador (empate)
        elif all(buttons[row][col]['text'] != '' for row in range(3) for col in range(3)):
            messagebox.showinfo('Empate', '¡Es un empate!!!')  # Muestra un mensaje indicando empate
            game_over = True  # Marca el juego como terminado
        else:
            # Cambia el jugador para el siguiente turno
            player = 'O' if player == 'X' else 'X'

# Función para reiniciar el juego
def reset_game():
    global player, game_over
    player = 'X'  # Reinicia el jugador inicial a 'X'
    game_over = False  # Marca el juego como no terminado
    # Reinicia todas las casillas del tablero
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''  # Limpia el texto de cada casilla
            buttons[row][col]['bg'] = '#263238'  # Restablece el color de fondo original

# Configuración de la ventana principal de la interfaz gráfica
root = tk.Tk()
root.title('Tic Tac Toe')  # Título de la ventana
root.geometry('400x450')  # Tamaño de la ventana
root.configure(bg='#263238')  # Color de fondo de la ventana

# Marco que contiene los botones del tablero
frame = tk.Frame(root, bg='#263238')
frame.place(relx=0.5, rely=0.5, anchor='center')  # Coloca el marco en el centro de la ventana

# Creación de una matriz de botones (3x3) para el tablero
buttons = [[tk.Button(frame, text='', font='normal 20 bold', width=5, height=2, bg='#263238', fg='white',
                      command=lambda row=row, col=col: button_click(row, col))  # Llama a button_click con la fila y columna correspondientes
            for col in range(3)] for row in range(3)]

# Posiciona cada botón en la cuadrícula del marco
for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col, padx=10, pady=10)  # Agrega un margen entre los botones

# Botón para reiniciar el juego
reset_button = tk.Button(root, text='Reiniciar', font='normal 15 bold', command=reset_game,
                         bg='#546E7A', fg='white')
reset_button.place(relx=0.5, rely=0.9, anchor='center')  # Coloca el botón de reinicio en la parte inferior de la ventana

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()