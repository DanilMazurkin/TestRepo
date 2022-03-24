
class Good:
    """Represent Good"""

    MAX_COUNT = 10

    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price

    def __str__(self):
        return f'Товар цена: {self.price}, имя: {self.name}, количество: {self.count}'

    @classmethod
    def change_var(cls):
        cls.MAX_COUNT = 4

    def __repr__(self):
        return f'{id(self)}'