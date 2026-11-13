class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money #* Private property set korar jonno getter and setter use kora


samsu = User("Kopa", 21, 1200)
print(samsu.__money)