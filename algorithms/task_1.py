"""
Задача о поиске общих элементов в двух списках. Даны два списка целых чисел, найдите все элементы, которые встречаются
и в первом, и во втором списке.
"""
from msvcrt import kbhit

list1 = [22, 16, 1, 45, 78, 12]
list2 = [15, 17, 18, 19, 22, 16]

elements = list(set(list1) & set(list2))
print(elements)

elements = [x for x in list1 if x in list2]
print(elements)


for x in list1:
    if x in list2:
        print(x)


