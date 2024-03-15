class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def vivod(self):
        print(f'Название автомобиля: {self.name}. Скорость: {self.max_speed}. Пробег: {self.mileage} ')

    def seating_capacity(self, capacity=50):
        print(f"Вместимость одного автобуса {self.name}   {capacity} пассажиров")

Autobus = Transport('Renault Logan', '180 km/h', 12)

Autobus.vivod()
Autobus.seating_capacity()
