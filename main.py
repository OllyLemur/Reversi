from pyexpat import model
from model.classic_game import ClassicGameRules
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

model = ClassicGameRules(8)
view = GameConsoleView(model)
controller = GameController(view, model)

controller.play_game()