from model.board import Board
from model.players_symbols import PlayersSymbols

class Moveset:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.curr_player = PlayersSymbols.X

    def change_player(self):
        self.curr_player = 3 - self.curr_player
    
    def make_move(self, row, col, res):
        target_cell = (col, row)
        for i in range(len(res)):
            current_cell = target_cell
            while current_cell != target_cell:
                current_cell = (current_cell[0] + res[i][0][0], current_cell[1] + res[i][0][1])
                self.board.update_sell(current_cell[1], current_cell[0], self.curr_player)

