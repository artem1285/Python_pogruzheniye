"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более кор
"""


def my_func():
    with open('task7_1.txt', 'r', encoding='utf-8') as f_nums, \
            open('task7_2.txt', 'r', encoding='utf-8') as f_names:
        nums = f_nums.readlines()
        names = f_names.readlines()

    for_write = []
    long = max(len(nums), len(names))
    i = 0
    while len(nums) != len(names):
        if len(nums) > len(names):
            names.extend(names[:len(nums) - len(names)])
        else:
            nums.extend(nums[:len(names) - len(nums)])

    while i < long:
        name = names[i]
        num = nums[i]
        a, b = map(float, num.split('|'))
        mult = a * b

        if mult >= 0:
            for_write.append(f'{name.upper().rstrip()} - {round(mult)}\n')
        else:
            for_write.append(f'{name.lower().rstrip()} - {abs(mult)}\n')
        i += 1

    with open("task7_3.txt", 'w', encoding='utf-8')as f:
        f.writelines(for_write)


my_func()
