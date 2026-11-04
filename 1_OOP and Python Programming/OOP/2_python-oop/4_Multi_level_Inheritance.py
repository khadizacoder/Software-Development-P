# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class

class Device:
    def __init__(self, name, brand, price, color) -> None:
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f"running {self.name}: {self.brand}"


class Laptop(Device):
    def __init__(self, name, brand, price, color, memory) -> None:
        self.memory = memory
        super().__init__(name, brand, price, color)

    def coding(self):
        return f"Learning python and practice"


class Phone(Device):
    def __init__(self, name, brand, price, color, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(name, brand, price, color)

    def phone_call(self, number, text):
        return f"sending SMS to : {number} with: {text}"

    def __repr__(self):
        return f"Phone {self.dual_sim}"


class Camera(Device):
    def __init__(self, name, brand, price, color, pixel) -> None:
        self.pixel = pixel
        super().__init__(name, brand, price, color)

my_phone = Phone("Phone", 'iPhone', 1300000, 'yellow', True)
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone)
print(my_phone.run())


my_laptop = Laptop('Laptop', 'del', 80000, 'pink', '16gb')
print(my_laptop.brand)
print(my_laptop.color)
print(my_laptop.run())