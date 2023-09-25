"""
Задание №3

Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки”
из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в
числовые параметры используйте генераторное выражение.
"""
from sys import argv
# def func(argums):
#     num = randint(argums[0], argums[1])
#     i = 0
#     while argums[2] > i:
#         u_num = int(input(f"введите число в диапазоне от {argums[0]} до {argums[1]}:>"))
#         if u_num > num:
#             print('меньше!')
#         elif u_num < num:
#             print('больше!')
#         else:
#             print('Угадал!')
#             return True
#         i += 1
#     return False

from for_task_2_3.func_for_task import func

min_, max_, count = map(int, argv[1:])
print(func(min_, max_, count))