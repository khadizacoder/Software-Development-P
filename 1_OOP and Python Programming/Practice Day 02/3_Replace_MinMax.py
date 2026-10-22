# Problem link --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M

n = int(input())
arr = list(map(int, input().split()))

mn = min(arr)
mx = max(arr)

for n in arr:
    if n == mn:
        print(mx, end=" ")
    elif n == mx:
        print(mn, end=" ")
    else:
        print(n, end=" ")