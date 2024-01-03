A = int(input())
B = int(input())

while A <= B:
    if A % 2 == 0:
        Chislo = A
        A += 1
        print(Chislo, end=' ')
    else: A += 1
