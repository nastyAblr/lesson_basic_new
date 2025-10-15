"""
Создайте класс Student с приватным атрибутом __name и
публичным методом get_name(), который возвращает имя студента.
Создайте класс Course, который имеет приватный атрибут __students
и методы add_student(student) и remove_student(student),
которые добавляют и удаляют студента из курса.
Затем создайте объекты этих классов и добавьте несколько студентов
в курс.
"""


class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Course:
    def __init__(self):
        self.__students = []

    def add_student(self, student):
        if student not in self.__students:
            self.__students.append(student)
        else:
            print('Студент уже записан на курс')

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
        else:
            print('Студент не найден в списке')

    def list_students(self):
        if not self.__students:
            print('Студентов пока нет')
        else:
            print('Студенты на курсе:')
            for student in self.__students:
                print(student.get_name())


student1 = Student('Иванов Иван')
student2 = Student('Петрова Мария')
student3 = Student('Сидоров Сидр')

course = Course()
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

course.list_students()

course.add_student(student1)
course.remove_student(student2)

course.list_students()
