"""
Задача о сортировке студентов по среднему баллу.
Дан список студентов с их оценками,
требуется отсортировать их по убыванию среднего балла.
"""
from operator import itemgetter

students = [
    {'name': 'Петров', 'grades': [4, 5, 4, 5, 4, 4]},
    {'name': 'Иванов', 'grades': [5, 5, 5, 4, 5, 4]},
    {'name': 'Сидоров', 'grades': [4, 4, 4, 3, 4, 4]},
    {'name': 'Машкина', 'grades': [4, 3, 4, 5, 4, 4]}]
for student in students:
    student['average'] = round(sum(student['grades']) /
                               len(student['grades']), 2)

students_sorted = sorted(students,
key=itemgetter("average"), reverse=True)
for student in students_sorted:
    print(f'{student['name']}: {student['average']}')
