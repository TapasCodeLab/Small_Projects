from abc import ABC, abstractmethod

class WinningStrategy(ABC):

    @abstractmethod
    def check_winner(self, row, col, player):
        pass

    @abstractmethod
    def remove_check_winner(self, row, col, player):
        pass