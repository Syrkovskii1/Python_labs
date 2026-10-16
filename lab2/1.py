

# вариант 3 
from csv import reader
from datetime import datetime
import os
import random


def open_table():
    try:
        with open('books.csv', 'r', encoding='cp1251') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            print(table[0])
            table = table[1:]
         
            return table
    except FileNotFoundError:
        print('Файл не найден!')
        return 0

table = open_table()
k = 0
for x in range(0,len(table)):
    if len(table[x][1]) > 30:
       # print(table[x][1])
        k+=1 

print(k)

'''
for book in table:
    print(book[6][6:10])
    if len(book[6][6:10]) != 4:
        print('erro')

'''

#/////////////////////////////////////////////////////
def search():
    #print(table[0][6])
    found_count = 0
    searchline = input('Введите шаблон поиска: ')
    if searchline != ' ':
        for book in table:
            if (searchline in book[3]) and (book[6][6:10] in ['2014', '2016', '2017']):
                #print(book)
                print(f"{book[1]} — {book[3]} {book[6][6:10]}")
                found_count += 1
    if found_count == 0:
        print("Ничего не найдено")
search()


def random_chose():
    random_books = random.sample(table, 20)
    k = 0
    with open('result.txt', 'w', encoding='utf-8') as f:
        for book in random_books:
            k+=1 
            #print(f"{book[1]}. {book[3]} - {book[6][6:10]}")
            line = f"{k}. {book[3]}. {book[1]} - {book[6][6:10]}\n"
            f.write(line)

random_chose()