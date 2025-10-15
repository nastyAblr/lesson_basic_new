"""
Создайте систему управления задачами в проекте.
Можно создать абстрактный класс Task,
который определяет общий интерфейс для всех задач,
и классы Bug, Feature и Improvement,
которые наследуются от Task и предоставляют конкретную реализацию
для каждого типа задач. Кроме того, можно создать абстрактный класс Project,
который определяет общий интерфейс для всех проектов,
и классы Product, Service и Internal, которые наследуются от Project
и предоставляют конкретную реализацию для каждого типа проектов.
"""
from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.status = 'Открыто'

    @abstractmethod
    def execute(self):  # метод для выполнения задачи
        pass

    @abstractmethod
    def details(self):  # метод возвращает описание задачи
        pass

    def __str__(self):
        return f'[{self.id}] {self.title} - {self.description}'


class Bug(Task):
    def __init__(self, id, title, description, severity):
        super().__init__(id, title, description)
        self.severity = severity

    def execute(self):
        self.status = 'Исправлено'
        print(f'Bug: {self.id} исправлен.')

    def details(self):
        return (f'Bug: {self.title}\nSeverity: {self.severity}\nDescription:'
                f'{self.description}\nStatus: {self.status}')


class Feature(Task):
    def __init__(self, id, title, description, priority):
        super().__init__(id, title, description)
        self.priority = priority

    def execute(self):
            self.status = 'Реализовано'
            print(f'Feature {self.id} реализована. ')


    def details(self):
        return (f'Bug: {self.title}\nPriority: {self.priority}\nDescription:'
                    f'{self.description}\nStatus: {self.status}')


class Improvement(Task):
    def __init__(self, id, title, description, area):
        super().__init__(id, title, description)
        self.area = area

    def execute(self):
        self.status = 'Улучшено'
        print(f'Improvtmtnt: {self.id} внедрено.')

    def details(self):
        return (f'Bug: {self.title}\nArea: {self.area}\nDescription:'
                    f'{self.description}\nStatus: {self.status}')

if __name__ == '__main__':
    tasks = [
        Bug(1, "Исправить ошибку входа", "Проблема с аутентификацией пользователей", "High"),
        Feature(2, "Добавить экспорт данных", "Возможность выгружать отчёты в XLS", "Medium"),
        Improvement(3, "Оптимизировать загрузку", "Ускорить загрузку страниц", "Performance")
    ]

    for task in tasks:
        print(task.details())
        task.execute()
        print(task)  # вывод статуса после выполнения
        print()
