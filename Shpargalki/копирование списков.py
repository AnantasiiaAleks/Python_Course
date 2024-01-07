import copy

my_list_1 = [123,234,3456,678,789, [111,222,[11,22,33],333,444]]
print(f'{my_list_1 =}')
my_list_2 = my_list_1
print(f'{my_list_2 =}')
print()
my_list_2[1] = 0
print(f'{my_list_1 =}')
print(f'{my_list_2 =}')
print()

my_list_3 = my_list_1.copy()
print(f'{my_list_1 =}')
print(f'{my_list_3 =}')
print()
my_list_3[2] = 999999
print(f'{my_list_1 =}')
print(f'{my_list_3 =}')
my_list_3[-1][2][1] = 'XXXX'
print(f'{my_list_1 =}')
print(f'{my_list_3 =}')

my_list_4 = my_list_1[:]

my_list_5 = copy.deepcopy(my_list_1)
print(f'{my_list_1 =}')
print(f'{my_list_5 =}')
print()
my_list_5[2] = 777777
print(f'{my_list_1 =}')
print(f'{my_list_5 =}')
my_list_5[-1][2][1] = '~~~~~~'
print(f'{my_list_1 =}')
print(f'{my_list_5 =}')