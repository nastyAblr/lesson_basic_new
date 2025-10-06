"""
Объявите класс с именем TravelBlog и объявите в нем атрибут:

total_blogs: 0

Создайте экземпляр этого класса с именем tb1,
сформируйте в нем два локальных свойства:

name: 'Франция'

days: 6

Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.
Создайте еще один экземпляр класса TravelBlog с именем tb2,
сформируйте в нем два локальных свойства:

name: 'Италия'

days: 5

Увеличьте значение атрибута total_blogs класса TravelBlog
еще на единицу.

"""
from calendar import day_name
from tkinter.font import names


class TravelBlog:
    total_blogs = 0

    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __str__(self):
        return f'Предложение: {self.name} на {self.days} дней'


tb1 = TravelBlog('Франция', 6)
print(tb1)

TravelBlog.total_blogs += 1
print(TravelBlog.total_blogs)

tb2 = TravelBlog('Италия', 5)
print(tb2)

TravelBlog.total_blogs += 1
print(TravelBlog.total_blogs)
