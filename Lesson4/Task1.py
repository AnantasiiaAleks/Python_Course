# В списке хранятся числа. Нужно выбрать только четные числа и
# составить список пар (число; квадрат числа)
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2,4), (8,64), (38. 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
#
# print(res)

def select(f, col):     # Возвращает список, в котором к каждому элементу применили функцию f
    return [f(x) for x in col]  # можно не использовать, если map

def where(f, col):      # Возвращает только те значения, которые прошли проверку условия f(x)
    return [x for x in col if f(x)] # можно не использовать, если filter

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)    # можно вместо select использовать map
print(res)
res = where(lambda x: x % 2 == 0, res) # вместо where можно использовать filter
print(res)
res = list(select(lambda x: (x, x ** 2), res))  # select можно заменить на map
print(res)