from csv import reader


def search(table, search_line):
    flag = 0
    output = open('result2.txt', 'w')

    for row in table:
        if find_string(row[2], search_line) != -1:
            flag += 1
            print(f'{row[0]} {row[2]}')
            output.write(f'{row[0]}. S/n: {row[18]} - {row[2]}, цена {row[8]} руб.\n')

    if flag == 0:
        print('Поиск не дал результатов')
    else:
        print(f'Найдено позиций: {flag}')

    output.close()


def find_string(string, search_line):
    lower_case = string.lower()
    index = lower_case.find(search_line.lower())
    return index


while True:
    search_line = input('Введите запрос: ')
    if search_line in ['0', '']:
        break

    try:
        with open('civic.csv', 'r') as csvfile:
            table = reader(csvfile, delimiter = ';')
            search(table, search_line)
    except FileNotFoundError:
        print('Файл не найден!')