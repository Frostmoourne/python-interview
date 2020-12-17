"""
5. Усовершенствовать первую функцию из предыдущего примера.

Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла

В новый текстовый файл обеспечить запись строк вида:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Т.е. извлекаются строки из первого текстового файла
а в новый они записываются в виде, где вместо числа ставится строка

Здесь необходимо использовать регулярные выражения.
"""
import os
import sys
import random
import string
import itertools
import re


def make_file(name):
    if os.path.exists(f'{name}.txt'):
        objects = []
        with open(f'{name}.txt', 'r', encoding='utf-8') as file:
            for line in file:
                result = re.findall(r'\w+|\?', line)
                result[0] = result[1]
                objects.append(result)

        with open(f'{name}_new.txt', 'w', encoding='utf8') as new_file:
            for item in objects:
                new_file.write(' '.join(item) + '\n')

        return new_file
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
    print_file(make_file('1234'))
