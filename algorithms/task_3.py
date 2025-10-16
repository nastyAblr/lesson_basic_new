"""
Задача о нахождении наиболее часто встречающегося элемента в списке.
Дан список целых чисел, найдите элемент,
который встречается в нем наиболее часто.
"""


def majority_element(nums):
    element = None
    count = 0

    for num in nums:
        if count == 0:
            element = num
            count = 1
        elif num == element:
            count += 1
        else:
            count -= 1

    if nums.count(element) > len(nums) // 2:
        return element
    else:
        return None


list_2 = [2, 2, 1, 3, 3, 1, 1, 1, 1, 1, 2]
print(majority_element(list_2))
