# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
import math
n = int(input('Введите, сколько км проезжает машина за день: '))
m = int(input('Введите общее количество км: '))
t = m/n
print(f'за {math.ceil(t)} дней проедет машина {m} км')
