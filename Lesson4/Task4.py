data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)    # можно вместо select использовать map
res = filter(lambda x: x % 2 == 0, res) # вместо where можно использовать filter
res = list(map(lambda x: (x, x ** 2), res))  # select можно заменить на map
print(res)