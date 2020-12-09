"""
2. Инкапсулировать оба параметра (название и цену)
товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы
будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return print(f'Цена на товар {self.__name}: {self.__price}')


if __name__ == '__main__':

    item = ItemDiscountReport('Принтер', '15000')
    item.get_parent_data()
