from abc import ABC, abstractmethod
from tictactoe.models.Board import Board


class BotPlayingStrategy(ABC):

    @abstractmethod
    def make_move(self,board:Board):
        pass