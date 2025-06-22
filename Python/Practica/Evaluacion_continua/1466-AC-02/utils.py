import os
import re
import platform as plat
from board import Board



class Utils:
    @staticmethod
    def clear_terminal():
        if plat.system() == "Windows":
            os.system("cls")

        else:
            os.system("clear")


    def valid_column_num(player_name=None, piece=None) -> int:
        pattern = r"^[1-7]$"

        while True:
            # Utils.clear_terminal()
            value = input(f"\n{player_name} (X) Elige columna (1-7): ")
            if re.match(pattern, value):
                return int(value) - 1

            else:
                print("Error!")
                continue


    @staticmethod
    def choose_name() -> str:
        """
        Asks the user for their name and returns it.
        """
        name = input("\nPlease, enter your name: ").strip()

        return name


    @staticmethod
    def choose_difficulty(name):
        while True:
            nivel = input(f"{name} elige la dificultad [easy] [normal] [hard]: ").strip().lower()

            if nivel in ["easy", "normal", "hard"]:
                return nivel

            print("➜ [ERROR] Nivel incorrecto")


    def check_winner(board, piece):
        grid = board._board
        rows = board._row
        cols = board._col

        # Checkeamos Horizontal
        for r in range(rows):
            for c in range(cols - 3):
                if(
                    grid[r][c] == piece and
                    grid[r][c + 1] == piece and
                    grid[r][c + 2] == piece and
                    grid[r][c + 3] == piece
                ):
                    return True

        # Vertical
        for c in range(cols):
            for r in range(rows - 3):
                if (grid[r][c] == piece and
                    grid[r + 1][c] == piece and
                    grid[r + 2][c] == piece and
                    grid[r + 3][c] == piece):
                    return True

        # Diagonal positiva
        for r in range(rows - 3):
            for c in range(cols - 3):
                if (grid[r][c] == piece and
                    grid[r + 1][c + 1] == piece and
                    grid[r + 2][c + 2] == piece and
                    grid[r + 3][c + 3] == piece):
                    return True

        # Diagonal negativa
        for r in range(3, rows):
            for c in range(cols - 3):
                if (grid[r][c] == piece and
                    grid[r - 1][c + 1] == piece and
                    grid[r - 2][c + 2] == piece and
                    grid[r - 3][c + 3] == piece):
                    return True

        return False


    def flood_fill_algorithm(board, row, col, piece, checked=None):
        """

        """

        # Si es la primera vez creamos una lista con los visitados:
        if checked is None:
            checked = []

            print(f"Empieza flood fill en {row}, {col}")

        # Comprobamos si la posición está fuera del board:
        if row < 0 or row >= len(board):
            print(f"({row}, {col}), row está fuera del board")
            return 0

        if col < 0 or col >= len(board[0]):
            print(f"({row}, {col}), col está fuera del board")
            return 0

        # Comprobamos si se ha checkeado la casilla:
        if (row, col) in checked:
            print(f"({row}, {col}, checked)")
            return 0


        # Comprobamos si la casilla es la pieza que buscamos:
        if board[row][col] != piece:
            return 0

        checked.append((row, col))
        print(f"Visitado: {row}, {col} => checked {checked}")
        count = 1

        # Recursividad en las 4 direcciones:
        count += Utils.flood_fill_algorithm(board, row + 1, col, piece, checked)
        count += Utils.flood_fill_algorithm(board, row - 1, col, piece, checked)
        count += Utils.flood_fill_algorithm(board, row, col + 1, piece, checked)
        count += Utils.flood_fill_algorithm(board, row, col - 1, piece, checked)

        return count


# Probando & debug flood fill algorithm
if __name__ == "__main__":

    Utils.clear_terminal()

    board = [
        [".", ".", ".", "X", "X", ".", ".", ],
        [".", ".", ".", "X", ".", ".", ".", ],
        [".", ".", "X", "X", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ],
        [".", ".", ".", ".", ".", ".", ".", ],
    ]

    # printamos el board:
    for r in board:
        print(" ".join(r))
    print()

    row_inicio = 0
    col_inicio = 4
    piece = "X"
    checked = []

    result = Utils.flood_fill_algorithm(board, row_inicio, col_inicio, piece, checked)
    print(f"Fichas conectadas: {result}")
    print(f"posiciones visitadas: {checked}")