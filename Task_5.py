'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

*Пример:*

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
[Негафибоначчи]
'''

def fibonacci_num_positive(number):
    list_fibonacci = [1, 0, 1]
    for i in range(number - 1):
        fib = list_fibonacci[len(list_fibonacci) - 1] + list_fibonacci[len(list_fibonacci) - 2]

        nfib = fib
        if i % 2 == 0:
            nfib = -nfib

        list_fibonacci.append(fib)
        list_fibonacci.insert(0, nfib)

    return list_fibonacci



number = int(input('Введите числа: '))

print(fibonacci_num_positive(number))