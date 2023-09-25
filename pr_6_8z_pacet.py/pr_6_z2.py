
__all__ = ["func"]
"""
Задание №2
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа:
нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных
границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
from random import randint


def func(start, stop, count):
    num = randint(start, stop)
    i = 0
    while count > i:
        u_num = int(input(f"введите число в диапазоне от {start} до {stop}:>"))
        if u_num > num:
            print('меньше!')
        elif u_num < num:
            print('больше!')
        else:
            print('Угадал!')
            return True
        i += 1
    return False

from for_task_2_3.func_for_task import func

print(func(1, 3, 3))