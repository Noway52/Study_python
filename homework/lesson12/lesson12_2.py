import random


n = int(input())
count = 0
b = []
a = [b.append(random.randint(0, 10)) for i in range(n)]

b.sort()
print(b)

b_unique = []
for i in b:
    if i not in b_unique:
        count += 1
        b_unique.append(i)
print(len(b_unique))

