class Calculator:
    brand = 'casio ma994'
    def add(self, num1, num2):
        print(num1 + num2)
    def minus(self, num1, num2):
        print(num1 - num2)

cal = Calculator()
cal.add(2,3)
cal.minus(2,3)