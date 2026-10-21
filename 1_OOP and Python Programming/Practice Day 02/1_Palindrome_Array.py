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