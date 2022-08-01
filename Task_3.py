'''Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

*Пример:*

- [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564'''

from decimal import Decimal


def read_numbers(): 
    list_numbers = []

    for i in range(5):
        number = Decimal(input('Введите вещественное число: '))
        list_numbers.append(number)
    return list_numbers

def get_max_min(list_numbers):
    max_result = list_numbers[0]
    min_result = list_numbers[0]

    for i in range(1, len(list_numbers)):
        if list_numbers[i] > max_result:
            max_result = list_numbers[i]
        if list_numbers[i] < min_result:
            min_result = list_numbers[i]
    return max_result, min_result

def get_fractions(list_numbers):
    list_fractions = []

    for num in list_numbers:
        list_fractions.append(num - int(num))
    return list_fractions



numbers = read_numbers()
fraction = get_fractions(numbers)
max_, min_ = get_max_min(fraction)
dif = max_ - min_
print(numbers)
print(f'{max_}', f'{min_}')
print(dif)