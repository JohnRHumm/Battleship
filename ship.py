class Ship():
    def __init__(self) -> None:
        self.hits_to_sink = 0
        self.is_floating = True
        self.location = []


class Destroyer(Ship):
    def __init__(self) -> None:
        super().__init__()
        self.hits_to_sink = 2


class Submarine(Ship):
    def __init__(self) -> None:
        super().__init__()
        self.hits_to_sink = 3

class Battleship(Ship):
    def __init__(self) -> None:
        super().__init__()
        self.hits_to_sink = 4

class AirCraftCarrier(Ship):
    def __init__(self) -> None:
        super().__init__()
        self.hits_to_sink - 5