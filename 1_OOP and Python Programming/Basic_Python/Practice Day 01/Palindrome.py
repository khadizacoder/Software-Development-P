num = str(input())

rev = num[::-1]
print(int(rev))

if num == rev:
    print("YES")
else: 
    print("NO")