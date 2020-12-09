"""
6. Проверить на практике возможности полиморфизма.

Необходимо разделить дочерний класс ItemDiscountReport на два класса.

Инициализировать классы необязательно.

Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.

Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class FirstItemDiscountReport(ItemDiscount):

    def get_info(self):
        return f'Название товара: {self.get_name()}'


class SecondItemDiscountReport(ItemDiscount):

    def get_info(self):
        return f'Цена товара: {self.get_price()}'


def cls_handler(obj):
    print(obj.get_info())


if __name__ == '__main__':
    items = [FirstItemDiscountReport('Принтер', 15000), SecondItemDiscountReport('Принтер', 15000)]
    for item in items:
        print(item.get_info())
        cls_handler(item)
