from sympy import O
from model.players_symbols import PlayersSymbols

class Board:
    EMPTY_CELL = 0

    def __init__(self, size):
        self.size = size 

        self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]
        self.mat[len(self.mat) // 2][len(self.mat) // 2] = PlayersSymbols.O
        self.mat[len(self.mat) // 2 + 1][len(self.mat) // 2] = PlayersSymbols.X
        self.mat[len(self.mat) // 2][len(self.mat) // 2 + 1] = PlayersSymbols.X
        self.mat[len(self.mat) // 2 + 1][len(self.mat) // 2 + 1] = PlayersSymbols.O

    def get_sell(self, row, col):
        return self.mat[row][col]

    def update_sell(self, row, col, player):
        self.mat[row][col] = player

    def count_cells(self):
        white = 0
        black = 0

        for j in range(len(self.mat)):
            for i in range (len(self.mat)):
                if self.mat[j][i] == PlayersSymbols.O:
                    white += 1
                if self.mat[j][i] == PlayersSymbols.X:
                    black += 1
        
        return (white, black)