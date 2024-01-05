m = int(input()) #max масса в лодке
n = int(input()) #количество рыбаков
a = [] #массив для веса рыбаков
b = [] #массив для лодок
for i in range(n):
    ves = int(input()) #вес рыбака
    a.append(ves)

for i in range(len(a)):
    if a[i] + min(a) <= m:
        b += [[a[i], min(a)]]
        a[i] += m
        a[a.index(min(a))] += m
    else:
        if a[i] > m:
            continue
        else:
            b += [a[i]]
print('Минимальное количество лодок:', len(b))

