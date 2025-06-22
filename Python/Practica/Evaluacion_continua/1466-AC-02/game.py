import os
from utils import Utils
from board import Board
from player import HumanPlayer, CPUPlayer
# from menu import Menu

ROWS = 6
COLUMNS = 7

def game():
    # Utils.clear_terminal()
    board = Board(ROWS, COLUMNS)
    board.print_board()

    player = HumanPlayer("Player 1", "X   ")
    cpu = CPUPlayer("CPU", "O   ", difficulty="easy")

    while True:
        # Turno del jugador humano
        user_col = player.play(board)
        board.insert_piece(user_col, player._piece)
        board.print_board()

        if Utils.check_winner(board, player._piece):
            print(f"{player._name} wins!")
            break

        # Turno de la CPU (easy)
        cpu_col = cpu.play_easy(board, cpu._piece)
        board.insert_piece(cpu_col, cpu._piece)
        board.print_board()

        if Utils.check_winner(board, cpu._piece):
            print(f"{cpu._name} wins!")
            break


if __name__ == "__main__":
    game()