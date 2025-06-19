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
        self.create_board()

    def create_board(self) -> list:

        # Generamos los números del header:
        print(" ".join(str(n) for n in range(self._col)))

        # Generamos el board de juego.
        for i in range(self._row):
            row = []
            for j in range(self._col):
                row.append(". ")

            self._board.append(row)

        # print(type(board))
        return self._board

    def print_board(self):

        for row in self._board:
            print("".join(row))


if __name__ == "__main__":

    Utils.clear_terminal()
    ROWS = 6
    COLUMNS = 7

    board = Board(ROWS, COLUMNS)
    board.print_board()