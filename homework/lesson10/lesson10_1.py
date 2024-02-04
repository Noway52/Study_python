pets = {}
pets2 = {}

while (True):
    k = input("Введите имя питомца: ")
    if k == '':
        break
    else:
        k1 = input('Вид питомца: ')
        k2 = int(input('Возраст питомца: '))
        k3 = input('Имя владельца:  ')
        pets2 = {'Вид питомца:': k1, 'Возраст питомца:': k2, 'Имя владельца:': k3}
        pets[k] = pets2

for key, value in pets.items():
    vid = value['Вид питомца:']
    old = value['Возраст питомца:']
    name = value['Имя владельца:']
    year_case = ''
    if old % 10 == 1 and old != 11 and old % 100 != 11:
        year_case = 'год'
    elif 1 < old % 10 <= 4 and old != 12 and old != 13 and old != 14:
        year_case = 'года'
    else:
        year_case = 'лет'

print("Это", vid, "по кличке", key,". Возраст питомца:", old, year_case, ". Имя владельца:", name)