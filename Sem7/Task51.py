# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики,
# и возвращают True, если это так. Если значение характеристики для разных
# объектов отличается - то False. Для пустого набора объектов, функция должна
# возвращать True. Аргумент characteristic - это функция, которая принимает
# объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [1, 21, 101, 61] same
# if same_by(lambda x: x % 2==0, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
# if not objects:
# return True
# result = list(map(characteristic,objects))
# print(result)
# return all(result) == any(result)

# values = [1, 20, 101, 61]

# if same_by(lambda x: x % 2 == 1, values):
# print('same')
# else:
# print('different')

# def same_by(characteristic, objects):
# if not objects:
# return True
# result = set(map(characteristic,objects))
# print(result)
# return len(result) == 1

# values = [1, 21, 101, 61]

# if same_by(lambda x: x % 2 == 1, values):
# print('same')
# else:
# print('different')

def same_by(characteristic, objects):
result = list(filter(characteristic,objects))
print(result)
return result == objects or not result

values = [5, 4, 78, 11]

if same_by(lambda x: x % 2 == 0, values):
print('same')
else:
print('different')
