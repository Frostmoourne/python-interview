"""
1. Написать программу, которая будет содержать функцию
для получения имени файла из полного пути до него.

При вызове функции в качестве аргумента должен передаваться путь до файла.
В функции необходимо реализовать «выделение» из этого пути имени файла (без расширения).

Пример:
функция принмает следующую строку - '../mainapp/views.py'

Результат:
views
"""
import re


def file_name_split(path):
    return path.split('/')[-1].split('.')[0]


def file_name_re(path):
    return re.findall(r'[-\w]+\.', path)[0][:-1]


if __name__ == '__main__':
    print(file_name_split('../mainapp/views.py'))
    print(file_name_re('../mainapp/views.py'))
