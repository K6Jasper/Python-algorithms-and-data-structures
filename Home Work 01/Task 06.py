# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input('Введите порядковый номер буквы в латинском алфавите (от 1 до 26): '))
char = chr(n + 96)
print(f'Это буква: {char}')
