'''
У вас есть список сотрудников, где каждый сотрудник представлен кортежем из
имени и возраста. Напишите функцию average_age, которая находит и
возвращает средний возраст сотрудников, исключая тех, чей возраст меньше
нуля (ошибочные данные).
Пример:
Входные данные:
employees = [("Alice", 30), ("Bob", -5), ("Charlie", 40)]
Ожидаемый результат:
35.0
'''
def average_age(employees: list[tuple]) -> float:
    """
    :param employees: список сотрудников, где каждый сотрудник представлен кортежем из имени и возраста
    :return: средний возраст сотрудников, исключая тех, чей возраст меньше нуля

    >>> print(average_age([("Alice", 30), ("Bob", -5), ("Charlie", 40)]))
    35.0
    """

    ages = [age for name, age in employees if age >= 0]
    return sum(ages) / len(ages) if ages else 0

if __name__ == '__main__':
    list_employees = [("Alice", 30), ("Bob", -5), ("Charlie", 40)]
    print(average_age(list_employees))