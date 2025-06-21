# from utils import Utils
# from board import Board

# class Menu:
#     def __init__(
#             self,
#             first_player = None,
#             second_player = None,
#             difficulty = None,
#             selected_option = None
#             ):

#         self._first_player_name = first_player
#         self._second_player_name = second_player
#         self._difficulty = difficulty
#         self._selected_option = selected_option
#         self._utils = Utils() # Creamos instanca a la clase Utils


#     def select_players(self):
#         """
#         Display the main menu and allow the user to select the game mode.
#         """
#         self._utils.clear_terminal()
#         opts = [
#             "One player vs CPU",
#             "Two players (coming soon)"
#         ]

#         for idx, opt in enumerate(opts):
#             print(f"{idx + 1}. {opt}")

#         select = input("\nPlease, select an option: ").strip()

#         while True:
#             if select == "1":
#                 self._utils.clear_terminal()
#                 print("Player 1: ")
#                 self._first_player_name = self._utils.choose_name()

#                 self._utils.clear_terminal()
#                 self._difficulty = self._utils.choose_difficulty(self._first_player_name)

#                 return self._first_player_name, self._difficulty


#             elif select == "2":
#                 self._utils.clear_terminal()
#                 print("Player 1: ")
#                 self._first_player_name = self._utils.choose_name()
#                 self._utils.clear_terminal()
#                 print(f"Player 1: {self._first_player_name}")

#                 print("Player 2: ")
#                 self._second_player_name = self._utils.choose_name()
#                 self._utils.clear_terminal()
#                 print(f"Player 1: {self._first_player_name}")
#                 print(f"Player 2: {self._second_player_name}")

#                 input("Press Enter to continue...")
#                 break

#             else:
#                 print("Opción inválida...")
#                 input("Presiona Enter para continuar...")
#                 break


# if __name__ == "__main__":
#     menu = Menu(first_player=None, second_player=None)
#     menu.select_players()