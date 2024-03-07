import random

n = int(input())

def ttp(x):
    return x % 3


b = []
a = [b.append(random.randint(0, 100)) for i in range(n)]

b.sort()
print(b)

b.sort(key=ttp)
print(b)