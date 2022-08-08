from model.board import Board

class Moveset:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.curr_player = 1

    def change_player(self):
        """Function changes the current player.
        """
        self.curr_player = 3 - self.curr_player
    
    def make_move(self, row, col, res, board):
        """_summary_

        Args:
            row (int): target cell coordinates
            col (int): target cell coordinates
            res (list): [(direction, end cell)]
            board (Board): current board
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
            is_valid_move (function): function that determines the validity of a move
            curr_player (int): value of current player
            board (Board): current board

        Returns:
            dict: {(possible move)):[(direction, end cell)]}
        """
        possible_moves = {}

        for row in range(1, board.size + 1):
            for col in range(1, board.size + 1):
                res = is_valid_move(col, row, curr_player, board)
                if res != []:
                    possible_moves[(row, col)] = res
        
        return possible_moves
