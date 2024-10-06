'''
Напишите программу, которая выводит на экран все строки этого файла в
обратном порядке.
'''

with open('zen.txt', 'r', encoding='utf-8') as f:
    zen_text = f.readlines()
    print(''.join(zen_text))

for str in reversed(zen_text):
    print(str.strip())