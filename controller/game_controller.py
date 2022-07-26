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
            row, col = self.view.get_move()
            
            res = self.model.is_valid_move(col , row, self.model.moveset.curr_player)

            i = empty
            while not res:
                print('Incorrect move! Try again')
                i -= 1
                row, col = self.view.get_move()
                res = self.model.is_valid_move(col - 1, row - 1, self.model.moveset.curr_player)

            self.model.moveset.make_move(row, col, res)
            white, black, empty = self.model.moveset.board.count_cells()
            if white == 0:
                self.view.display_winner('X')
                break
            elif black == 0:
                self.view.display_winner('O')
                break
            elif empty == 0:
                winner = self.model.check_winner(white, black)
                if winner:
                    self.view.display_winner('O')
                    break
                else:
                    self.view.display_winner('X')
                    break
            
            self.model.moveset.change_player()
