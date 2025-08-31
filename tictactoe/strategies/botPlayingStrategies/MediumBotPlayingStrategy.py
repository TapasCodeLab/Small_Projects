from tictactoe.models.CellStatus import CellStatus
from tictactoe.models.Game import Game
from tictactoe.models.Player import Player
from tictactoe.strategies.botPlayingStrategies.BotPlayingStrategy import BotPlayingStrategy

class MediumBotPlayingStrategy(BotPlayingStrategy):

    def make_move(self, game: Game):
        board = game.get_board()
        winning_strategies = game.get_winning_strategies()
        player_index = game.get_player_index()
        players = game.get_players()
        current_player = players[player_index]
        # Can I win
        for row in range(board.get_dimension()):
            for col in range(board.get_dimension()):
                if board.get_cell(row,col).get_cell_status() == CellStatus.EMPTY:
                    for ws in winning_strategies:
                        if ws.check_win_possibility(row, col, current_player):
                            return row, col
        # Can I block opponents winning
        for row in range(board.get_dimension()):
            for col in range(board.get_dimension()):
                if board.get_cell(row,col).get_cell_status() == CellStatus.EMPTY:
                    for player in players:
                        if player != current_player:
                            for ws in winning_strategies:
                                if ws.check_win_possibility(row, col, player):
                                    return row, col
        # Easy playing strategy
        for row in range(board.get_dimension()):
            for col in range(board.get_dimension()):
                if board.get_cell(row,col).get_cell_status() == CellStatus.EMPTY:
                    return row,col
        return -1, -1