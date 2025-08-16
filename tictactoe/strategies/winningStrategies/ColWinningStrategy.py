from tictactoe.strategies.winningStrategies.WinningStrategy import WinningStrategy


class ColWinningStrategy(WinningStrategy):
    def __init__(self, dimension, players):
        self.dimension = dimension
        self.cols = {}
        for col in range(dimension):
            self.cols[col] = {}
            for player in players:
                self.cols[col][player] = 0

    def check_winner(self, row, col, player):
        self.cols[col][player] = self.cols[col][player] + 1
        return self.cols[col][player] == self.dimension

    def remove_check_winner(self, row, col, player):
        self.cols[col][player] = self.cols[col][player] - 1