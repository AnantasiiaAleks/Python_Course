'''
Напишите программу, которая получает на вход число n (количество минут),
затем считает, сколько это будет в часах и сколько минут останется, и выводит
на экран эти два результата.
'''

minutes = int(input('Введите количество минут: '))

print(f'{minutes//60} ч. и {minutes%60} мин.')