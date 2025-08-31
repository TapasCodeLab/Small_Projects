from tictactoe.strategies.winningStrategies.WinningStrategy import WinningStrategy


class DiagonalWinningStrategy(WinningStrategy):
    def __init__(self, dimension, players):
        self.dimension = dimension
        self.left_diagonal = {}
        self.right_diagonal = {}
        for player in players:
            self.left_diagonal[player] = 0
            self.right_diagonal[player] = 0

    def check_winner(self, row, col, player):
        if row==col:
            self.left_diagonal[player] = self.left_diagonal[player] + 1
        if row+col == self.dimension-1:
            self.right_diagonal[player] = self.right_diagonal[player] + 1
        #return (self.left_diagonal[player] == self.dimension) or (self.right_diagonal[player] == self.dimension)

        if self.left_diagonal[player] == self.dimension:
            return True, "left diagonal."
        elif self.right_diagonal[player] == self.dimension:
            return True, "right diagonal."
        else:
            return False, ""

    def remove_check_winner(self, row, col, player):
        if row==col:
            self.left_diagonal[player] = self.left_diagonal[player] - 1
        if row+col == self.dimension-1:
            self.right_diagonal[player] = self.right_diagonal[player] - 1

    def check_win_possibility(self, row, col, player):
        if row == col and row+col == self.dimension-1:
            return (self.left_diagonal[player] == self.dimension-1) or (self.right_diagonal[player] == self.dimension-1)
        elif row==col:
            return self.left_diagonal[player] == self.dimension -1
        elif row+col == self.dimension-1:
            return self.right_diagonal[player] == self.dimension-1
        else:
            return False