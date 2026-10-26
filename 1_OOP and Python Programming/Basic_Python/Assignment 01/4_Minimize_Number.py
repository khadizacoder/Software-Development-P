#  https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P

# n = int(input())
# arr = list(map(int, input().split()))

# ans = 0

# while True:
#     even = 0
#     odd = False

#     for x in arr:
#         if x%2 == 1:
#             odd = True


#     if odd: break
#     ans+=1

#     if not odd:
#         for i in range(len(arr)):
#             arr[i] //=2


# print(ans)



n = int(input())
arr = list(map(int, input().split()))

ans = 0
while True:
    odd = False

    for n in arr:
        if n%2 == 1:
            odd = True

    if odd: break
    ans+=1

    for i in range(len(arr)):
        arr[i] //= 2

print(ans)