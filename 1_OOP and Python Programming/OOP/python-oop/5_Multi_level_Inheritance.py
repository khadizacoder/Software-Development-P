class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def run(self):
        return f"This {self.name} Price -> {self.price}"


class Buss(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self):
        return f'Buss {self.name}, Price {self.price} and seat {self.seat}'


class Track(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)


class ACBus(Buss):
    def __init__(self, name, price, seat, temp) -> None:
        self.temp = temp
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        return f'AC Buss {self.name}, seat {self.seat} and Temparature {self.temp}'

    
    def display_info(self):
        return f'''
            Buss : {self.name}
            Price : {self.price}
            Seat : {self.seat}
            Temparature: {self.temp}
        '''


my_busses = Buss('Poribohon Bus', '$30000', 42)
print(my_busses.run())
print(my_busses)

green_line = ACBus("Green", '$6000', 22, 18)
print(green_line)
print(green_line.display_info())
