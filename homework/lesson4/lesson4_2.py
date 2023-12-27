a = int(input())
b = a % 10
c = (a % 100) // 10
d = (a % 1000) // 100
e = (a % 10000) // 1000
f = a // 10000

print(f, e, d, c, b)
print(float(((c ** b) * d) // (f - e)))
