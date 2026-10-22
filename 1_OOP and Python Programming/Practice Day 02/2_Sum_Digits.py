# Problem link --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/K

n = int(input())
# arr = list(map(int, input().split()))
st = str(input())

# arr = list(st)
arr = list(map(int,st))

# print(st)
# print(arr)

sumation = 0
for num in arr:
    sumation = sumation + num

print(f'{sumation}')


# n = int(input())
# st = str(input())

# arr = list(map(int, st))
# ans = 0
# for n in arr:
#     ans = ans + n

# print(ans)