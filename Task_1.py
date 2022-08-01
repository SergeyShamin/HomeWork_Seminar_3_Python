'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.

*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

def read_numbers(): 
    list_numbers = []

    for i in range(5):
        number = int(input('Введите числа: '))
        list_numbers.append(number)
    return list_numbers


def negative_elements(list_numbers):
    negative_elements_pos = []

    for i in range(len(list_numbers)):
        if i % 2 == 1:
            negative_elements_pos.append(list_numbers[i])
    return negative_elements_pos

def sum_negative_elements(negative_elements_pos):
    _sum = 0

    for i in range(len(negative_elements_pos)):
        _sum = negative_elements_pos[i] + _sum
    return _sum

input_numbers = read_numbers()
filtered_numbers = negative_elements(input_numbers)
_sum = sum_negative_elements(filtered_numbers)

print(_sum)