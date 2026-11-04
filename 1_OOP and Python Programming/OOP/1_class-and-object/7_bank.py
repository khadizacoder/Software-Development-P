class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def main_balance(self):
        return self.balance

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'Fokira. You can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw or amount > self.balance:
            print(f'Bank fokir hoay jabe. You can not withdraw more than {self.max_withdraw} and {self.balance}')
        else:
            self.balance -= amount
            print(f'Withdraw money {amount}, now current ballance {self.balance}')

brac = Bank(2000)
brac.withdraw(50)
brac.deposite(2500)
brac.withdraw(1000)

brac.withdraw(100000)


dbbl = Bank(500000)
dbbl.withdraw(1000)
