"""
Разложить число на простые сомножители. Результат записать в виде примера
вида 48 = 2 * 2 * 2 * 2 * 3
"""
import math

def prime_multipliers(num: int) -> list:
    """
    выводит в формате примера перечень простых сомножителей
    :param num: целое число
    """
    digits = []
    if is_prime(num):
        digits.append(1)
        digits.append(num)
    else:
        while num % 2 == 0:
            digits.append(2)
            num //= 2
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            while num % i == 0:
                digits.append(i)
                num //= i
        if num > 2:
            digits.append(num)
    return digits


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
    number = int(input('Введите целое число: '))
    multipliers = prime_multipliers(number)
    result = f'{number} = ' + ' * '.join(map(str, multipliers))
    print(result)