import random as rand
from utils import Utils


class Board:
    """
    Class that represents the Connect Four game board.\n
    Attr:
        _row (int): Number of rows of the board.
        _col (int): Number of columns of the board.
        _board (list): Matrix that represents the board.
    """
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._board = []
        self._empty_cell = ".   "
        self.create_board()

    def create_board(self) -> list:
        """
        Creates a board game grid\n
        Arg1 x: int: ROWS \n
        Arg2 y: int: COLUMNS\n
        Return: List: 2D array with the board generated
        """
        # Generamos el board de juego.
        for i in range(self._row):
            row = []
            for j in range(self._col):
                row.append(self._empty_cell)

            self._board.append(row)

        # print(type(board))
        return self._board


    def print_board(self, board: list):
        """
        Muestra el tablero por pantalla\n
        Arg: 2D List\n
        Return: List: 2D array rendered in CMD.
        """
        # Board header:
        print("   ".join(str(n) for n in range(self._col)))
        # Board
        for row in self._board:
            print("".join(row))


    def is_valid_column(self, col: int) -> bool:

        if col < 0 or col >= self._col:
            return False
        
        if self._board[0][col] == self._empty_cell:
            return True
        
        else:
            return False


    def insert_piece(self, col: int, piece: str) -> bool:
        
        Utils.clear_terminal()
        for row in reversed(range(self._row)):
            if self._board[row][col] == self._empty_cell:
                self._board[row][col] = piece
                return True

        return False  # La columna está llena


if __name__ == "__main__":

    Utils.clear_terminal()
    ROWS = 6
    COLUMNS = 7

    board = Board(ROWS, COLUMNS)
    board.print_board()

    # Preguntamos al user por la columna que quiere
    user_move = Utils.valid_column_num()
    piece = "X "

    # Comprobamos si la columna es válida y colocamos la ficha
    while True:
        if board.is_valid_column(user_move):
            board.insert_piece(user_move, "X  ")
            board.print_board()
            break