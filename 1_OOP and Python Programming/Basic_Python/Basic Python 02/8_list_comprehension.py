numbers = [1,8,4,9,5,3,2]

odd=[]
for num in numbers:
    if num%2 == 1:
        odd.append(num)

print(odd)

odd_nums = [num for num in numbers]
print(odd_nums)

# odd_nums2 = [num for num in numbers if num%2 == 1]
odd_nums2 = [num for num in numbers if num%2 == 1 if num % 5 == 0]
print(odd_nums2)

names = ["mina", "raju", "amin"]
ages = [22, 54, 13]

age_cmb = []
for name in names:
    print(f'name {name}')
    for age in ages:
        print(f'age {age}')
        age_cmb.append([name, age])

print(age_cmb)
print(2**4)

def per(**kargs):
    for key, val in kargs.items():
        print(f"{key} {val}")

per(Name="Khadiza", Age="30")