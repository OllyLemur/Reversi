from model.classic_game import ClassicGameRules
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController
from model.simple_ai import SimpleAI
from model.advanced_ai import AdvancedAI
from model.human_player import HumanPlayer

class ConsoleUI:
    def create_ui(self):
        board_size = input('Enter board size (4, 6, 8, 10, 12): ')

        model = ClassicGameRules(board_size)
        view = GameConsoleView(model)

        game_mode = input('Select game mode: \n a. Player VS Player b. Player VS Computer \n input (a, b): ')

        if game_mode == 'a':
            player_one = HumanPlayer(1)
            player_two = HumanPlayer(2)
            controller = GameController(view, model, player_one, player_two)
            controller.play_game()
        elif game_mode == 'b':
            game_difficulty = input('Select game difficulty: easy(e), medium(m), hard(h): ')
            player_one = HumanPlayer(1)

            if game_difficulty == 'e':
                player_two = SimpleAI(2)
                controller = GameController(view, model, player_one, player_two)
                controller.play_game()
            elif game_difficulty == 'm':
                player_two = AdvancedAI(2, ClassicGameRules(board_size), 2)
                controller = GameController(view, model, player_one, player_two)
                controller.play_game()
            elif game_difficulty == 'h':
                player_two = AdvancedAI(2, ClassicGameRules(board_size), 4)
                controller = GameController(view, model, player_one, player_two)
                controller.play_game()

            
