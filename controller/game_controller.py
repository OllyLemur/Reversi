from view.game_console_view import GameConsoleView
from model.classic_game import ClassicGameRules
from model.simple_ai import SimpleAI

class GameController:
    def __init__(self, view: GameConsoleView , model: ClassicGameRules) -> None:
        self.view = view
        self.model = model
    
    def play_game_vs_player(self):
        while True:
            white, black, empty = self.model.moveset.board.count_cells()
            self._draw_desk(white, black)

            possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player)

            if possible_moves:
                row, col = self.view.get_move()
            else:
                print('No possible moves')
                self.model.moveset.change_player()
                possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player)
                if possible_moves:
                    row, col = self.view.get_move()
                else:
                    print('No possible moves')
                    self._determine_the_winner(white, black)
                    break

            col, row = self._check_validity_of_move(col, row, possible_moves)

            self.model.moveset.make_move(row, col, possible_moves[(col, row)])

            white, black, empty = self.model.moveset.board.count_cells()
            if white == 0 or black == 0 or empty == 0:
                self._determine_the_winner(white, black)
                break
            
            self.model.moveset.change_player()

    def play_game_vs_simple_ai(self):

        simple_ai = SimpleAI()
        
        while True:
            white, black, empty = self.model.moveset.board.count_cells()
            self._draw_desk(white, black)

            possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player)
            
            if possible_moves:
                if self.model.moveset.curr_player == 2:
                    col, row = simple_ai.choose_move(possible_moves)
                else:
                    row, col = self.view.get_move()
            else:
                print('No possible moves')
                self.model.moveset.change_player()
                possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player)
                if possible_moves:
                    if self.model.moveset.curr_player == 2:
                        col, row = simple_ai.choose_move(possible_moves)
                    else:
                        row, col = self.view.get_move()
                else:
                    print('No possible moves')
                    self._determine_the_winner(white, black)
                    break
            
            col, row = self._check_validity_of_move(col, row, possible_moves)

            self.model.moveset.make_move(row, col, possible_moves[(col, row)])

            white, black, empty = self.model.moveset.board.count_cells()
            if white == 0 or black == 0 or empty == 0:
                self._determine_the_winner(white, black)
                break
            
            self.model.moveset.change_player()

    def _draw_desk(self, white, black):
        self.view.draw_board()
        self.view.display_score(white, black)
        self.view.display_player(self.model.moveset.curr_player)

    def _determine_the_winner(self, white, black):
        winner = self.model.check_winner(white, black)
        if winner:
            self.view.display_winner('X')
        else:
            self.view.display_winner('O')

    def _check_validity_of_move(self, col, row, possible_moves):
        if (col, row) not in possible_moves:
            while True:
                print('Incorrect move! Try again')
                row, col = self.view.get_move()
                if (col, row) in possible_moves:
                    break
        
        return col, row
        