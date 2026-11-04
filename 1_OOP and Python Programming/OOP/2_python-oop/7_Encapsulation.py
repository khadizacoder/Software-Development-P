class Bank:
    def __init__(self, holder_name, balance) -> None:
        self.holder_name = holder_name  # Public
        # self.balance = balance        # Public
        self.__balance = balance        # Private
        self._brance = 'Bonani Branch'  # Protected


    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


    def withdraw (self, amount):
        if amount <= self.balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Fokir nai tui'


    def __repr__(self):
        return f'Holder name is {self.holder_name} and Bank balance {self.__balance}'

habiba = Bank("choto Choti", 30000)
print(habiba.holder_name)
print(habiba)

# Public name access
# print(habiba.balance)
# habiba.balance = 0
# print(habiba.balance)

# Private name access
habiba.deposit(50000)
print(habiba.get_balance())


# Protected name access
print(habiba._brance)



# Jor kore access korbo je vabe
# print(dir(habiba))
print(habiba._Bank__balance)