from utils import Utils
from board import Board
from time import sleep
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
        Utils.show_cpu_turn(board)
        valid_col = self._board.get_valid_columns()

        return random.choice(valid_col)


    def normal(self, board, player_piece, cpu_piece):
        """

        """
        Utils.show_cpu_turn(board)
        valid_col = board.get_valid_columns()

        # Optimizo a un loop for 2D
        # Busca ganar o bloquear:
        for piece in [cpu_piece, player_piece]:
            for col in valid_col:
                row = board.get_available_row(col)

                if row != -1:
                    # Copia board para simular:
                    cpu_board_copy = board.get_board_copy()
                    temp_board = Board(board._row, board._col)
                    temp_board._board = cpu_board_copy


                    # Simula poner la ficha
                    temp_board._board[row][col] = piece

                    if Utils.check_winner(temp_board, piece):
                        return col

        # Si no puede ganar ni bloquear, jugada aleatoria
        return self.easy(board)


    def hard(self, player_piece, cpu_piece):
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
        block_cols = []

        for col in valid_col:
            row = self._board.get_available_row(col)

            if row != -1:
                # Simula jugada de la CPU
                cpu_board_copy = self._board.get_board_copy()
                cpu_board_copy[row][col] = cpu_piece
                checked = []  # guardamos las posiciones vistas

                cpu_connected = Utils.flood_fill_algorithm(cpu_board_copy, row, col, cpu_piece, checked)

                # Si la CPU encuentra que puede conectar 4, gana:
                if cpu_connected >= 4:
                    return col

                # prioriza la jugada de 3 si no hay mejor opción
                elif cpu_connected == 3 and max_connected_pieces < 3:
                    max_connected_pieces = 3
                    best_col = col

                # Guarda la columna con la mayor cantidad de fichas conectadas o iguales, para mejor movimiento:
                elif cpu_connected > max_connected_pieces:
                    max_connected_pieces = cpu_connected
                    best_col = col

                # Player puede ganar? Simula
                # Copia board para simulación:
                player_board_copy = self._board.get_board_copy()
                player_row = self._board.get_available_row(col)

                if player_row != -1:
                    player_board_copy[player_row][col] = player_piece

                    temp_player_board = Board(self._board._row, self._board._col)
                    temp_player_board._board = player_board_copy

                    if Utils.check_winner(temp_player_board, player_piece):
                        block_cols.append(col)  # Guardamos las posibles columnas a bloquear

        # Si encuentra 2, que bloquee una al azar
        if block_cols:
            return random.choice(block_cols)

        # Si no hay jugada ganadora, escoge la mejor conexion:
        if best_col is not None:
            return best_col

        # sinó jugada aleatoria:
        return self.easy(self._board)


# DEBBUG:
if __name__ == "__main__":
    from constants import EMPTY_CELL, PLAYER_PIECE, CPU_PIECE
    Utils.clear_terminal()

    # board hipotetico
    # simulo un board para debug:
    board = Board(6, 7)
    board._board = [
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, PLAYER_PIECE],
        [EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, CPU_PIECE],
        [EMPTY_CELL, EMPTY_CELL, CPU_PIECE, EMPTY_CELL, EMPTY_CELL, EMPTY_CELL, CPU_PIECE],
        [EMPTY_CELL, EMPTY_CELL, PLAYER_PIECE, PLAYER_PIECE, PLAYER_PIECE, EMPTY_CELL, CPU_PIECE]
    ]

    logic = Logic(board)
    player_piece = PLAYER_PIECE
    cpu_piece = CPU_PIECE


    # Llama al método hard y muestra el resultado
    col = logic.hard(player_piece, cpu_piece)
    print(f"Columna a bloquear o ganar: {col + 1}")