from turtle import back
from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from model.classic_game import ClassicGameRules

class GameConsoleView(GameView):
    def __init__(self, game: ClassicGameRules) -> None:
        super().__init__(game)
        self.board_view = BoardConsoleView(game.moveset.board)

    def get_move(self):
        s = input('Enter your move (row, col): ').split(',')
        row, col = int(s[0]), int(s[1])
        return row, col

    def draw_board(self):
        self.board_view.draw_board()

    def display_winner(self, player):
        print(player)

    def display_score(self, white, black):
        print(f'X score: {black}, O score: {white}')

    def display_player(self, player):
        print(f'Player {player}: It\'s your turn')