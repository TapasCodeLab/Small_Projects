from tictactoe.models.Cell import Cell
from tictactoe.models.CellStatus import CellStatus
from tictactoe.models.GameStatus import GameStatus


class Board(object):
    def __init__(self, dimension):
        self.dimension = dimension
        self.grid = [[Cell(row,col,CellStatus.EMPTY) for col in range(dimension)] for row in range(dimension)]

    def get_dimension(self):
        return self.dimension

    def get_cell(self,row,col):
        return self.grid[row][col]

    def print_board(self):
        for row in range(self.dimension):
            print('| ',end='')
            for col in range(self.dimension):
                print(self.get_cell(row,col).print_cell(),'| ',end='')
            print()

    def is_valid_move(self, row, col):
        return 0<=row<self.dimension and 0<=col<self.dimension and self.get_cell(row, col).get_cell_status()==CellStatus.EMPTY
