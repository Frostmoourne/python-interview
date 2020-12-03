"""
Задание 2.	Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    заполните далее

Пример:
[
('mainapp', 'admin.py'),
('mainapp\\management\\commands', 'seed_db.py'),
...
]
"""
import os


def print_directory_contents(s_path):
    """Функция прнимает на вход путь до каталога
    и распечатывает в рекурсивном виде его содержимое"""
    current_dir = [s_path]
    s_path = os.path.abspath(s_path)
    for item in os.listdir(s_path):
        current_dir.append(item)
        if os.path.isdir(os.path.join(s_path, item)):
            print_directory_contents(os.path.join(s_path, item))
    current_dir = tuple(current_dir)
    print(current_dir)


if __name__ == '__main__':
    print_directory_contents(os.getcwd())
