# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


import random

size = 10
array = [random.randint(0, 50) for item in range(size)]
print(f'Неотсортированный массив: {array}')


def sort_merge(array):

    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    sort_merge(left)
    sort_merge(right)

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


sort_merge(array)
print(f'Отсортированный массив: {array}')
