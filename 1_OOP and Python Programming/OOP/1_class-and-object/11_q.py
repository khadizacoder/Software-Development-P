# def call():
#     print('calling someone')
#     return 'call done'

# class Phone:
#     price = 103334
#     color = 'blue'

#     def call(self):
#         print('call me')

# my_p = Phone()
# call()


# class A:
#     def __init__(self, value):
#         value = 3
#         self.value = value

#     def change(self):
#         self.value = 12

# ans = []
# a = A(13)
# ans.append(a.value)
# a.change()
# ans.append(a.value)
# print(ans)

# class Shop:
#     cart = []
#     def __init__(self, buyer):
#         self.buyer = buyer

#     def add_to_cart(self, item):
#         self.cart.append(item)

# p1 = Shop("meh jabeen")
# p1.add_to_cart("shoes")
# p1.add_to_cart("phone")


# nisho = Shop("nisho")
# nisho.add_to_cart('cap')
# nisho.add_to_cart('watch')

# print(nisho.cart)


class Shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

p1 = Shop("meh jabeen")
p1.add_to_cart("shoes")
p1.add_to_cart("phone")


nisho = Shop("nisho")
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')

print(nisho.cart)