"""
Спроектировать и создать класс Person
"""
class Person:

    school = 'гимназия №1'
    def __init__(self, post, subject, name, age):
        self.post = post
        self.subject = subject
        self.name = name
        self.age = age
    def work_hard(self):


        print(Person.school)
        print(f'Должность сотрудника {self.post}, преподает предмет {self.subject}, '
              f' его имя {self.name}, его возраст {self.age}')
person_1 = Person('учитель', 'химия', 'Мария Ивановна', '45')
person_1.work_hard()