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
        print("\nCPU (O) Turn\nChoosing a valid column...")
        sleep(1)
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


        for col in valid_col:
            row = self._board.get_available_row(col)

            if row is not None:
                # Player puede cpu? Simula
                # Copia board para simulación:
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
                    best_col


                # Guarda la columna con la mayor cantidad de fichas conectadas o iguales, para mejor movimiento:
                elif cpu_connected > max_connected_pieces:
                    max_connected_pieces = cpu_connected
                    best_col = col

                # Player puede ganar? Simula
                # Copia board para simulación:
                player_board_copy = self._board.get_board_copy()
                player_board_copy[row][col] = player_piece
                checked = [] # guardamos las posiciones vistas

                player_connected = Utils.flood_fill_algorithm(player_board_copy, row, col, player_piece, checked)

                if player_connected >= 4:
                    # Bloquea victoria del player
                    return col

                elif player_connected == 3 and max_connected_pieces < 3:
                    # bloqueo de 3 al player
                    max_connected_pieces = 3
                    best_col = col


        # Si no hay jugada ganadora, escoge la mejor conexion:
        if best_col is not None:
            return best_col


        # sinó jugada aleatoria:
        return self.easy(self._board)