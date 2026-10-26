class Shop:
    cart = [] # cart is an a class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


habiba = Shop('Habiba')
habiba.add_to_cart('shoes')
habiba.add_to_cart('phone')

print(habiba.cart)


mita = Shop('Mita')
mita.add_to_cart('hand book')
mita.add_to_cart('hardwork')
mita.add_to_cart('economic')

print(mita.cart)