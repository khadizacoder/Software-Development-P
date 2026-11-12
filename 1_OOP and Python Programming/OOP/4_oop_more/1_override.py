class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("vat, mangsho, polaw, korma")

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self,name,age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

    # Override
    def eat(self):
        print("vagetables, seeds")

    def exercise(self):
        print("gym e onk tk deay gham jhoray")

    # using python magic/dunder methods
    def __add__(self, other):
        return self.age + other.age

    def __mul__(self, other):
        return self.weight * other.weight

    # def __len__(self): # returns an integer
    #     return self.height

    def __len__(self): # returns an integer
        return int(self.height)

    def __gt__(self, other):
        return self.age > other.age


shakib = Cricketer("Shakib", 33, 5.7, 67, 'BD')
mushi = Cricketer("Mushi", 43, 5.9, 87, "BD")
# shakib.eat()
# shakib.exercise()

print(30+50)
print("Khadiza"+"Habiba")
print([1,3,4,5,6] + [5,8,4,5,9])

print(shakib + mushi)
print(shakib * mushi)
print(len(shakib))
print(shakib > mushi)