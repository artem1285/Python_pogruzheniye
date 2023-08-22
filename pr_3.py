# //Задание №1 
'''✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка. 
✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списко

lst = [4, 4, 3, 5, 4, 1]
print(list(set(lst)))
new_lst = []
for el in lst:
    if el not in new_lst:
        new_lst.append(el)
print(new_lst)
# //Теперь что бы отсортировать по порядку, используем Ф sorted  и туда помещаем новый список
print(sorted(new_lst))  

# // Задание №3 
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже: 
✔ Целое положительное число 
✔ Вещественное положительное или отрицательное число 
✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква 
✔ Строку в нижнем регистре в остальных случаях

a = (1, 2, 1, True, None, "ghb")
dst = {}
for el_1 in a:
    obj_type = type(el_1)
    lst = []
    for el_2 in a:
        if type(el_2) == obj_type:
            lst.append(el_2)
    dst[obj_type] = lst
print(dst)

# // Задание №4 
✔ Создайте вручную список с повторяющимися элементами. 
✔ Удалите из него все элементы, которые встречаются дважды.

lst = [1, 1, 2, 2, 2, 3, 3, 5]
for el_1 in lst:
    count = 0
    for el_2 in lst:
        if el_1 == el_2:
            count +=1
    if count == 2:
        lst.remove(el_1)
        lst.remove(el_1)
print(lst)

# Задание №5 
✔ Создайте вручную список с повторяющимися целыми числами. 
✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка. 
✔ Нумерация начинается с единицы.

lst = [1, 2, 2, 3, 3, 4, 5, 5]
res = []
for i in range(len(lst)):
    if lst [i] %2 == 1 :
     res.append(i+1)   
print(res)
# лист комплитейшн
res = [i+1 for i in range(len(lst)) if lst [i] %2 == 1]
print(res)

# Задание №7 
✔ Пользователь вводит строку текста. 
✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним. 
✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке. 
✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях

# data = input ('введите еткст: ')
data = 'абракадабра'
dct = {}
for el in data:
    value = data.count(el)
    dct [el] = value
print(dct)    

# без count
data = 'абракадабра'
dct = {}
for el_1 in data:
  count = 0 
  for el_2 in data:
     if el_1 == el_2:
        count +=1
  dct [el_1] = count
print(dct)  
'''
