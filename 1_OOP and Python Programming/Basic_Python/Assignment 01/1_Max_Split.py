# Problem Link --> https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s

st = str(input())

balance = 0
start = 0
parts = []
for i, ch in enumerate(st):
    if ch == 'L':
        balance += 1
    else: balance -= 1

    if balance == 0:
        parts.append(st[start:i+1])
        start = i+1

print(len(parts))
print(*parts, sep="\n")