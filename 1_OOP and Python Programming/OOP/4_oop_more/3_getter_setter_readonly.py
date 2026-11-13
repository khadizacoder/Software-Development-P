class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money #* Private property set korar jonno getter and setter use kora

    # getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age

    # @getattr
    @property
    def salary(self):
        return self.__money

    @salary.setter
    def salary (self, value):
        if value < 0:
            return "salary can not ne nagative"
        
        self.__money+=value
    

samsu = User("Kopa", 21, 1200)
# print(samsu.__money)
# print(samsu.age())

samsu.salary = 4500
print(samsu.salary)