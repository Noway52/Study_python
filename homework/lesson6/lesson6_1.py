N = int(input())
kolvonulev = 0

for i in range(N):
    number = int(input())
    if number == 0:
        kolvonulev += 1

print('Количество чисел равных нулю =', kolvonulev)