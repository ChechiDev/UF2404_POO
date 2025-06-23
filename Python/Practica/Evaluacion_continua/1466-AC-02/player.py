from logic import Logic
from utils import Utils


class Player:
    def __init__(self, name, piece):
        self._name = name
        self._piece = piece


class HumanPlayer(Player):
    def __init__(self, name, piece):
        super().__init__(name, piece)


    def play(self, board):
        """
        Asks the player to select a valid column for their move.

        Args:
            board (Board): The current game board.

        Returns:
            int: The selected valid column index.
        """
        while True:
            col = Utils.valid_column_num(board, self._name, self._piece)

            if board.is_valid_column(col):
                return col

            else:
                print("That column is full")


class CPUPlayer(Player):
    def __init__(self, name, piece, difficulty):
        super().__init__(name, piece)
        self.difficulty = difficulty


    def play_easy(self, board, piece):
        """
        CPU's move in easy mode by selecting a random valid column.

        Args:
            board (Board): The current game board.
            piece (str): The symbol representing the CPU's piece.

        Returns:
            int: The selected column index for the move.
        """
        logic = Logic(board)
        col = logic.easy(board)

        return col


    def play_normal(self, board, player_piece, cpu_piece):
        """

        """
        logic = Logic(board)
        col = logic.normal(board, player_piece, cpu_piece)

        return col


    def play_hard(self, board, player_piece, cpu_piece):
        """
        CPU's move by evaluating possible moves and selecting the best option.

        Args:
            board (Board): The current game board.
            player_piece (str): The symbol representing the human player's piece.
            cpu_piece (str): The symbol representing the CPU's piece.

        Returns:
            int: The selected column index for the move.
        """
        logic = Logic(board)
        col = logic.hard(player_piece, cpu_piece)

        return col


    # COMING SOON
    def play_insane(self, board, piece):
        pass