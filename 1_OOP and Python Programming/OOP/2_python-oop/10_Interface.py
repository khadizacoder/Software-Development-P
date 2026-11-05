from typing import Protocol

class AnimalProtocol(Protocol):
    def __init__(self):
        pass

class Dog:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        print(f'{self.name} Geaw Geaw kore kno')


class Cat:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        print(f'{self.name} koi gelo')


dog = Dog("Monuu")
cat = Cat("Menu")

arr = [dog, cat]
for animal in arr:
    animal.sound()

    