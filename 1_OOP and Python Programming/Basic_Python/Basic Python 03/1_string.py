name1 = "kahdiza khatun"
name2 = 'Khadiza\'s Khatun' #escape

# multi line string
name3 = '''
my name is khadiza
my age 22
my collage khulna govt mohila collage
'''

print(name3)
print(name2[1:6])
print(name1[-4])

for char in name1:
    print(char)

if 'khatun' in name1:
    print("exists")


# string methods

print(name1.upper())
print(name1.capitalize())

print(', '.join(name3))