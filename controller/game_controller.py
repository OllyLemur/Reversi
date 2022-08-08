import datetime

from view.game_console_view import GameConsoleView
from model.classic_game import ClassicGameRules
from model.advanced_ai import AdvancedAI

class GameController:
    def __init__(self, view: GameConsoleView , model: ClassicGameRules, first_player, second_player) -> None:
        self.view = view
        self.model = model
        self.first_player = first_player
        self.second_player = second_player

    def play_game(self):
        while True:
            white, black, empty = self.model.moveset.board.count_cells()
            self._draw_desk(white, black)

            possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player, self.model.moveset.board)

            if possible_moves:
                row, col = self._get_move(possible_moves)
            else:
                print('No possible moves')
                self.model.moveset.change_player()
                possible_moves = self.model.moveset.get_possible_move(self.model.is_valid_move, self.model.moveset.curr_player, self.model.moveset.board)
                if possible_moves:
                    row, col = self._get_move(possible_moves)
                else:
                    print('No possible moves')
                    self._determine_the_winner(white, black)
                    break

            self.model.moveset.make_move(row, col, possible_moves[(row, col)], self.model.moveset.board)

            white, black, empty = self.model.moveset.board.count_cells()
            if white == 0 or black == 0 or empty == 0:
                self.view.draw_board()
                self.view.display_score(white, black)
                self._determine_the_winner(white, black)
                break
            
            self.model.moveset.change_player()

    def _draw_desk(self, white, black):
        """Function draw board, display score and player

        Args:
            white (int)
            black (int)
        """
        self.view.draw_board()
        self.view.display_score(white, black)
        self.view.display_player(self.model.moveset.curr_player)

    def _determine_the_winner(self, white, black):
        """function checks the winner and displays score on the screen

        Args:
            white (int):
            black (int):
        """
        winner = self.model.check_winner(white, black)
        if winner == True:
            self.view.display_winner('O')
            self._write_result_in_file('O', white, black)
        elif winner == False:
            self.view.display_winner('X')
            self._write_result_in_file('X', white, black)
        elif winner == -1:
            print('Draw!')
            self._write_result_in_file('Draw!', white, black)

    def _get_move(self, possible_moves):
        """Determines the move depending on the type of player

        Args:
            possible_moves (dict): {(possible move)):[(direction, end cell)]}

        Returns:
            row (int), col (int): row, col of target cell
        """
        curr_player = self.model.moveset.curr_player
        if curr_player == self.first_player.value and isinstance(self.first_player, AdvancedAI):
            row, col = self.first_player.get_move(self.model.moveset.board, possible_moves)
        elif curr_player == self.second_player.value and isinstance(self.second_player, AdvancedAI):
            row, col = self.second_player.get_move(self.model.moveset.board, possible_moves)
        else:
            if curr_player == self.first_player.value:
                row, col = self.first_player.get_move(possible_moves)
            elif curr_player == self.second_player.value:
                row, col = self.second_player.get_move(possible_moves)

        return row, col

    def _write_result_in_file(self, winner, white, black):
        now = datetime.datetime.now()
        date = str(now.day) + str(now.month) + str(now.year)
        score = f'O score: {white}, X score: {black}'
        if winner == 'O' or winner == 'X':
            str_winner = f'{winner} is win!'
        else:
            str_winner = f'{winner}'
        
        with open('resalts.txt', 'w') as f:
            f.write(date + '\n')
            f.write(score + '\n')
            f.write(str_winner + '\n')