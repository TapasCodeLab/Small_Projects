from enum import Enum

class WinningStrategyType(Enum):
    ROW = 'Row',
    COL = 'Column'
    DIA = 'Diagonal'