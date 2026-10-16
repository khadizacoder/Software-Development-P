balance = 3000

def buy_now(item, price):
    # Local scop
    # balance = 500

    # global scop
    global balance
    balance = balance - price
    print(f'previews {balance}')

print(buy_now("bottle", 1000))

