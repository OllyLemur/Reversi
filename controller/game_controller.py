from view.game_console_view import GameConsoleView
from model.classic_game import ClassicGameRules

class GameController:
    def __init__(self, view: GameConsoleView , model: ClassicGameRules) -> None:
        self.view = view
        self.model = model
    
    def play_game(self):
        while True:
            self.view.draw_board()
            white, black, empty = self.model.moveset.board.count_cells()
            self.view.display_score(white, black)

            self.view.display_player(self.model.moveset.curr_player)
            if self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player):
                row, col = self.view.get_move()
            else:
                print('No possible moves')
                self.model.moveset.change_player()
                if self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player):
                    row, col = self.view.get_move()
                else:
                    print('No possible moves')
                    winner = self.model.check_winner(white, black)
                    if winner:
                        self.view.display_winner('O')
                        break
                    else:
                        self.view.display_winner('X')
                        break

            res = self.model.is_valid_move(col , row, self.model.moveset.curr_player)

            while not res:
                print('Incorrect move! Try again')
                row, col = self.view.get_move()
                res = self.model.is_valid_move(col, row, self.model.moveset.curr_player)

            self.model.moveset.make_move(row, col, res)
            white, black, empty = self.model.moveset.board.count_cells()
            if white == 0 or black == 0 or empty == 0:
                winner = self.model.check_winner(white, black)
                if winner:
                    self.view.display_winner('O')
                    break
                else:
                    self.view.display_winner('X')
                    break
            
            self.model.moveset.change_player()
