# Problem link --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Y

# O(NQ)
# n, q = map(int, input().split())
# arr = list(map(int, input().split()))

# for _ in range(q):
#     l, r = map(int, input().split())
#     sum = 0
#     for i, n in enumerate(arr):
#         if i+1 >= l and i+1 <= r:
#             sum+=n

#     print(sum)


# Efficient solution — Prefix Sum

n, q = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * (n+1)

for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l-1])