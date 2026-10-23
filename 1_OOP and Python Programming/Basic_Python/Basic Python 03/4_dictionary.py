# key value pair
# dictionary
# object

person = {'name' : 'khadiza', 'age' : 22, 'depertment': 'economics'}
print(person)
print(person['depertment'])

print(person.keys())
print(person.values())

person['job'] = 'developeer'
print(person)

person['name'] = 'khadiza khan'
print(person)

del person['age']
print(person)

for key, val in person.items():
    print(key, ":", val)

