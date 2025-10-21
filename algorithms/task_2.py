"""
Задача о нахождении k-го наименьшего элемента в неотсортированном списке.
 Дан неотсортированный список целых чисел и число k.
 Найдите k-ый наименьший элемент в этом списке.
"""


# def partition(nums, low, high):
#     pivot = nums[(low + high) // 2]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1
#
#         j -= 1
#         while nums[j] > pivot:
#             j -= 1
#
#         if i >= j:
#             return j
#
#         nums[i], nums[j] = nums[j], nums[i]
#
#
# def quickselect(nums, low, high, k):
#     if low == high:
#         return nums[low]
#     pivot_index = partition(nums, low, high)
#     if k <= pivot_index:
#         return quickselect(nums, low, pivot_index, k)
#     else:
#         return quickselect(nums, pivot_index + 1, high, k)
#
#
# def kth_smallest(nums, k):
#     if k < 1 or k > len(nums):
#         return None
#     return quickselect(nums, 0, len(nums) - 1, k - 1)
#
#
# list_1 = [22, 45, 12, 1, 55, 78, 96, 63]
# print(kth_smallest(list_1))


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

def find_kth_smallest_index(arr, k):
    # Найдём значение k-го по величине числа (k-1 — индекс в 0-индексации)
    value = quickselect(arr.copy(), 0, len(arr)-1, k-1)
    # Найдём индекс первого вхождения этого значения в исходном массиве
    return arr.index(value)

# Пример
arr = [7, 10, 4, 3, 20, 15]
k = 3
index = find_kth_smallest_index(arr, k)
print(index)  # Выведет индекс элемента, который является 3-м по возрастанию
