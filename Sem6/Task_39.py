# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

import random


size_1 = int(input('Введите размер первого списка: '))
size_2 = int(input('Введите размер второго списка: '))
array_1 = [random.randint(0, 10) for i in range(size_1)]
array_2 = [random.randint(0,10) for j in range(size_2)]
print(f'Ваш первый список: {array_1}')
print(f'Ваш второй список: {array_2}')
nums = []

for i in range(size_1):
    if array_1[i] in array_2:
        i += 1
    else:
        nums.append(array_1[i])

print(nums)