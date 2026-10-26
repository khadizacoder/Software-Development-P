class Shop:
    shopping_mall = 'Jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an a instant attribute

    def add_to_cart(self, item):
        self.cart.append(item)


mafuz = Shop('mafuz')
mafuz.add_to_cart('hedphone')
mafuz.add_to_cart('laptop')
mafuz.add_to_cart('dextoop')

print(mafuz.cart)


mina = Shop('mina')
mina.add_to_cart('lipestic')
mina.add_to_cart('mekup')
mina.add_to_cart('foods')

print(mina.cart)