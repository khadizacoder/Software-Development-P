numbers = [30,40,50,60]

print(numbers)
numbers.append(70)
print(numbers)

numbers.insert(1,80)
print(numbers)

numbers.remove(40)
print(numbers)

# numbers.remove(20)
if 50 in numbers:
    numbers.remove(50)
    print(numbers)
else : print("Not avl")

last = numbers.pop()
print(last)
print(numbers)

if 8 in numbers:
    idx = numbers.index(8)
    print(idx)

numbers.sort()
# print(sorted)
print(numbers)
