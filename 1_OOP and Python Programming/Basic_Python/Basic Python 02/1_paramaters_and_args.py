
def double_it(num):
    result = num * 2
    print(result)

double_it(4)
double_it(10)

# def sum(num1, num2):
#     result = num1 + num2
#     return result

# print("Total value" ,sum(4, 9))


def sum(num1, num2 = 0, num3 = 0):
    total= num1 + num2 + num3
    return total

# print("Toatal value" ,sum(4,6))
# print("Toatal value" ,sum(4,6, 6))

def args(num1, *num2):
    print(num1, num2)
    sum = 0
    for n in num2:
        print(n)
        sum = sum + n
    return sum


total = args(34,6,2,7,9)
print(total)


def do_a_lot(*args):
    print(args)