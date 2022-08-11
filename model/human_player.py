from model.players import Players
import re

class HumanPlayer(Players):
    def __init__(self, value) -> None:
        super().__init__(value)

    def get_move(self, possible_moves):
        """Function get move from user

        Args:
            possible_moves (dict): {(possible move)):[(direction, end cell)]}

        Returns:
            row (int), col (int)
        """
        s = input('Enter your move (row, col): ')
        
        row, col = self._move_validation(s)

        if (row, col) not in possible_moves:
            while True:
                print('Incorrect move! Try again')
                s = input('Enter your move (row, col): ')
                row, col = self._move_validation(s)
                if (col, row) in possible_moves:
                    break

        return row, col

    def _move_validation(self, str):
        """The function checks the correctness of the move entered by the user

        Args:
            str (string): user input

        Returns:
            row (int), col (int)
        """
        regex = '\d+, ?\d+'
        if bool(re.search(regex, str)):
            str = str.split(',')
            row, col = int(str[0]), int(str[1])
        else:
            while True:
                str = input('Incorrect input! Type row, col: ')
                if bool(re.search(regex, str)):
                    str = str.split(',')
                    row, col = int(str[0]), int(str[1])
                    break
        
        return row, col
