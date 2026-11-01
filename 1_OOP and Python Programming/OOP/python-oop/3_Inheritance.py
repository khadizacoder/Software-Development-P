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


class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory

    def coding(self):
        return f"Learning python and practice"


class Phone:
    def __init__(self, dual_sim) -> None:
        self.dual_sim = dual_sim

    def phone_call(self, number, text):
        return f"sending SMS to : {number} with: {text}"


class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel
