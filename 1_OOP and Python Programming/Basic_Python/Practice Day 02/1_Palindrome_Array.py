# Problem link --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G

n = int(input())

arr = list(map(int, input().split()))
cpy_arr = arr
cpy_arr_rev = cpy_arr[::-1]

# print(n)
# print(arr)

if arr == cpy_arr_rev:
    print("YES")
else :
    print("NO")


# n = int(input())
# arr = list(map(int, input().split()))

# cpy_arr = arr
# rev_cpy_arr = cpy_arr[::-1]

# if arr == rev_cpy_arr :
#     print("YES")
# else:
#     print("NO")