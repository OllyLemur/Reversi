from model.players import Players

class HumanPlayer(Players):
    def __init__(self, value) -> None:
        super().__init__(value)

    def get_move():
        s = input('Enter your move (row, col): ').split(',')
        row, col = int(s[0]), int(s[1])
        return row, col