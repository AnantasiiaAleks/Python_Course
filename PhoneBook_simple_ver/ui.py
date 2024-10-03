from logger import input_data, print_data

def interface():
    print('Привет! Вы попали в специальный бот-справочник от GB\n'
          'Я умею:\n'
          '1 - Ввод данных\n'
          '2 - Вывод данных')
    command = int(input('Введите число: '))

    while command != 1 and command != 2:
        print('Неверный ввод')
        command = int(input('Введите число: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()