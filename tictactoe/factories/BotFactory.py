from tictactoe.exceptions.InvalidDifficultyLevel import InvalidDifficultyLevel
from tictactoe.models.Bot import Bot
from tictactoe.models.BotDifficultyLevel import BotDifficultyLevel
from tictactoe.strategies.botPlayingStrategies.EasyBotPlayingStrategy import EasyBotPlayingStrategy
from tictactoe.strategies.botPlayingStrategies.HardBotPlayingStrategy import HardBotPlayingStrategy
from tictactoe.strategies.botPlayingStrategies.MediumBotPlayingStrategy import MediumBotPlayingStrategy


class BotFactory():
    def __init__(self):
        pass

    @staticmethod
    def create_bot(name, symbol, bot_difficulty_level: BotDifficultyLevel):
        bot_playing_strategy = None
        if bot_difficulty_level==BotDifficultyLevel.EASY:
            bot_playing_strategy = EasyBotPlayingStrategy()
        elif bot_difficulty_level == BotDifficultyLevel.MEDIUM:
            bot_playing_strategy = MediumBotPlayingStrategy()
        elif bot_difficulty_level == BotDifficultyLevel.HARD:
            bot_playing_strategy = HardBotPlayingStrategy()
        else:
            raise InvalidDifficultyLevel

        return Bot(name, symbol, bot_difficulty_level, bot_playing_strategy)