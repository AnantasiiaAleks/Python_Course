# Пользователь вводит некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве
# строки. Как превратить list строк в list чисел?

data = '15 156 96 3 5 8 52 5'
print(data) # Выводит строку

data_1 = data.split()
print(data_1) # Выводит список строк

data_2 = list(map(int, data.split()))
print(data_2) # Преобразует строку в список чисел