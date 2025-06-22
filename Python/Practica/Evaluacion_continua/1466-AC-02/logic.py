from utils import Utils
from board import Board
from time import sleep
# from main import Menu
import random


class Logic:
    def __init__(self, board):
        self._board = board


    def easy(self, board):
        valid_col = self._board.get_valid_columns()
        sleep(2)
        return random.choice(valid_col)


    def normal(slef):
        pass


    def hard(slef):
        pass