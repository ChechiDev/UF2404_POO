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
        pattern = r"^[0-6]$"

        while True:
            # Utils.clear_terminal()
            value = input(f"\n{player_name} (X) Elige columna (0-6): ")
            if re.match(pattern, value):
                return int(value)

            else:
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