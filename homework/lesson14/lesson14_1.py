my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def posl(my_list):
    if my_list == []:
        print("Конец списка")
    else:
        print(my_list.pop(0))
        posl(my_list)

posl(my_list)

