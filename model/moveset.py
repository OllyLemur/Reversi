from model.board import Board
from model.players import Players
from model.human_player import HumanPlayer
from model.simple_ai import SimpleAI
from model.advanced_ai import AdvancedAI

class Moveset:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.curr_player = 1

    def change_player(self):
        self.curr_player = 3 - self.curr_player
    
    def make_move(self, row, col, res, board):
        """_summary_

        Args:
            row (_type_): _description_
            col (_type_): _description_
            res (_type_): _description_
            board (_type_): _description_
        """
        target_cell = (col - 1, row - 1)
        board.update_sell(target_cell[1], target_cell[0], self.curr_player)
        for i in range(len(res)):
            current_cell = target_cell
            while current_cell != res[i][1]:
                current_cell = (current_cell[0] + res[i][0][0], current_cell[1] + res[i][0][1])
                board.update_sell(current_cell[1], current_cell[0], self.curr_player)

    def get_possible_move(self, is_valid_move, curr_player, board):
        """_summary_

        Args:
            is_valid_move (bool): _description_
            curr_player (_type_): _description_
            board (_type_): _description_

        Returns:
            _type_: _description_
        """
        possible_moves = {}

        for row in range(1, board.size + 1):
            for col in range(1, board.size + 1):
                res = is_valid_move(col, row, curr_player, board)
                if res != []:
                    possible_moves[(row, col)] = res
        
        return possible_moves
