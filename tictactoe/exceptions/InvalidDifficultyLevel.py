class InvalidDifficultyLevel(Exception):
    def __init__(self):
        super().__init__("Invalid difficulty level provided")
