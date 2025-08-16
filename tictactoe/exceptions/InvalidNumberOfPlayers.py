class InvalidNumberOfPlayers(Exception):
    def __init__(self):
        super().__init__("Invalid number of players")

