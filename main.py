from model.classic_game import ClassicGameRules
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

model = ClassicGameRules(4)
view = GameConsoleView(model)
controller = GameController(view, model)

controller.play_game_vs_simple_ai()