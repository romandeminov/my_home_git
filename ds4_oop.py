class Airplane:
    def __init__(self, type, max_count, current_count):
        self.type = type
        self.max_count = max_count
        self.current_count = current_count

    def __add__(self, other):
        return self.current_count + other

    def __sub__(self, other):
        return self.current_count - other

    def __iadd__(self, other):
        self.current_count += other
        return self

    def __isub__(self, other):
        self.current_count -= other
        return self

    def __eq__(self, other):
        if self.type == other:
            return 'одинаковый тип самолётов'
        else:
            return 'разный тип самолётов'

    def __lt__(self, other):
        if self.max_count < other:
            return 'в этом самолёте максимальное количество пассажиров меньше'
        else:
            return 'в этом самолёте максимальное количество пассажиров больше'

    def __gt__(self, other):
        if self.max_count > other:
            return 'в этом самолёте максимальное количество пассажиров больше'
        else:
            return 'в этом самолёте максимальное количество пассажиров меньше'

    def __str__(self):
        return f'это самолёт типа {self.type} с максимальным количеством пассажиров = {self.max_count}'

    def __int__(self):
        return f'текущее количество пассажиров = {self.current_count}'


airplane = Airplane('military', 100, 63)
airplane += 20
print(airplane.current_count)
airplane -= 5
print(airplane.current_count)
print(airplane + 20)
print(airplane - 20)
print(airplane > 30)
print(airplane < 200)
print(airplane)
print(airplane.__int__())
print(airplane == 'military')