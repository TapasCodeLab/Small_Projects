from tictactoe.strategies.winningStrategies.WinningStrategy import WinningStrategy


class RowWinningStrategy(WinningStrategy):
    def __init__(self, dimension, players):
        self.dimension = dimension
        self.rows = {}
        for row in range(dimension):
            self.rows[row] = {}
            for player in players:
                self.rows[row][player] = 0

    def check_winner(self, row, col, player):
        self.rows[row][player] = self.rows[row][player] + 1
        return self.rows[row][player] == self.dimension, f"row {row}."

    def remove_check_winner(self, row, col, player):
        self.rows[row][player] = self.rows[row][player] - 1

    def check_win_possibility(self, row, col, player):
        return self.rows[row][player] == self.dimension-1

