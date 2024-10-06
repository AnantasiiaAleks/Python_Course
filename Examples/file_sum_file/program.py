'''
Во входном файле numbers.txt записано N целых чисел, которые могут быть
разделены пробелами и концами строк. Напишите программу, которая выводит
сумму чисел во выходной файл answer.txt.
'''

with open('numbers.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    data_clear = list(map(lambda x: x.strip(), data))
    data_nums = list(map(lambda x: int(x), data_clear))
with open('answer.txt', 'w', encoding='utf-8') as f:
    f.write(str(sum(data_nums)))
