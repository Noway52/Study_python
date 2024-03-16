class Kassa(object):
    kolvo_money = 22110

    def top_up(self, x):
        self.x = x
        Kassa.kolvo_money += x
        return f"В кассе {Kassa.kolvo_money}"

    def count_1000(self):
        return f"В кассе {Kassa.kolvo_money // 1000} целых тысяч"

    def take_away(self, y):
        if y <= self.kolvo_money:
            self.kolvo_money -= y
            return f"В кассе осталось {self.kolvo_money}"
        else:
            return f"Недостаточно денег в кассе"

r = Kassa()

print(r.top_up(5000))
print(r.count_1000())
print(r.take_away(10000))