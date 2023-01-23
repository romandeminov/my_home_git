class Money:
    def __init__(self, name_of_cur, whole_part, fractional_part, symbol_of_cur):
        self.name_of_cur = name_of_cur
        self.whole_part = whole_part
        self.fractional_part = fractional_part
        self.symbol_of_cur = symbol_of_cur

    @property
    def make_full_number(self):
        self.full_number = str(self.whole_part) + '.' + str(self.fractional_part)
        return self.full_number

    def show_full_number(self):
        print(self.make_full_number)


dollar = Money('dollar', 22, 55, '$')
dollar.show_full_number()