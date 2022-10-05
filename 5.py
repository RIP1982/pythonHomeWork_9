# Дана строка в виде случайной последовательности чисел от 0 до 9.
#
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте
# функцию count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто
# встречаемых чисел.

from random import randint

lst = []
def count_it(sequence):
    some_dict = {int(item): sequence.count(item) for item in sequence}
    sort_dict = sorted(some_dict.items(), key=lambda element: element[1])
    sort_dict = dict(sort_dict[-3:])
    return sort_dict, some_dict

def add_string(lst):
    [lst.append(randint(0, 10)) for i in range(0, 10)]
    lst = ''.join(map(str, lst))
    return lst

print(count_it(add_string(lst)))
