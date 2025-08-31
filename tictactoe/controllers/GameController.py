class GameController(object):
    def __init__(self, game_service):
        self.game_service = game_service

    def create_player(self,name,player_type,symbol,difficulty_level=None):
        return self.game_service.create_player(name,player_type,symbol,difficulty_level)

    def create_ws(self, size, players, strategies):
        return self.game_service.create_ws(size, players, strategies)

    def create_game(self,size, players, winning_strategies):
        return self.game_service.create_game(size, players, winning_strategies)

    def print_board(self, game):
        self.game_service.print_board(game)

    def make_move(self,game):
        self.game_service.make_move(game)

    def check_undo(self, game):
        return self.game_service.check_undo(game)

    def undo_move(self, game):
        self.game_service.undo_move(game)



