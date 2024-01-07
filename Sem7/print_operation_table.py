# Напишите функцию print_operation_table(operation, num_rows, num_columns),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
# строки и столбца. По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
# Если строк меньше двух, выдайте текст: ОШИБКА! Размерности таблицы должны быть больше 2!

def print_operation_table(operation, num_rows = 9, num_columns = 9):
    if num_rows >= 2:
        a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
        for i in a:
            print(*[f"{x}" for x in i])
    else:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')



print_operation_table(lambda x, y: x * y)
