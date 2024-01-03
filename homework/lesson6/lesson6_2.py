X = int(input())
x = int(input())
delit = 1
kolvo = 0

while x > 0:
    for i in range(X):
        if X % delit == 0:
            kolvo += 1

        x -= 1
        delit += 1

print(kolvo)




