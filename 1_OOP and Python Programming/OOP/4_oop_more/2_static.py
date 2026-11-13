#* Static attribute (class attribute)
#* static method @staticmethod
#* class method @classmethod
#* differences between ststic method and class method

class Shopping:
    cart = [] #* Class attribute or static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = "jamuna"
        self.location = "Jam er majkhane"
        pass

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"Buying: {item} for Price: {price} and remaining: {remaining}")

    @staticmethod
    def multiplay(a,b):
        mul = a*b
        print(mul)

    @classmethod
    def hudai_dekhi(self, item):
        print("huday dekhi but keni na", item)


basundara = Shopping("basundhara", "popular")
basundara.purchase("Phone", 12000, 15000)
# Shopping.purchase( "Khadiza","phone", 12000, 20000)

basundara.hudai_dekhi("lungi")
Shopping.hudai_dekhi("Panjabi")

Shopping.multiplay(4,6) #* Static method
basundara.multiplay(5,5)

# ? Google search --> Python ststic method vs class method