class InvalidNoOfBots(Exception):
    def __init__(self):
        super().__init__(f"Invalid number of bots. In a game there can be maximum 1 Bot.")
