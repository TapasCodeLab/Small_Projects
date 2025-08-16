class InvalidNumberOfPlayers(Exception):
    def __init__(self):
        super().__init__("There should be at least one winning strategy")