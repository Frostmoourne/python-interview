"""
3. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return print(f'Цена на товар "{self.get_name()}": {self.get_price()}')


if __name__ == '__main__':

    item = ItemDiscountReport('Принтер', '15000')
    item.get_parent_data()
