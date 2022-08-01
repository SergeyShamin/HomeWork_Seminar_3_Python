'''Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

import random

def random_list():
    list_numbers = []

    for i in range(5):
        list_numbers.append(random.randint(1, 10))
    return list_numbers

def multiple_numbers(list_numbers):
    multiple_list= []
    
    for i in range(len(list_numbers)):
        if i <= len(list_numbers) - i - 1:
            multiple = list_numbers[i] * list_numbers[len(list_numbers) - i - 1]
            multiple_list.append(multiple)
        else:
            break
        
    return multiple_list

numbers = random_list()
print(numbers)
print(multiple_numbers(numbers))