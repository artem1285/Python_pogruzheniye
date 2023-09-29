"""
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

"""

from random import choices
from random import randbytes
from random import randint
from string import ascii_lowercase
from os import makedirs, chdir, getcwd


def func(ext, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096,
         files=42):
    for i in range(files):
        name = ''.join(
            choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        size = randint(min_rand_bytes, max_rand_bytes)
        with open(name, 'wb') as f:
            f.write(randbytes(size))


def func_2(files=10, **kwargs):
    dct = kwargs
    val = []
    for k, v in dct.items():
        val.append(v)
    for i in range(files):
        ext = str(*choices(val))
        func(ext, files=1, min_len=6, max_len=30, min_rand_bytes=256,
             max_rand_bytes=4096)


def func_3(dir):
    my_path = getcwd() + dir
    try:
        makedirs(my_path)
        chdir(my_path)
    except FileExistsError:
        chdir(my_path)
    func_2(5, a='.txt', b='.doc', c='.exe')
    chdir('..')


func_3('\\task6')