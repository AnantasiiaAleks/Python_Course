'''
Вам дан список оценок студентов, в котором некоторые оценки могут быть
недействительными (отрицательные числа). Напишите функцию
normalize_grades, которая удаляет недействительные оценки и возвращает
список всех оставшихся оценок, отсортированных в порядке убывания.
Пример:
grades = [95, -10, 82, 90, -5, 77]
print(normalize_grades(grades))
На выходе: [95, 90, 82, 77]
'''

def normalize_grades(grades: list) -> list:
    """
    очищает список, убирая отрицательные числа и сортирует в порядке убывания
    :param grades: список оценок до очистки
    :return: список оценок без недействительных и отсортированный по убыванию
    >>> print(normalize_grades([95, -10, 82, 90, -5, 77]))
    [95, 90, 82, 77]
    """
    good_grades = [grade for grade in grades if grade >= 0]
    return sorted(good_grades, reverse=True)

if __name__ == '__main__':
    grades = [95, -10, 82, 90, -5, 77]
    print(normalize_grades(grades))