# Write about *args and **kwargs of Python with proper examples.

def sum(*args):
    total = 0
    for n in args:
        total += n

    return total

print(sum(3,4,5))
print(sum(2,2,2,2))


def person(**kargs):
    for key, val in kargs.items():
        print(f"{key} : {val}")


person(name = "Khadiza", age= 22, sub = "Economic") 