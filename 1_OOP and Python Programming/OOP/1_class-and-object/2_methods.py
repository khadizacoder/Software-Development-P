def call():
    print("Calling some on")
    return 'call done'

class Phone:
    price = 10000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'airphone', 'hammer']

    def call(self):
        print('Calling one persone')

    def send_sms(self, phone, sms):
        print(f'{phone} this number sms -> {sms}')

my_phone = Phone()
print(my_phone.features)
print(my_phone.brand)

my_phone.call()
my_phone.send_sms(233434, 'i miss you')
