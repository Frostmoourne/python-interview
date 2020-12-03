"""
Задание 3.	Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.

Пример:
(
[18, 22, 21, 23, 18, 21, 19, 16, 18, 8],
{'elem_18': 18, 'elem_22': 22, 'elem_21': 21, 'elem_23': 23,
'elem_19': 19, 'elem_16': 16, 'elem_8': 8}
)
"""
import random


def random_elements(first_num, second_num):
    """Функция-генератор рандомных чисел"""
    nums_list = []
    nums_dict = {}
    for _ in range(first_num, second_num):
        number = random.randrange(first_num, second_num)
        if number == 0:
            continue
        nums_list.append(number)

    for j in nums_list:
        nums_dict[f'elem_{j}'] = j

    return nums_list, nums_dict


if __name__ == '__main__':
    print(random_elements(0, 10))
