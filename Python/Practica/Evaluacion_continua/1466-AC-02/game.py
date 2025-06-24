from utils import Utils
from board import Board
from menu import Menu
from player import HumanPlayer, CPUPlayer
from constants import ROWS, COLUMNS, CPU_PIECE, PLAYER_PIECE

def game():

    # Landing menu:
    menu = Menu()
    first_player_name, difficulty = menu.select_players()

    board = Board(ROWS, COLUMNS)
    board.print_board()
    player_piece = PLAYER_PIECE
    cpu_piece = CPU_PIECE


    player = HumanPlayer(first_player_name, player_piece)
    cpu = CPUPlayer("CPU", cpu_piece, difficulty=difficulty)

    while True:
        # Turno del player
        Utils.clear_terminal()
        board.print_board()
        user_col = player.play(board)
        board.insert_piece(user_col, player._piece)

        Utils.clear_terminal()
        board.print_board()

        # Check para victoria:
        if Utils.check_winner(board, player_piece):
            print(f"\n{player._name} wins!")
            break

        # Check para empate:
        if Utils.check_is_full(board._board):
            print("Draw! The board is full.")
            break

        # Turno de la CPU:
        # check de dificultad
        if cpu.difficulty == "easy":
            cpu_col = cpu.play_easy(board, cpu_piece)

        elif cpu.difficulty == "normal":
            cpu_col = cpu.play_normal(board, player_piece, cpu_piece)

        elif cpu.difficulty == "hard":
            cpu_col = cpu.play_hard(board, player_piece, cpu_piece)

        else:
            cpu_col = cpu.play_easy(board, cpu_piece)

        board.insert_piece(cpu_col, cpu_piece)

        Utils.show_cpu_turn(board)
        board.print_board()

        # Check para victoria:
        if Utils.check_winner(board, cpu_piece):
            print(f"{cpu._name} wins!")
            break

        # Check para empate:
        if Utils.check_is_full(board._board):
            print("Draw! The board is full.")
            break


if __name__ == "__main__":
    game()