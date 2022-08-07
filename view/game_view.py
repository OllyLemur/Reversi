from abc import ABC, abstractclassmethod
from model.moveset import Moveset

class GameView(ABC):
    """ Abstract class for the visual presentation of the game
    """
    
    def __init__(self, game: Moveset) -> None:
        self.game = game

    @abstractclassmethod
    def draw_board(self):
        pass

    @abstractclassmethod
    def display_winner(self, player):
        pass

    @abstractclassmethod
    def display_score(self, white, black):
        pass

    @abstractclassmethod
    def display_player(self, player):
        pass