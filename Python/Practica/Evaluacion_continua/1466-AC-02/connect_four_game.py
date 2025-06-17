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


def create_board(x, y):
    matrix = []

    for i in range(x):
        row = []
        for j in range(y):
            if (i == 0):
                row.append(str(j))

            else:
                row.append(".")

        matrix.append(row)

    # Comprobamos matriz
    print(type(matrix))

    # Mostramos contenido de la lista 2D:
    for row in matrix:
        print(" ".join(row))


def game():
    """
    Lógica principal del juego
    """
    clear_terminal()
    board = create_board(ROWS, COLUMNS)

if __name__ == "__main__":
    game()