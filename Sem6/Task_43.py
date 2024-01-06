# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.

from random import randint

size_list = randint(5, 10)

list_1 = [randint(1, 5) for _ in range(size_list)]
print(list_1)
count_nums = 0
for i in range(size_list - 1):
    for j in range(i + 1, size_list):
        if list_1[i] == list_1[j]:
            count_nums += 1
print(count_nums)
counter = 0
for i in range(size_list - 1):
    counter += list_1[i+1:].count(list_1[i])
print(counter)