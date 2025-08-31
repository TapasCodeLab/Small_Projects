import random

from tictactoe.exceptions import InvalidNoOfWS
from tictactoe.exceptions.InvalidDimension import InvalidDimension
from tictactoe.exceptions.InvalidNoOfBots import InvalidNoOfBots
from tictactoe.exceptions.InvalidNumberOfPlayers import InvalidNumberOfPlayers
from tictactoe.models.Board import Board
from tictactoe.models.GameStatus import GameStatus
from tictactoe.models.PlayerType import PlayerType


class GameBuilder(object):
    def __init__(self):
        self.players = None
        self.dimension = None
        self.winning_strategies = None

    def set_players(self, players):
        self.players = players
        return self

    def set_dimension(self, dimension):
        self.dimension = dimension
        return self

    def set_winning_strategies(self, winning_strategies):
        self.winning_strategies = winning_strategies
        return self

    def validate(self):
        if self.dimension<3:
            raise InvalidDimension
        elif len(self.players) > self.dimension - 1 or len(self.players) < 2:
            raise InvalidNumberOfPlayers(2,self.dimension - 1)
        elif sum([1 if player.player_type==PlayerType.BOT else 0 for player in self.players])>1:
            raise InvalidNoOfBots
        elif len(self.winning_strategies) == 0:
            raise InvalidNoOfWS
        else:
            return self

    def build(self):
        return Game(self)



class Game(object):
    def __init__(self, builder: GameBuilder):
        self.players = builder.players
        self.dimension = builder.dimension
        self.winning_strategies = builder.winning_strategies
        self.game_state = GameStatus.IN_PROGRESS
        self.board = Board(self.dimension)
        self.winner = None
        self.next_player = random.randrange(len(self.players))  #any random integer from 0 to number of players-1
        self.moves = []

    def get_game_state(self):
        return self.game_state

    def set_game_state(self, state):
        self.game_state = state

    def get_dimension(self):
        return self.dimension

    def get_next_player(self):
        player = self.players[self.next_player]
        self.next_player = (self.next_player+1)%len(self.players)
        return player

    def get_board(self):
        return self.board

    def add_move(self,row,col,player):
        self.moves.append([row,col,player])

    def undo_move(self):
        row, col, player = self.moves.pop()
        self.get_board().get_cell(row, col).set_player(None)
        self.next_player = (self.next_player +len(self.players) - 1) % len(self.players)
        self.remove_check_winner(row, col, player)


    def get_moves_length(self):
        return len(self.moves)

    def check_winner(self, row, col, player):
        for ws in self.winning_strategies:
            if ws.check_winner(row, col, player):
                self.game_state = GameStatus.COMPLETED
                self.winner = player

    def remove_check_winner(self, row, col, player):
        for ws in self.winning_strategies:
            ws.remove_check_winner(row, col, player)











