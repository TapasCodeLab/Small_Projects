class InvalidNumberOfPlayers(Exception):
    def __init__(self,_min,_max):
        super().__init__(f"Invalid number of players, there can be a minimum {_min} and maximum {_max} players.")
