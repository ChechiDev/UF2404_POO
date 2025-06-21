import os
from logic import Logic


class Player:
    def __init__(self, name, piece):
        self._name = name
        self._piece = piece



class HumanPlayer(Player):
    def __init__(self, name, piece):
        super().__init__(name, piece)


    def play(self, board):
        pass



class CPUPlayer(Player):
    def __init__(self, name, piece, difficulty):
        super().__init__(name, piece)
        self.difficulty = difficulty


        def play_easy(self, board, piece):
            pass


        def play_normal(self, board, piece):
            pass


        def play_hard(self, board, piece):
            pass


        # COMING SOON
        def play_insane(self, board, piece):
            pass