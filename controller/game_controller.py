from view.game_console_view import GameConsoleView
from model.classic_game import ClassicGameRules
from model.simple_ai import SimpleAI
from model.players import Players
from model.human_player import HumanPlayer

class GameController:
    def __init__(self, view: GameConsoleView , model: ClassicGameRules, first_player: Players, second_player: Players) -> None:
        self.view = view
        self.model = model
        self.first_player = first_player
        self.second_player = second_player

    def play_game(self):
        while True:
            white, black, empty = self.model.moveset.board.count_cells()
            self._draw_desk(white, black)

            possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player)

            if possible_moves:
                row, col = self._get_move(possible_moves)
            else:
                print('No possible moves')
                self.model.moveset.change_player()
                possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player)
                if possible_moves:
                    row, col = self._get_move(possible_moves)
                else:
                    print('No possible moves')
                    self._determine_the_winner(white, black)
                    break

            if isinstance(self.first_player, HumanPlayer) or isinstance(self.second_player, HumanPlayer):
                col, row = self._check_validity_of_move(col, row, possible_moves)

            self.model.moveset.make_move(row, col, possible_moves[(row, col)])

            white, black, empty = self.model.moveset.board.count_cells()
            if white == 0 or black == 0 or empty == 0:
                self._draw_desk(white, black)
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
            self.view.display_winner('O')
        else:
            self.view.display_winner('X')

    def _check_validity_of_move(self, col, row, possible_moves):
        if (col, row) not in possible_moves:
            while True:
                print('Incorrect move! Try again')
                row, col = self._get_move()
                if (col, row) in possible_moves:
                    break
        
        return col, row

    def _get_move(self, possible_moves):
        curr_player = self.model.moveset.curr_player
        if curr_player == self.first_player.value and isinstance(self.first_player, SimpleAI):
            row, col = self.first_player.get_move(possible_moves)
        elif curr_player == self.second_player.value and isinstance(self.second_player, SimpleAI):
            row, col = self.second_player.get_move(possible_moves)
        elif curr_player == self.first_player.value and isinstance(self.first_player, HumanPlayer):
            row, col = self.first_player.get_move()
        elif curr_player == self.second_player.value and isinstance(self.second_player, HumanPlayer):
            row, col = self.second_player.get_move()

        return row, col    