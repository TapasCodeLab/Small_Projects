from tictactoe.models.CellStatus import CellStatus
from tictactoe.models.Game import Game
from tictactoe.strategies.botPlayingStrategies.BotPlayingStrategy import BotPlayingStrategy

class HardBotPlayingStrategy(BotPlayingStrategy):

    def make_move(self, game: Game):
        board = game.get_board()
        for row in range(board.get_dimension()):
            for col in range(board.get_dimension()):
                if board.get_cell(row,col).get_cell_status() == CellStatus.EMPTY:
                    return row,col
        return -1, -1