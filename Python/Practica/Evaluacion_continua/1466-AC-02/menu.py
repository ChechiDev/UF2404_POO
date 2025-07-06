from utils import Utils
from board import Board
from player import HumanPlayer, CPUPlayer
from time import sleep
from constants import ROWS, COLUMNS, CPU_PIECE, PLAYER_PIECE

class Menu:
    def __init__(
            self,
            first_player = None,
            second_player = None,
            difficulty = None,
            selected_option = None,
            header_width = None,
            header_pattern = None
            ):

        self._utils = Utils() # Creamos instanca a la clase Utils
        self._first_player_name = first_player
        self._second_player_name = second_player
        self._difficulty = difficulty
        self._selected_option = selected_option
        self._header_width = 60
        self._header_pattern = "="


    def center(self, text: str, width: int = None) -> str:
        """
        Centers the given text within the specified width.

        Args:
            text (str): The text to center.
            width (int, optional): The width to center the text in.
                If not provided, uses self._header_width.

        Returns:
            str: The centered text.
        """
        if width is None:
            width = self._header_width

        return text.center(width)


    def header(self):
        """
        Prints the game header with a centered title and decorative lines.
        """
        print(self._header_pattern * self._header_width)
        print(self.center("CONNECT - 4: The Ultimate Game!"))
        print(self._header_pattern * self._header_width)


    def footer(self):
        """
        Prints a footer for the menu
        """
        print("\n" * 2)
        print(self._header_pattern * self._header_width)


    def select_players(self):
        """
        Display the main menu and allow the user to select the game mode.
        """
        self._utils.clear_terminal()
        opts = [
            "One player vs CPU",
            "Two players (coming soon)"
        ]

        while True:
            self._utils.clear_terminal()

            self.header()

            for idx, opt in enumerate(opts):
                print(f"{idx + 1}. {opt}")

            self.footer()
            select = input("Please, select a game mode: ").strip()

            if select == "1":
                self._utils.clear_terminal()

                self.header()
                print("Nickname Player 1: ")

                self.footer()
                self._first_player_name = input("Please, enter your nickname: ").strip()

                self._utils.clear_terminal()

                self._difficulty = self._utils.choose_difficulty(self._first_player_name)

                return self._first_player_name, self._difficulty

            # COMMING SOON:
            # elif select == "2":
            #     self._utils.clear_terminal()
            #     print("Player 1: ")
            #     self._first_player_name = self._utils.choose_name()
            #     self._utils.clear_terminal()
            #     print(f"Player 1: {self._first_player_name}")

            #     print("Player 2: ")
            #     self._second_player_name = self._utils.choose_name()
            #     self._utils.clear_terminal()
            #     print(f"Player 1: {self._first_player_name}")
            #     print(f"Player 2: {self._second_player_name}")

            #     input("Press Enter to continue...")
            #     break

            else:
                print("Wrong option...")
                sleep(1)