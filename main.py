from model.classic_game import ClassicGameRules
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController
from model.simple_ai import SimpleAI
from model.advanced_ai import AdvancedAI

player_one = AdvancedAI(1, ClassicGameRules(8), 4)
player_two = SimpleAI(2)

model = ClassicGameRules(8)
view = GameConsoleView(model)
controller = GameController(view, model, player_one, player_two)


controller.play_game()