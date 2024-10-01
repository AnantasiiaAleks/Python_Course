'''
Напишите свою функцию sum, которая должна быть более гибкой, чем
стандартная. Она должна уметь складывать числа:
● из списка списков,
● набора параметров.
'''

def my_sum(*args):
    total_sum = 0

    for i_elem in args:

        if isinstance(i_elem, int):                                 # проверка на число
            total_sum += i_elem
        elif isinstance(i_elem, (list, tuple)):                     # проверка список или кортеж
            for n in i_elem:
                total_sum += my_sum(n)                              # Рекурсивный вызов функции

    return total_sum

# print(my_sum([[1, 2, [3]], [1], 3]))