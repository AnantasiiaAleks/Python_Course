'''
Вводится целое число s которое является площадью прямоугольника.
Вывести целочисленные стороны всех прямоугольников, площадь которых равна s. Каждую пару с новой строки,
в любом порядке без повторений
'''
import math


def rectangle_sides(s: int) -> list:
    """
    Функция подбирает целочисленные значения возможных сторон прямоугольника по известной площади
    :param s: площадь прямоугольника
    """
    res = []
    if s < 1:
        raise ValueError('Площадь не может быть 0 или отрицательным числом.')
    if is_prime(s):
        res.append([1, s])
    else:
        for a in range(1, int(math.sqrt(s)) + 1):
            if s % a == 0:
                b = int(s / a)
                res.append([a, b])

    return res



def is_prime(num: int) -> bool:
    """
    Является ли число простым
    :param num: целое число
    """

    for i in range(num):
        if num > 1:
            for divider in range(1, num // 2):
                if num % divider == 0:
                    return False
            else:
                return True


if __name__ == '__main__':
    print(*rectangle_sides(24))