from soupsieve import select
from model.board import Board
from model.players import Players

class Moveset:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.curr_player = 1

    def change_player(self):
        self.curr_player = 3 - self.curr_player
    
    def make_move(self, row, col, res):
        target_cell = (col - 1, row - 1)
        self.board.update_sell(target_cell[1], target_cell[0], self.curr_player)
        for i in range(len(res)):
            current_cell = target_cell
            while current_cell != res[i][1]:
                current_cell = (current_cell[0] + res[i][0][0], current_cell[1] + res[i][0][1])
                self.board.update_sell(current_cell[1], current_cell[0], self.curr_player)

    def get_possible_move(self, is_valid_move, curr_player):
        possible_moves = {}

        for row in range(1, self.board.size + 1):
            for col in range(1, self.board.size + 1):
                res = is_valid_move(col, row, curr_player)
                if res != []:
                    possible_moves[(row, col)] = res
        
        return possible_moves
