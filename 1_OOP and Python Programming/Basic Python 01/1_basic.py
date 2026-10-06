# print("Hello Khadiz...")
""" 
print("Hello"); print("How are you"); print("Khadiza")
print(50)
print(5+50) 


print("my age", 22, "and my name khadiza")
print(f"my age {22} and my name is Khadiza")

"""

#Variables

""" n = int(20)
st = str(50)
nm = float(20)

print(type(n), n); print(type(st), st); print(type(nm), nm) """

# Many Values to Multiple Variables
""" x , y, z = 'Apple', 'Banana', 'Mango'
print(x)
print(y)
print(z) """


# List Example
fruits = ['apple', 'banana', 'mango']
print(fruits)
# print(type(fruits))

fruits[2] = 'cherry'
""" 
print(fruits[0])
print(fruits[2])
print(fruits[0], fruits[1], fruits[2]) """

# Global Variables
# outside var inside allow but inside var outside not allowed

x = 'awesome'
def fun():
    print("python outside var", x) 

fun()
