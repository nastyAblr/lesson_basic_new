"""
Создайте класс Person с приватным атрибутом _age (возраст).
В конструкторе init установите self._age = 0.

Добавьте метод-геттер def get_age(self):, который возвращает self._age.
Добавьте метод-сеттер def set_age(self, new_age):,
который устанавливает self._age = new_age,
но только если new_age >= 0
(иначе выведите сообщение "Возраст не может быть отрицательным!"
и не меняйте значение).

Создайте объект p = Person(), вызовите p.set_age(25) (должно сработать),
затем p.set_age(-5) (должно вывести ошибку).
Выведите print(p.get_age()).
"""


class Person:
    def __init__(self, age=0):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age

        else:
            print('Ошибка')


p = Person()
p.set_age(25)

p.set_age(-5)
print(p.get_age())
