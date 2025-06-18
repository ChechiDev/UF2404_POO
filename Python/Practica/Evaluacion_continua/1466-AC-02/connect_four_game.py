import os
import random
import platform


"""
# Ejercicio

Desarrollar el juego completo de **Conecta Cuatro** en la terminal, en el que un jugador humano compite contra una **CPU con inteligencia variable** (`easy`, `normal`, `hard`).
El juego debe ser completamente funcional, visual y ejecutable desde consola.
"""
"""
## Objetivos

1. Practicar el uso de listas bidimensionales `board`
2. Control de flujo `if`, `for`, `while`
3. Funciones puras y control del estado
4. Desarrollo incremental y Q&A (”testeo”) de funciones
5. Pensamiento algorítmico: detección de victoria y lógica de CPU
"""
"""
## Hints

- Usa `board[:]` y listas por comprensión para copiar el tablero sin errores
- La sentencia `while True` permite ejecutar un conjunto de sentencias de código en Python hasta que se rompa la ejecución utilizando algún mecanismo como la palabra reservada `break`
- Añade comentarios en tu código
- Haz pruebas de cada parte por separado antes de combinar todo
"""
"""
## Extras

- Realizar una introducción al juego (animación)
- Permitir al jugador escoger colores de ficha (ANSI)
- Modo dos jugadores humanos
- Añadir dificultad `"insane"` con lógica más avanzada
- Crear un menú de elección
- Historial de partidas
"""

"""
Part 1: Crear el tauler »Crear una funció `create_board()` que retorni una matriu 6x7 de `.` »Crear una funció `print_board()` que el mostri per pantalla
Part 2: Inserir fitxes »Implementar la funció `insert_piece(board, column, piece)` »La fitxa ha de caure fins a la posició lliure més baixa
Part 3: Torns i validacions »Alternar els torns entre el jugador `X` i la CPU `0` »Verificar si la columna és vàlida abans de jugar
Part 4: Detecció de victòria »Crear una funció `check_win(board, piece)` »Ha de detectar 4 en ratlla en: »  Horitzontal »  Vertical »  Diagonal descendent (`/`) »  Diagonal ascendent (`\`)
Part 5: Intel·ligència de la CPU »Crear diferents funcions per a la CPU: »  `cpu_easy`: tria una columna aleatòria »  `cpu_normal`: intenta guanyar o bloquejar el jugador »  `cpu_hard`: utilitza una heurística per triar la millor jugada
Part 6: Flux del joc »Mostrar el tauler després de cada torn »Mostrar missatges de victòria o empat »Permetre triar la dificultat al començar el joc
"""


# Variabless globales para configuración del juego:
ROWS = 6
COLUMNS = 7


def clear_terminal():
    """
    Limpia la terminal
    """
    if platform.system() == "Windows":
        os.system("cls")

    else:
        os.system("clear")


def create_board(x: int, y: int) -> list:
    """
    Creates a board game grid\n
    Arg1 x: int: ROWS \n
    Arg2 y: int: COLUMNS\n
    Return: List: 2D array with the board generated
    """
    board = []

    # Generamos los números del header
    print("  ".join(str(n) for n in range(y)))

    # Generamos el board de juego.
    for i in range(x):
        row = []
        for j in range(y):
            row.append(". ")

        board.append(row)

    # print(type(board))
    return board


def print_board(board: list) -> list:
    """
    Muestra el tablero por pantalla\n
    Arg: 2D List\n
    Return: List: 2D array rendered in CMD.
    """

    # print(type(list))
    for row in board:
        print(" ".join(row))


def game():
    """
    Lógica principal del juego
    """
    # Limpiamos terminal:
    clear_terminal()

    board = create_board(ROWS, COLUMNS)
    print_board(board)


if __name__ == "__main__":
    game()