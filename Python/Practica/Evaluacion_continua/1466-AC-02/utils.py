import os
import re
import platform as plat
from board import Board



class Utils:
    @staticmethod
    def clear_terminal():
        """
        Clears the terminal screen based on the user's operating system.
        """
        if plat.system() == "Windows":
            os.system("cls")

        else:
            os.system("clear")


    def valid_column_num(player_name=None, piece=None) -> int:
        """
        Asks the user to select a valid column number for their move.

        Args:
            player_name (str, optional): The name of the player.
            piece (str, optional): The piece symbol for the player.

        Returns:
            int: The selected valid column number (1-7).
        """
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
        Asks the user to enter their name.

        Returns:
            str: The entered player name.
        """
        name = input("\nPlease, enter your name: ").strip()

        return name


    @staticmethod
    def choose_difficulty(name):
        """
        Asks the user to select a difficulty level for the game.

        Args:
            name (str): The name of the player.

        Returns:
            str: The selected difficulty level ('easy', 'normal', or 'hard').
        """
        while True:
            nivel = input(f"{name} elige la dificultad [easy] [normal] [hard]: ").strip().lower()

            if nivel in ["easy", "normal", "hard"]:
                return nivel

            print("➜ [ERROR] Nivel incorrecto")


    def check_winner(board: list, piece: str) -> bool:
        """
        Checks if the specified piece has achieved a winning condition (four in a row)
        horizontally, vertically, or diagonally on the board.

        Args:
            board (list): The current game board as a 2D list.
            piece (str): The piece symbol to check for a win.

        Returns:
            bool: True if the piece has won, False otherwise.
        """
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
        Performs a flood fill algorithm starting from the specified cell to find connected pieces.

        Args:
            board (list): The current game board as a 2D list.
            row (int): The starting row index.
            col (int): The starting column index.
            piece (str): The piece symbol to search for.
            checked (set, optional): Set of already checked positions.

        Returns:
            int: The number of connected pieces found.
        """

        # Si es la primera vez creamos una lista con los visitados:
        if checked is None:
            checked = []

        # Comprobamos si la posición está fuera del board:
        if row < 0 or row >= len(board):
            return 0

        if col < 0 or col >= len(board[0]):
            return 0

        # Comprobamos si se ha checkeado la casilla:
        if (row, col) in checked:
            return 0


        # Comprobamos si la casilla es la pieza que buscamos:
        if board[row][col] != piece:
            return 0

        checked.append((row, col))
        count = 1

        # Recursividad en las 4 direcciones:
        count += Utils.flood_fill_algorithm(board, row + 1, col, piece, checked)
        count += Utils.flood_fill_algorithm(board, row - 1, col, piece, checked)
        count += Utils.flood_fill_algorithm(board, row, col + 1, piece, checked)
        count += Utils.flood_fill_algorithm(board, row, col - 1, piece, checked)

        return count