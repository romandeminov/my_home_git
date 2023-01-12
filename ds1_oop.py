class Automobil:
    def __init__(self, name='', year='', producer='', amount='', color='', cost=''):
        self.name = name
        self.year = year
        self.producer = producer
        self.amount = amount
        self.color = color
        self.cost = cost

    @property
    def set_up(self):
        self.name = input('Введите название автомобиля')
        self.year = input('Введите год выпуска автомобиля')
        self.producer = input('Введите производителя автомобиля')
        self.amount = input('Введите объем двигателя автомобиля')
        self.color = input('Введите цвет автомобиля')
        self.cost = input('Введите цену автомобиля')

    def show_up(self):
        print(f'название автомобиля: {self.name}')
        print(f'год выпуска автомобиля: {self.year}')
        print(f'производитель автомобиля: {self.producer}')
        print(f'объем двигателя автомобиля: {self.amount}')
        print(f'цвет автомобиля: {self.color}')
        print(f'цена автомобиля: {self.cost}')

    def show_exactly(self):
        choice = input("""Введите
        1 - если хотите название автомобиля
        2 - если хотите год выпуска автомобиля
        3 - если хотите производителя автомобиля
        4 - если хотите объем двигателя автомобиля
        5 - если хотите цвет автомобиля
        6 - если хотите цену автомобиля
        :::""")
        if choice in '123456':
            if choice == '1':
                print(self.name)
            elif choice == '2':
                print(self.year)
            elif choice == '3':
                print(self.producer)
            elif choice == '4':
                print(self.amount)
            elif choice == '5':
                print(self.color)
            elif choice == '6':
                print(self.cost)
        else:
            print('вы ввели не то число')


car = Automobil()
car.set_up()
car.show_up()
car.show_exactly()