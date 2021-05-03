# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима)

import random

m = 5
array = [random.randint(-100, 100) for item in range(2 * m + 1)]
print(f'Исходный массив: {array}')


median = 0

for i in range(len(array)):
    right = 0
    left = 0
    equal = 0

    for j in range(len(array)):
        if i == j:
            continue

        if array[j] < array[i]:
            left += 1
        elif array[j] > array[i]:
            right += 1
        elif array[j] == array[i]:
            equal += 1


    if abs(right - left) <= equal:
        median = i
        break

print(f'Медиана массива: {array[median]}')
