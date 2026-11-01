# Multiple Inheritance

class Family:
    def __init__(self, address) -> None:
        self.address = address

class School:
    def __init__(self, id, lavel)-> None:
        self.id = id
        self.lavel = lavel

class Sports:
    def __init__(self, game) -> None:
        self.game = game


class Student(Family, School, Sports):
    def __init__(self, address, id, lavel, game) -> None:
        School.__init__(self, id, lavel)
        Sports.__init__(self, game)
        Family.__init__(self, address)
        # super().__init__(address)