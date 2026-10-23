# lambda

# def doubled(x):
#     return x*2

doubled = lambda num : num*2
squared = lambda num : num ** 2

result = doubled(44)
print(result)

print(squared(20))

add = lambda a, b: a+b
sum = add(5,10)
print(sum)


numbers = [2,4,6,8,1,3,5,7]

print(numbers)

# doubled_num = map(doubled, numbers)
doubled_num = map(lambda x : x*2, numbers)
squared_nums = map(lambda x: x**2, numbers)

print(list(doubled_num))
print(list(squared_nums))


actors = [
    {"name": "sabnan", "age": 21},
    {"name": "sabnur", "age": 24},
    {"name": "khanman", "age": 38},
    {"name": "habiba", "age": 30},
]


juniors = filter(lambda actor : actor['age'] < 30, actors)
fivers = filter(lambda actor : actor['age'] % 5 == 0, actors)

print(list(juniors))
print(list(fivers))