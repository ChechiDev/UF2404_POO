import os
from utils import Utils
from board import Board
# from menu import Menu

ROWS = 6
COLUMNS = 7

def game():
    Utils.clear_terminal()

    board = Board(ROWS, COLUMNS)
    board.print_board()

    user_move = Utils.valid_column_num()
    piece = "X"

    while True:
        if board.is_valid_column(user_move):
            board.insert_piece(user_move, piece)
            board.print_board()
            break


if __name__ == "__main__":
    game()