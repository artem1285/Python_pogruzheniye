
'''
Задание №2 
✔ Напишите функцию, которая принимает строку текста. 
✔ Сформируйте список с уникальными кодами Unicode каждого символа 

def sort_char(data):
    lst = list(set([ord(el) for el in data]))
    res = sorted(lst, reverse = True)
    return res
   
print(sort_char("data"))

Задание №3 
✔ Функция получает на вход строку из двух чисел через пробел. 
✔ Сформируйте словарь, где ключом будет символ из Unicode, 
а значением — целое число. 
✔ Диапазон пар ключ-значение от наименьшего из введённых 
пользователем чисел до наибольшего включительно. 
введённой строки отсортированный по убыванию. 

def dict_fnc(my_str):
    dct = {ord(el): int(el) for el in sorted(my_str.split())}
    return dct
print (dict_fnc ("1 2"))

Задание №4 
✔ Функция получает на вход список чисел. 
✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии. 
'''
def sort_data(data):
    for i in  range(len(data) - 1):
        index = i
        for j in range(i + 1, len (data)):
            if data [j] < data [index]:
                index = j
        if index !=i:
            temp = data [i]
            data [i] = data [index]
            data [index] = temp

data = [9, 3, 5, 2, 4, 7, 4]
print(data)
sort_data(data)
print(data)













