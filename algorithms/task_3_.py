"""
Задача о нахождении наиболее часто встречающегося элемента
в списке. Дан список целых чисел,
найдите элемент, который встречается в нем наиболее часто.
"""


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def frequent_element(sorted_list):
    if not sorted_list:
        return None
    max_count = 1
    current_count = 1
    most_common = sorted_list[0]

    for i in range(1, len(sorted_list)):
        if sorted_list[i] == sorted_list[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                most_common = sorted_list[i - 1]
            current_count = 1

    if current_count > max_count:
        most_common = sorted_list[-1]
    return most_common


lst_1 = [10, 5, 4, 3, 87]
sorted_list = quick_sort(lst_1)
print(f'Отсортированный список: {sorted_list}')
print(f'Наиболее встречающийся элемент в списке: {frequent_element(sorted_list)}')

