"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
from random import randint, uniform


def write_pair_nums(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num} | {float_num:.2f}\n')


write_pair_nums('task7_1.txt', 20)
