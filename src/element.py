class Element:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, o) -> bool:
        return self.x == o.x and self.y == o.y
