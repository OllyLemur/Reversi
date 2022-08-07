from abc import ABC, abstractclassmethod
from model.board import Board

class BoardView(ABC):
    """ Abstract class for the visual presentation of the game board
    """
    
    def __init__(self, board: Board) -> None:
        self.board = board

    @abstractclassmethod
    def draw_board(self):
        pass