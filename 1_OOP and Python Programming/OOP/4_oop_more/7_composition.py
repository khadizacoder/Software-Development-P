# ? interview Q : inheritance vs composition
# in a relation | has a relation


class Engine:
    def __init__(self):
        pass

    def start(self):
        return "Engine started"



class Driver:
    def __init__(self):
        pass


# car "has an" engine
class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()



# ! Make computer

class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity


# computer has a cpu
# computer has a ram
# computer has a hard drive

class Computer:
    def __init__(self, cores, ram_size, hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_drive = HardDrive(hd_capacity)


my_computer = Computer(5, 12, 512)