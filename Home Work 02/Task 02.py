# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Введите натуральное число: ')
even_count = 0
odd_count = 0

for num in number:
    if int(num) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f'В числе {number} - {odd_count} нечетных  и {even_count} четных циры')
