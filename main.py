from model.classic_game import ClassicGameRules
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController
from model.simple_ai import SimpleAI

player_one = SimpleAI(1)
player_two = SimpleAI(2)

model = ClassicGameRules(4)
view = GameConsoleView(model)
controller = GameController(view, model, player_one, player_two)

controller.play_game()