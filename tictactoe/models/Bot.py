from tictactoe.models.Board import Board
from tictactoe.models.BotDifficultyLevel import BotDifficultyLevel
from tictactoe.models.Player import Player
from tictactoe.models.PlayerType import PlayerType
from tictactoe.strategies.botPlayingStrategies.BotPlayingStrategy import BotPlayingStrategy


class Bot(Player):
    # Use Factory
    def __init__(self,name, symbol, bot_difficulty_level: BotDifficultyLevel, bot_playing_strategy: BotPlayingStrategy):
        super().__init__(name, PlayerType.BOT, symbol)
        self.bot_difficulty_level = bot_difficulty_level
        self.bot_playing_strategy = bot_playing_strategy

    def make_move(self, board:Board):
        return self.bot_playing_strategy.make_move(board)