# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import randint

n = 20
a = [randint(-100, 100) for _ in range(n)]
i = 0
item = -1

for i in range(len(a)):
    if a[i] < 0 and (a[i] > a[item] or item == -1):
        item = i
    i += 1

print(f'Массив: {a}')

if item == -1:
    print('В массиве нет отрицательных элементов')
else:
    print(f'Максимальный отрицательный элемент: {a[item]}, его позиция в массиве: {item + 1}')
