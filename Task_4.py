'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.

*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

def convert_numbers(number):
    list_number = []

    b = number

    while b > 1:
        a = b % 2 
        b = int(b / 2)
        list_number.append(a)

        if b == 1:
            list_number.append(b)

    return list_number

def reverse_list(list_number):
    result_list = []

    for i in range(len(list_number)):
        result_list.append(list_number[len(list_number) - i - 1])
    return result_list

number = int(input('Введите число: '))
print(reverse_list(convert_numbers(number)))

#print(convert_numbers(number)[::-1])
