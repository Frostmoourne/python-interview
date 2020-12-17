"""
4. Написать программу, в которой реализовать две функции.

В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.

Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Например:
[91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
и
['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']


Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Например:
91 zmsebjvdgi

42 ychpwljtzn

...

Первая функция должна возвращать ссылку на файловый дескриптор


После вызова первой функции возвращаемый файловый дескриптор нужно передавать во вторую функцию
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
"""
import os
import sys
import random
import string
import itertools


def make_file(name):
    if os.path.exists(f'{name}.txt'):
        print('Такой файл уже существует')
        sys.exit(0)
    else:
        with open(f'{name}.txt', 'w', encoding='utf8') as file:
            nums = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
            # Создание всех буквенных символов ascii
            letters = string.ascii_lowercase
            # Генерация 8 рандомных букв в случайном диапазоне
            strings = [''.join(random.choices(letters, k=8)) for _ in range(random.randint(3, 10))]
            # Упаковка двух списков, если длина одного из массивов меньше, то недостающий элемент заменяется, на ?
            result = list(itertools.zip_longest(nums, strings, fillvalue='?'))
            for line in result:
                file.write('%s %s\n' % line)
            return file


def print_file(file):
    with open(file.name, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)


if __name__ == '__main__':
    print_file(make_file('123'))
