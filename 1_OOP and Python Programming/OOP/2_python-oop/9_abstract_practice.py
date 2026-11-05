from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def Sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def Sound(self):
        print(f"{self.name} Gawoo Gawooo kora knooo")

dog = Dog("Monuu")
dog.Sound()


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def Sound(self):
        print(f'{self.name} mmeaw meaw korte korte koi galo')


menu = Cat("Menu")
menu.Sound()