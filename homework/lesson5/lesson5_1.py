a = int(input())

if (a < 0) and (a % 2 == 0):
    print("отрицательное четной число")
elif a == 0:
    print("нулевое число")
elif (a > 0) and (a % 2 == 0):
    print("положительное четное число")
else:
    print("число не является четным")