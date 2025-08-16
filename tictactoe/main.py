# Client code
from tictactoe.controllers.GameController import GameController
from tictactoe.models.BotDifficultyLevel import BotDifficultyLevel
from tictactoe.models.GameStatus import GameStatus
from tictactoe.models.PlayerType import PlayerType
from tictactoe.services.GameService import GameService

if __name__ == '__main__':
    game_service = GameService()
    game_controller = GameController(game_service)

    player1 = game_controller.create_player('Prisha',PlayerType.HUMAN,'X')
    player2 = game_controller.create_player('Tapas', PlayerType.HUMAN, '#')
    player3 = game_controller.create_player('Bot',PlayerType.BOT,'O',BotDifficultyLevel.EASY)
    players = [player1, player2,player3]
    size = 4
    winning_strategies = game_controller.create_ws(size, players)
    game = game_controller.create_game(size, players, winning_strategies)
    game_controller.print_board(game)


    while game.get_game_state() == GameStatus.IN_PROGRESS:
        game_controller.make_move(game)
        game_controller.print_board(game)
        while game_controller.check_undo(game):
            game_controller.undo_move(game)
            game_controller.print_board(game)


    #game.get_board().print_board()
    if game.get_game_state()==GameStatus.COMPLETED:
        print(f"{game.winner.get_name()} won the game.")
    else:
        print("The game was drawn.")


