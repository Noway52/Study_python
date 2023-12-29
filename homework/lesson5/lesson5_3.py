invest = int(input())
maik = int(input())
vany = int(input())

if (maik >= invest) and (vany >= invest):
    print('2')
elif (maik >= invest) and (vany < invest):
    print('Maik')
elif (maik < invest) and (vany >= invest):
    print('Ivan')
elif (maik + vany) >= invest:
    print('1')
else:
    print('0')