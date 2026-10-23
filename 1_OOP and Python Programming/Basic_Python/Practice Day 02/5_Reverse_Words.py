# Problem Link --> https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q

st = str(input())
words = st.split()

ln = len(words)
for i, word in enumerate(words):
    rev = word[::-1]
    if i+1 == ln:
        print(rev)
    else:
        print(rev, end=" ")