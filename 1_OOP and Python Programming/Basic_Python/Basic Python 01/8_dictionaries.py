
print("Python Dictionaries")

student = {
    "name" : "kahdiza",
    "age" : 22,
    "isMarrid" : "yes",
    "isStatus": False
}

print(student)
print(student["name"])
# print(type (student["isStatus"]))

x = student.keys()
y = student.values()
z = student.items()

# print(x)
# print(y)

# print(f"{x} : {y}")

student["age"] = 26
print(student)

print(student.get("age"))
print(student.get("phone"))
print(student.get("phone", "Not avl"))

student["email"] = "khadiza@gmail.com"
print(student.get("email"))

student.pop("age")
print(student)

del student["isMarrid"]
print(student)

print(student.keys())
print(student.values())
print(student.items())

# for key, val in student.items() : 
#     print(f"{key} : {val}")


friends = {
    "me" : "khadiza",
    "She" : "habiba",
    "he" : "hridoy",
    "you" : "tumi"
}

for key, val in friends.items():
    print(f"{key} : {val}")



# squares = {x : x**2 for x in range(1,6)}
# print(squares)

# squ = {x : x**x for x in range(1,11)}
# print(squ)

squ = {x : x**2 for x in range(1,11) if x%2 == 0}
print(squ)

# Nested Dictionary

users = {
    "user1": {"name" : "khadiza", "age" : 20, "City" : "khulna"},
    "user2":{"name" : "Habiba", "age" : 24, "City" : "Dhaka"},
    "user3":{"name" : "mina", "age" : 30, "City" : "Bagerhat"},
}

print(users["user1"]["name"])
print(users["user2"]["City"])
>>>>>>> dbdf44e (Basic Python M2 Done)
