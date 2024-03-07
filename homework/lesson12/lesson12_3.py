import random

n = int(input())
c = 0
sph = []
a = [sph.append(random.randint(0, 1000)) for i in range(n)]
hs = []
b = [hs.append(random.randint(0, 100)) for j in range(n)]
zp = []

for i in range(n):
    c = sph[i] * hs[i]
    zp.append(c)

zp.sort()
print(zp)