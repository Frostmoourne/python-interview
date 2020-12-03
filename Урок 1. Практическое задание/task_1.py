"""
Задание 1. Написать функцию, реализующую вывод таблицы умножения
размерностью AｘB. Первый и второй множитель должны задаваться
в виде аргументов функции. Элементы строки
(элементы таблицы умножения) должны разделяться табуляцией.

Пример:
Таблица умножения 10x10:
0	1	2	3	4	5	6	7	8	9	10
1	1	2	3	4	5	6	7	8	9	10
2	2	4	6	8	10	12	14	16	18	20
3	3	6	9	12	15	18	21	24	27	30
4	4	8	12	16	20	24	28	32	36	40
5	5	10	15	20	25	30	35	40	45	50
6	6	12	18	24	30	36	42	48	54	60
7	7	14	21	28	35	42	49	56	63	70
8	8	16	24	32	40	48	56	64	72	80
9	9	18	27	36	45	54	63	72	81	90
10	10	20	30	40	50	60	70	80	90	100

Обратите внимание на первую строку и столбец!
На пересечении их элементов и находятся искомые значения
ЭТИ СТРОКА И СТОЛБЕЦ ОБЗЯТЕЛЬНО ДОЛЖНЫ БЫТЬ
"""
from tabulate import tabulate


def multiplication_table(first_num: int, second_num: int):
    """Функция отображения таблицы умножения a x b"""
    # Создаем ширину ряда таблицы
    first_row = []
    for num in range(first_num + 1):
        first_row.append(num)
    # Итоговая таблица с первым рядом
    table = [first_row]
    for j in range(1, second_num + 1):
        # Добавляем цифру из столбца на первое место в ряде
        row = [j]
        for i in first_row[1:]:
            row.append(i * j)
        table.append(row)
    print(f'Таблица Умножения {first_num}x{second_num}:')
    return print(tabulate(table))


if __name__ == '__main__':
    multiplication_table(9, 9)
