"""
Спроектировать и создать класс Animal
"""
class Animal:
    type_animal = 'кот'
    def __init__(self, breed, color, age):
        self.breed = breed
        self.color = color
        self.age = age

    def eats_food(self, food):
        print(f'Это животное относится к виду {Animal.type_animal}, '
              f'порода {self.breed}, окрас {self.color}, возраст {self.age}, '
              f'питается \"{food}\" ')

animal_1 = Animal('Сиамский', 'бежевый', '4')
animal_1.eats_food('Китекет')