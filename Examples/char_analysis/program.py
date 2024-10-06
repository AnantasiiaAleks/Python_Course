'''
Напишите программу, которая
выполняет частотный анализ, определяя долю каждой буквы английского
алфавита в общем количестве английских букв в тексте, и выводит результат в
файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
учитывать не нужно.
В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с
тремя знаками в дробной части. Буквы должны быть отсортированы по
убыванию их доли. Буквы с равной долей должны следовать в алфавитном
порядке.
'''
alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзиклмнопрстуфхцчшщъыьэюя'
total_letters = 0
with open('voyna-i-mir.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

letter_count = {letter: 0 for letter in alphabet}
for char in text:
    if char in alphabet:
        letter_count[char] += 1
        total_letters += 1

letter_freq = {letter: (count / total_letters) for letter, count in letter_count.items() if count > 0}

sorted_letters = sorted(letter_freq.items(), key=lambda x: (-x[1], x[0]))

with open('analysis.txt', 'w', encoding='utf-8') as f:
    for letter, freq in sorted_letters:
        f.write(f"{letter} {freq:.3f}\n")


