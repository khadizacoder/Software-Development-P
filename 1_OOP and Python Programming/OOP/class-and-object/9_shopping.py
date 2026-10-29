class Shopping():
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, "price": price, 'quantity' : quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        
        print(f'Total Price {total}')

        if amount < total:
            print(f'Please provide {total - amount } Taka more ')
        else:
            extra = amount - total
            print(f'Here is your items and extra money {extra}')


anishul = Shopping('Anisul islam')
anishul.add_to_cart('Alu', 100, 5)
anishul.add_to_cart('Dim', 12, 30)
anishul.add_to_cart('BEGUN', 20, 5)

print(anishul.cart)
anishul.checkout(1500)