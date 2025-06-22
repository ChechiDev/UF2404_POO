from utils import Utils
from board import Board
from time import sleep
# from main import Menu
import random


class Logic:
    def __init__(self, board):
        self._board = board


    def easy(self, board):
        """
        Selects a random valid column for the CPU to play in easy mode.

        Args:
            board (Board): The current game board.

        Returns:
            int: Selected column index
        """
        valid_col = self._board.get_valid_columns()
        sleep(2)
        return random.choice(valid_col)


    def normal(self, player_piece, cpu_piece):
        """
        Selects the best column for the CPU to play by evaluating possible moves and choosing the one that maximizes the number of connected CPU pieces.

        Args:
            player_piece (str):
            cpu_piece (str):

        Returns:
            int: Selected column index
        """
        valid_col = self._board.get_valid_columns()
        best_col = None
        max_connected_pieces = 0


        for col in valid_col:
            row_copy = self._board.get_board_copy()
            row = self._board.get_available_row(col)

            if row is not None:
                # La CPU puede ganar?
                row_copy[row][col] = cpu_piece
                checked = []

                cpu_connected = Utils.flood_fill_algorithm(row_copy, row, col, cpu_piece, checked)
                if cpu_connected >= 4:
                    return col

                if cpu_connected > max_connected_pieces:
                    max_connected_pieces = cpu_connected
                    best_col = col


                # Player puede ganar?
                row_copy[row][col] = player_piece
                checked = []
                player_connected = Utils.flood_fill_algorithm(row_copy, row, col, player_piece, checked)
                if player_connected >= 4:
                    return col


        # sinó jugada aleatoria:
        return self.easy(self._board)


    def hard(slef):
        pass