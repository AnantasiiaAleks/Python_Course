'''
В базе магазина электроники есть список видеокарт компании NVIDIA разных
поколений. Вместо полных названий хранятся только числа, которые обозначают
модель и поколение видеокарты. Недавно компания выпустила новую линейку
видеокарт. Самые старшие поколения разобрали за пару дней.
Напишите программу, которая удаляет наибольшие элементы из списка видеокарт
'''
count = int(input('Введите количество карт: '))
full_list = list()
res_list = []
max_item = 0

for i in range(count):
    card = int(input('Введите номер карты: '))
    full_list.append(card)
    if card > max_item:
        max_item = card
for i in range(count):
    if full_list[i] < max_item:
        res_list.append(full_list[i])

print('Старый список видеокарт: [', end=' ')
for item in range(count):
    print(full_list[item], end=' ')
print(']')
# Вывод нового списка видеокарт
print('Новый список видеокарт: [', end=' ')
for item in range(len(res_list)):
    print(res_list[item], end=' ')
print(']')
