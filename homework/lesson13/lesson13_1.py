import random

a = int(input('Кол-во строк = '))
b = int(input('Кол-во столбцов = '))

m1 = [[random.randint(0, 10) for j in range(b)] for i in range(a)]
print('Первая матрица: ')
for i in range(a):
    print(m1[i])

m2 = [[random.randint(0, 10) for j in range(b)] for i in range(a)]
print('Вторая матрица: ')
for i in range(a):
    print(m2[i])

res = [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]
print("Результат сложения двух матриц: ")
for r in res:
    print(r)

