from model.board import Board
from model.rules import GameRules

class ClassicGameRules(GameRules):
    def __init__(self, board_size):
        super().__init__(board_size)
        

    def is_valid_move(self, col, row, curr_player, board):
        target_cell = (col - 1, row - 1)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        result = []

        if board.get_sell(target_cell[1], target_cell[0]) != 0:
             return result

        for direction in directions:
            curr_cell = target_cell
            curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
            if curr_cell[0] >= board.size or curr_cell[1] >= board.size or curr_cell[0] < 0 or curr_cell[1] < 0:
                pass
            else:
                if board.get_sell(curr_cell[1], curr_cell[0]) == 3 - curr_player:
                    while True:
                        curr_cell = (curr_cell[0] + direction[0], curr_cell[1] + direction[1])
                        if curr_cell[0] >= board.size or curr_cell[0] < 0 or curr_cell[1] < 0 or curr_cell[1] >= board.size:
                            break
                        if board.get_sell(curr_cell[1], curr_cell[0]) == curr_player:
                            result.append((direction, curr_cell))
                            break
                        elif board.get_sell(curr_cell[1], curr_cell[0]) == 3 - curr_player:
                            continue
                        else:
                            break
        
        return result
                        

    def check_winner(self, white, black):
        if black == 0:
            return True
        if white == 0:
            return False
        return white > black #True — white are winers, False - black win
