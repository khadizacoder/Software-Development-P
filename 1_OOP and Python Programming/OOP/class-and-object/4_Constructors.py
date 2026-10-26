class Phone:
    menufacture = 'China'

    def __init__(self, owner, brand, price):
        # pass
        self.owner = owner
        self.brand = brand
        self.price = price


    def send_msg(self, phone, msg):
        print(f'{phone} this number msg -> {msg}')


my_phone = Phone('Kala', 'Oppo', 50000)
print(my_phone.owner, my_phone.brand, my_phone.price)


her_phone = Phone('monir','Sawmi', 20000)
print(her_phone.owner, her_phone.brand, her_phone.price)