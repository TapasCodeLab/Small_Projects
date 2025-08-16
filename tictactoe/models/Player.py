from tictactoe.models.Board import Board
from tictactoe.models.PlayerType import PlayerType
from tictactoe.models.Symbol import Symbol

class Player(object):
    def __init__(self, name, player_type: PlayerType, symbol):
        self.name = name
        self.player_type = player_type
        self.symbol = Symbol(symbol)

    def get_name(self):
        return self.name

    def make_move(self, board:Board):
        while True:
            row = int(input('Please enter row: '))
            col = int(input('Please enter column: '))
            if board.is_valid_move(row, col):
                return row, col
            else:
                print("Invalid selection -")