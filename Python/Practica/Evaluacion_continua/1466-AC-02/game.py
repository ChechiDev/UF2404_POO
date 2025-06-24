from utils import Utils
from board import Board
from menu import Menu
from player import HumanPlayer, CPUPlayer
from constants import ROWS, COLUMNS, CPU_PIECE, PLAYER_PIECE

def game():

    while True:
    # Landing menu:
        menu = Menu()
        utils = Utils()
        first_player_name, difficulty = menu.select_players()

        if difficulty == "exit":
            continue

        board = Board(ROWS, COLUMNS)
        board.print_board()
        player_piece = PLAYER_PIECE
        cpu_piece = CPU_PIECE


        player = HumanPlayer(first_player_name, player_piece)
        cpu = CPUPlayer("CPU", cpu_piece, difficulty=difficulty)

        while True:
            # Turno del player
            utils.clear_terminal()
            board.print_board()
            user_col = player.play(board)
            board.insert_piece(user_col, player._piece)

            utils.clear_terminal()
            board.print_board()

            # Check para victoria:
            if Utils.check_winner(board, player_piece):
                menu.footer()
                print(f"{player._name} WINS!!!")
                break

            # Check para empate:
            if Utils.check_is_full(board._board):
                menu.footer()
                print("Draw! The board is full.")
                break

            # Turno de la CPU:
            # check de dificultad

            if cpu.difficulty == "exit":
                break

            elif cpu.difficulty == "easy":
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
                utils.clear_terminal()
                menu.header()
                print(f"{cpu._name} WINS!!!")
                menu.footer()
                break

            # Check para empate:
            if Utils.check_is_full(board._board):
                utils.clear_terminal()
                menu.header()
                print("Draw! The board is full.")
                break


if __name__ == "__main__":
    game()