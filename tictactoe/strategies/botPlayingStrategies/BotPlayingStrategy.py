from abc import ABC, abstractmethod
from tictactoe.models.Game import Game


class BotPlayingStrategy(ABC):

    @abstractmethod
    def make_move(self,game:Game):
        pass