# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в
# котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка
# будут соответствовать правилам задания ключей в словарях.

from random import randint
def to_dict(lst):
    some_dict = {element: element for element in lst}
    return some_dict

lst = []

def add_lst():
    [lst.append(randint(1, 10)) for i in range(0, 10)]
    return lst

print(to_dict(add_lst()))