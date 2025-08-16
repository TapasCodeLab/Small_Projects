from tictactoe.exceptions.InvalidCellSelection import InvalidCellSelection
from tictactoe.models.CellStatus import CellStatus


class Cell(object):
    def __init__(self,row,col,status:CellStatus):
        self.row = row
        self.col = col
        self.status = status
        self.player = None

    def get_cell_status(self):
        return self.status

    def set_player(self,player):
        if player and self.status == CellStatus.EMPTY:
            self.player = player
            self.status = CellStatus.FILLED
        elif player is None:  #For undo
            self.player = None
            self.status = CellStatus.EMPTY
        else:
            raise InvalidCellSelection

    def print_cell(self):
        if self.status == CellStatus.EMPTY:
            return '_'
        else:
            return self.player.symbol.character