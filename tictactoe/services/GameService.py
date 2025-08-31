from tictactoe.exceptions.InvalidPlayerType import InvalidPlayerType
from tictactoe.factories.BotFactory import BotFactory
from tictactoe.models.Game import GameBuilder, Game
from tictactoe.models.GameStatus import GameStatus
from tictactoe.models.Player import Player
from tictactoe.models.PlayerType import PlayerType
from tictactoe.strategies.winningStrategies.ColWinningStrategy import ColWinningStrategy
from tictactoe.strategies.winningStrategies.DiagonalWinningStrategy import DiagonalWinningStrategy
from tictactoe.strategies.winningStrategies.RowWinningStrategy import RowWinningStrategy
from tictactoe.models.WinningStrategyType import WinningStrategyType

class GameService(object):
    def __init__(self):
        pass

    def create_player(self,name,player_type,symbol,difficulty_level=None):
        if player_type==PlayerType.HUMAN:
            return Player(name,PlayerType.HUMAN,symbol)
        elif player_type==PlayerType.BOT:
            return BotFactory().create_bot(name,symbol,difficulty_level)
        else:
            raise InvalidPlayerType

    def create_ws(self, size, players,strategies):
        winning_strategies = []
        for strategy in strategies:
            if strategy == WinningStrategyType.ROW:
                winning_strategies.append(RowWinningStrategy(size, players))
            elif strategy == WinningStrategyType.COL:
                winning_strategies.append(ColWinningStrategy(size, players))
            elif strategy == WinningStrategyType.DIA:
                winning_strategies.append(DiagonalWinningStrategy(size, players))

        return winning_strategies

    def create_game(self, size, players, winning_strategies):
        game = (GameBuilder()
                .set_dimension(size)
                .set_players(players)
                .set_winning_strategies(winning_strategies)
                .validate()
                .build())
        return game

    def print_board(self,game:Game):
        game.get_board().print_board()

    def make_move(self,game:Game):
        player = game.get_next_player()
        print(f"It is {player.get_name()}'s turn:")
        row, col = player.make_move(game.get_board())
        game.get_board().get_cell(row,col).set_player(player)
        game.add_move(row,col,player)
        game.check_winner(row, col, player)
        if game.get_game_state() == GameStatus.IN_PROGRESS and game.get_moves_length() == game.get_dimension()*game.get_dimension():
            game.set_game_state(GameStatus.DRAWN)

    def check_undo(self, game):
        choice = 'N'
        if game.get_game_state()== GameStatus.IN_PROGRESS and game.get_moves_length()>0:
            choice = input("Do you want to undo? Please enter 'Y' for yes, anything else for no: " )
        return choice=='Y'

    def undo_move(self, game):
        game.undo_move()
