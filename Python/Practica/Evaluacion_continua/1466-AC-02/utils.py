import os
import re
import platform as plat



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


    def copy_board(board: list) -> list:
        pass


    def valid_column(board, column):
        """
        Devuelve True si la columna es válida (entre 0 y 6 y no está llena)
        """
        pass


    def get_valid_columns(board):
        """
        Devuelve una lista de columnas válidas para jugar
        ➜ Utiliza valid_column para filtrar las columnas disponibles
        """
        pass