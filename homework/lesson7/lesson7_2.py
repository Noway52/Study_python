N = int(input())
m = []

for i in range(N):
    a = int(input())
    m.append(a)

m.insert(0, m.pop())
print(m)