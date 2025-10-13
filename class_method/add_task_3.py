"""
Задача 3: Класс "Прямоугольник" с шириной
Создайте класс Rectangle с приватным атрибутом _width (ширина).
В init установите self._width = 1.

Добавьте метод-геттер def get_width(self):, который возвращает self._width.
Добавьте метод-сеттер def set_width(self, new_width):,
который устанавливает self._width = new_width,
но только если new_width > 0
(иначе установите 1 по умолчанию и выведите "Ширина должна быть положительной!").

Создайте rect = Rectangle(), вызовите rect.set_width(10) (ок),
затем rect.set_width(0) (установит 1 и выведет ошибку).
Выведите print(rect.get_width()).
"""


class Rectangle:
    def __init__(self):
        self._width = 1

    def get_width(self):
        return self._width

    def set_width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            new_width = 1
            print(f'{new_width} ширина должна быть положительна')

rest = Rectangle()
rest.set_width(10)
rest.set_width(0)
print(rest.get_width())