"""
Объявите класс Book со следующим набором сеттеров и геттеров:

set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;

set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;

set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;

get_title(self) - получение значения локального приватного свойства __title объектов класса Book;

get_author(self) - получение значения локального приватного свойства __author объектов класса Book;

get_price(self) - получение значения локального приватного свойства __price объектов класса Book;

Объекты класса Book предполагается создавать командой:

book = Book(автор, название, цена)

При этом, в каждом объекте должны создаваться приватные локальные свойства:

__author - строка с именем автора;

__title - строка с названием книги;

__price - целое число с ценой книги.
"""


class Book:

    def __init__(self, author, title, price):
        self.__author = author.title()
        self.__title = title
        self.__price = price

    def get_author(self):
        return self.__author.istitle()

    def set_author(self, author):
        if type(author) == str:
            return author
        else:
            print('Ошибка')

    def get_title(self, title):
        return self.__title.istitle()

    def set_title(self, title):
        if type(title) == str:
            return title
        else:
            print('Ошибка')

    def get_price(self, price):
        return self.__title

    def set_price(self, price):
        if type(price) == float and price > 0:
            return self.__price
        else:
            print('Ошибка')

    def __str__(self):
        return f'Автор: {self.__author}, Название: {self.__title}, Цена: {self.__price}'

book_1 = Book('толстой л.н.', 'Анна Каренина', 20.5)
print(book_1)