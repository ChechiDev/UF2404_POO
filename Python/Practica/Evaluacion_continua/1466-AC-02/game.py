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
    player_piece = "X   "
    cpu_piece = "O   "

    player = HumanPlayer("Player 1", player_piece)
    cpu = CPUPlayer("CPU", cpu_piece, difficulty="normal")

    while True:
        # Turno del player
        user_col = player.play(board)
        board.insert_piece(user_col, player._piece)
        board.print_board()

        if Utils.check_winner(board, player_piece):
            print(f"{player._name} wins!")
            break

        # check de dificultad y turno cpu
        if cpu.difficulty == "easy":
            cpu_col = cpu.play_easy(board, cpu_piece)

        elif cpu.difficulty == "normal":
            cpu_col = cpu.play_normal(board, player_piece, cpu_piece)

        elif cpu.difficulty == "hard":
            cpu_col = cpu.play_hard(board, player_piece, cpu_piece)

        else:
            cpu_col = cpu.play_easy(board, cpu_piece)

        board.insert_piece(cpu_col, cpu_piece)
        board.print_board()

        if Utils.check_winner(board, cpu_piece):
            print(f"{cpu._name} wins!")
            break


if __name__ == "__main__":
    game()