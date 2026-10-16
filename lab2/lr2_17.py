from csv import reader
from datetime import datetime
import os


def open_table():
    try:
        with open('civic.csv', 'r') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            table = table[1:]
            return table
    except FileNotFoundError:
        print('Файл не найден!')
        return 0


def search(table):
    searchline = input('Введите шаблон поиска: ')
    if searchline in ['0', '']:
        return 0
    elif searchline.isalpha() == False:
        return 0
    output = open('result.txt', 'w')
    output.write(f'Поиск от: {datetime.today()}\n\n')
    flag = 0
    for row in table:
        if find_string(searchline, row[2]) != -1:
            print(row[2])
            output.write(f'ID {row[0]}. {row[2]} Цена {row[8]} руб. S/n {row[18]}\n')
            flag += 1

    if flag == 0:
        print('Ничего не найдено!')
    else:
        print(f'Найдено позиций: {flag}')
    input('Нажмите Enter')
    output.close()


def find_string(searchline, string):
    string = string.lower()
    index = string.find(searchline.lower())
    return index


def search_id(table):
    id_line = input('Введите ID: ')
    if id_line in ['0', '']:
        return 0
    elif id_line.isnumeric() == False:
        return 0
    flag = 0
    for row in table:
        if id_line == row[0]:
            print(f'{row[0]} {row[2]}')
            flag = 1
    if flag == 0:
        print('Ничего не найдено, нажмите Enter')
    else:
        print('Нажмите Enter')
    input()


while True:
    os.system('cls')
    if open_table() == 0:
        break
    print('Меню:\n1 - Поиск по названию\n2 - Поиск по ID\n0 - Выход')
    menu = input('Выберите пункт меню: ')
    match menu:
        case '1':
            search(open_table())
        case '2':
            search_id(open_table())
        case '0':
            break
        case _:
            print('Нет пункта меню, нажмите Enter')
            input()




    # for row in table:
        # print(f'ID {row[0]}. {row[2]} Цена {row[8]} руб. S/n {row[18]}')