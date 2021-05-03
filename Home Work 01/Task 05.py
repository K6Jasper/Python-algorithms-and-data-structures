# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

first = ord(input('1-я буква: '))
second = ord(input('2-я буква: '))
first = first - ord('a') + 1
second = second - ord('a') + 1
print(f'Номер первой буквы = {first}, второй = {second}')
print(f'Количество букв между ними: {abs(first - second) - 1}')
