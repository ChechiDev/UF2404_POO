import os
import re
import platform as plat
from time import sleep
from constants import EMPTY_CELL, COLUMNS, PLAYER_PIECE, CPU_PIECE



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


    @staticmethod
    def valid_menu_opt():
        pass


    # @staticmethod
    def choose_difficulty(self, name):
        """
        Asks the user to select a difficulty level for the game.

        Args:
            name (str): The name of the player.

        Returns:
            str: The selected difficulty level ('easy', 'normal', or 'hard').
        """
        from menu import Menu

        opts = ["Easy", "Normal", "Hard"]

        while True:
            Utils.clear_terminal()

            menu = Menu()
            menu.header()

            for idx, opt in enumerate(opts):
                print(f"{idx + 1}. {opt}")

            print("\n0. Exit")

            menu.footer()
            select = input(f"{name}, Please select a difficulty game mode: ").strip()

            if select == "1":
                return opts[0]

            elif select == "2":
                return opts[1]

            elif select == "3":
                return opts[2]

            elif select == "0":
                return "exit"

            else:
                print("Wrong option...")
                sleep(1)


    def valid_column_num(board=None, player_name=None, piece=None) -> int:
        """
        Asks the user to select a valid column number for their move.

        Args:
            player_name (str, optional): The name of the player.
            piece (str, optional): The piece symbol for the player.

        Returns:
            int: The selected valid column number (1-7).
        """
        from menu import Menu

        menu = Menu()

        pattern = r"^\d{1,2}$"

        while True:
            menu.footer()
            value = input(f"{player_name} ({PLAYER_PIECE.strip()}) Turn\nChoose a valid column (1 - {COLUMNS}): ")

            if re.match(pattern, value):
                num = int(value)

                if 1 <= num <= COLUMNS:
                    return num - 1

            menu.footer()
            print("Wrong column...\nPlease select a valid column!")
            sleep(1)

            # Limpiamos terminal e imprimimos board:
            if board is not None:
                Utils.clear_terminal()
                board.print_board()


    @staticmethod
    def show_cpu_turn(board):
        """
        Clears the terminal, prints the CPU turn message, and displays the current board.

        Args:
            board (Board): The current game board to display.
        """
        from menu import Menu

        menu = Menu()

        Utils.clear_terminal()
        board.print_board()

        menu.footer()
        print(f"CPU ({CPU_PIECE.strip()}) Turn\nChoosing a valid column...")
        sleep(1)


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
                    grid[r][c + 3] == piece):
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


    # Check empate:
    def check_is_full(board: list) -> bool:

        for col in range(len(board[0])):
            if board[0][col] == EMPTY_CELL:
                return False

            return True


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