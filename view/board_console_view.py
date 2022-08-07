from view.board_view import BoardView
from model.board import Board

class BoardConsoleView(BoardView):
    """This class is inherited class from BoardView for building the view of board in the console.
    """
    
    SYMBOLS = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, board: Board) -> None:
        super().__init__(board)

    def draw_board(self):
        """Function prints board in the console
        """

        board_size = self.board.size
        header = '  |'
        line = '--+'
        for i in range(board_size):
            header += f' {i + 1} |'
            line += '---+'
        print(header)
        print(line)
        for j in range(board_size):
            print(f' {j + 1}|', end='')
            for i in range(board_size):
                cell = self.board.get_sell(j, i)
                print(f' {self.SYMBOLS[cell]} |', end='')
            print('\n'+line)
