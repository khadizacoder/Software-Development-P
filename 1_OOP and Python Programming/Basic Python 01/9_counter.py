from collections import Counter

numbers = [1,2,1,3,2,3,2,1,6, 2]
count = Counter(numbers)

print(count)
print(count.most_common(1))