# set : unique items collection

# List  --> []
# Tuple --> ()
# Set   --> {}

numbers = [2,3,4,5,6,7,8]
print(numbers)

numbers_set = set(numbers)
print(numbers_set)

# numbers_set[1] = 88

numbers_set.add(44)
numbers_set.add(44)
print(numbers_set)

numbers_set.remove(4)
print(numbers_set)

for item in numbers_set:
    print(item)

if 6 in numbers_set:
    print("6 exists")
elif 44 in numbers_set:
    print('44 Exists')


A = {1,2,5,7}
B = {3,4,5,6,7}
print(A & B)
print(A | B)

