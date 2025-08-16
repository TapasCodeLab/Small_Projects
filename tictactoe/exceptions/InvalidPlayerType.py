class InvalidPlayerType(Exception):
    def __init__(self):
        super().__init__("Invalid player type provided")
