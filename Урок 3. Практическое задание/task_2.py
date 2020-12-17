"""
2. Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.

Примеры:

Введите число: test
Вы ввели не число

Введите число: 45
Число 45 - целое

Введите число: 45.45
Число 45.45 - дробное
Левая и правая части совпадают

Введите число: 45.34
Число 45.34 - дробное
Левая и правая части не совпадают
"""


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def num_test():
    while True:
        num = input('Введите число: ')
        if isint(num):
            print(f'Число {int(num)} - целое')
        elif isfloat(num):
            num_split = str(num).split('.')
            print(f'Число {num} - дробное')
            if num_split[0] == num_split[1]:
                print('Левая и правая части совпадают')
            else:
                print('Левая и правая части не совпадают')
        else:
            print('Вы ввели не число')


if __name__ == '__main__':
    num_test()
