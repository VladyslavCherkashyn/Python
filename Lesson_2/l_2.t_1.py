"""Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

my_list = [1, 2.3, None, "kekw", (1, 2), {2, 3}, frozenset({6, 7}), True, {1: 2, "key_1": 400}, [4, 5]]

for el in my_list:
    print(type(el))