import copy

from model.players import Players
from model.board import Board

class AdvancedAI(Players):
    def __init__(self, value, model, depth) -> None:
        super().__init__(value)
        self.model = copy.deepcopy(model)
        self.depth = depth
    
    def get_move(self, board, possible_moves):
        copy_possible_moves = copy.deepcopy(possible_moves)
        most_moves = 0
        point = (0, 0)

        while len(copy_possible_moves):
            possible_move = copy_possible_moves.popitem()
            new_board = copy.deepcopy(board)
            target_cell = possible_move[0]

            self.model.moveset.make_move(target_cell[0], target_cell[1], possible_move[1], new_board)
            board_value = self.minmax(new_board, self, AdvancedAI(3 - self.value, self.model, self.depth), self.depth)

            if board_value > most_moves:
                most_moves = board_value
                point = target_cell

        return point

    def minmax(self, board, max_player, min_player, depth):
        if depth == 0:
            return self.get_board_value(board, max_player)

        values = []
        possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, max_player.value, board)

        while len(possible_moves):
            possible_move = possible_moves.popitem()

            new_board = copy.deepcopy(board)
            target_cell = possible_move[0]
            possible_moves_of_point = possible_move[1]

            self.model.moveset.make_move(target_cell[0], target_cell[1], possible_moves_of_point, new_board)
            board_value = self.minmax(new_board, min_player, max_player, depth - 1)

            values.append(board_value)
        
        if not values:
            return self.get_board_value(board, max_player)

        if self == max_player:
            return max(values)
        else:
            return min(values)
    
    def get_board_value(self, board: Board, player: Players):
        board_value = 1
        white, black, empty = board.count_cells()
        if player.value == 1:
            board_value += black
        else:
            board_value += white

        possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, player.value, board)
        while len(possible_moves):
            item = possible_moves.popitem()
            target_cell = item[0]
            moves = item[1]

            if target_cell[0] - 1 == 0:
                board_value += 1
            if target_cell[1] - 1 == 0:
                board_value += 1
            if target_cell[0] == board.size:
                board_value += 1
            if target_cell[1] == board.size:
                board_value += 1
            
            if moves[0] == (1, 1):
                board += 1
            if moves[0] == (1, -1):
                board += 1
            if moves[0] == (-1, 1):
                board += 1
            if moves[0] == (-1, -1):
                board += 1
        
        return board_value

        