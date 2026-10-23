# tuple not changible

def multiple():
    return 3,4

print(multiple())

# things = ('pen', 'bottle', 'pad', 'phone')
things = 'pen', 'bottle', 'pad', 'phone'
things2 = 'pen',
print(things)
print(things2)
print(things[1])
print(things[-1])
print(things[::-1])

# things[0] = 'wagon'


if 'phone' in things:
    print("Already exists")

for x in things:
    print(x)

mega1 = [(1,2,3), (4,5,6)]
mega2 = ([1,2,3], [4,5,6])

print(type(mega1))
print(type(mega2))

mega2[0][1] = 999
print(mega2)