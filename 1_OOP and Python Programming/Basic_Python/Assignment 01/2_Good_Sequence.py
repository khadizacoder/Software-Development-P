# Problem Link --> https://atcoder.jp/contests/arc087/tasks/arc087_a
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

# print(arr.count(1))
cnt = Counter(arr)
# print(cnt)

remove = 0
for n in cnt:
    if cnt[n] < n:
        remove += cnt[n]
    else:
        remove += cnt[n] - n

print(remove)