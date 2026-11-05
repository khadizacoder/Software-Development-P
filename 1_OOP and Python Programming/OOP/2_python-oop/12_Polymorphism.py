from math import pi

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print("animal making some sound")


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Meaw Meaw")


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Ghew Ghew")


class Goat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Baaa Baoww Baa")

cat = Cat("menu")
dog = Dog("Bok Bok")
shepard = Dog("Local shepard")
goat = Goat("chagol")

arr = [cat, dog, shepard, goat]
for animal in arr:
    animal.make_sound()


print("..................")

class Shape:
    def __init__(self, name):
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width


class Cercle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius * self.radius


ractangle = Rectangle("ractangle", 4, 3)
print(ractangle.area())

cercle = Cercle("cercle", 2)
print(cercle.area())
