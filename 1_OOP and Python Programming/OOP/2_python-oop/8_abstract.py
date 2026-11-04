from abc import ABC, abstractmethod

class Anumal(ABC):
    @abstractmethod
    def eat(self):
        print("I need Food")
    
    @abstractmethod
    def move(self):
        pass

class Monkey(Anumal):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()

    # def eat(self):
    #     print("Hey nana, Eating banana")

    def eat(self):
        super().eat()
        print("Hey nana, Eating banana")

    def move(self):
        print("tara tare move koro")


layka = Monkey("lucky")
print(layka.name)
layka.eat()
layka.move()