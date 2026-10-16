def full_name(first, last):
    name = f'{first} {last}'
    return name

# name = full_name('Alu', 'Kodu')
# name = full_name(last='Kodu', first='Alu')
# print(name)

def famus_name(first, last, **additional):
    name = f'{first} {last} {additional}'
    return name

name = famus_name(first="khadiza", last="khatun", depertment="Economics" , year="first year")
print(name)


def a_lot(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    return sum, mult, remain

everithing = a_lot(5,5)
