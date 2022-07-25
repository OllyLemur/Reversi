from abc import ABC, abstractclassmethod
from model.moveset import Moveset

class GameRules(ABC):
    def __init__(self, board_size):
        self.moveset = Moveset(board_size)
        
    @abstractclassmethod
    def is_valid_move(self):
        pass

    @abstractclassmethod
    def check_winner(self):
        pass