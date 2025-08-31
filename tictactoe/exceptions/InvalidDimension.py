class InvalidDimension(Exception):
    def __init__(self):
        super().__init__("Invalid dimension - it should be at least 3")
