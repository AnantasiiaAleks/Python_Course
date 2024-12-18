'''
Вывести n строк по n чисел от 1 до n**2 через \t
'''
num = int(input('Введите число: '))


for i in range(num):
    row = []
    for j in range(num):
        row.append(str(i * num + j + 1))
    print("\t".join(row))



for i in range(num):
    print(f'\t'.join(str(j) for j in range(i * num + 1, (i + 1) * num + 1)))
