'''
Напишите функцию, которая принимает строку и возвращает количество
уникальных символов в строке. Используйте для выполнения задачи
lambda-функции и map и/или filter.
Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
регистра должны считаться одинаковыми.
Пример:
message = "Today is a beautiful day! The sun is shining and the birds are
singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
Вывод: количество уникальных символов в строке — 5.
'''
def count_unique_characters(str):
    lower_str = str.lower()
    uniq_chars = list(filter(lambda char: lower_str.count(char.lower()) == 1, lower_str))
    return len(uniq_chars)


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)