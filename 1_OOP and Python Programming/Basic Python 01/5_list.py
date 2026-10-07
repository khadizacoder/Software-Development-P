fruits = ["apple", "banana", "mango", "cherry"]

# print(fruits[1])
# print(fruits[3])
print(fruits[0::])
print(fruits[0:3])
print(fruits[:2])
print(fruits[1:])

print(fruits[-1])
print(fruits[::-1]) # reverse hoay jabe

fruits[1] = "orange"
print(fruits[0::])


fruits.append("grape")
print(fruits)

fruits.remove("mango")
print(fruits)

fruits.pop(1)
print(fruits)

print(len(fruits))


squares = []
for x in range(1, 10):
    squares.append(x**2)

print(squares)

squ = [x**2 for x in range(1, 10)]
print(squ)


student = ["khadiza", 22, "CSE"]
name, age, department = student
print(name, age, department)

scores = [20, 39, 40, 28, 93, 45]
first, *middle, last = scores
print(first)
print(middle)
print(last)

scores.sort()
print(scores)

scores.sort(reverse=True)
print(scores)


list1 = [1,2,3]
list2 = list1
list2.append(4)
print(list1)

num1 = [1,2,3]
num2 = num1.copy()
num2.append(4)
print(num1)
# print(num2)

