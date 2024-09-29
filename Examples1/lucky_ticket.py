'''
Вам требуется написать программу, которая проверяет счастливость билета с
номером n и выводит на экран yes или no.
'''

ticket = input('Введите номер билета: ')
first = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
last = int(ticket[-1]) + int(ticket[-2]) + int(ticket[-3])

if first == last:
    print('yes')
if first != last:
    print('no')
