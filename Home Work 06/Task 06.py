# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
#   - выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
#   - написать 3 варианта кода (один у вас уже есть);
#   - проанализировать 3 варианта и выбрать оптимальный;
#   - результаты анализа (количество занятой памяти в вашей среде разработки)
#     вставить в виде комментариев в файл с кодом.
#   - Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;


# Для решения было взято задние № 6 из урока № 1.
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# OS: Windows 10 64-bit
# IDE: PyCharm 2020.3.2 (Community Edition) Build #PC-203.6682.179, Runtime version: 11.0.9.1+11-b1145.63 amd64


from sys import getsizeof


def show_size(x, level=0):
    result_size = getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result_size += show_size(key, level + 1)
                result_size += show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                result_size += show_size(item, level + 1)
    return result_size


def local_var_size(local_var):
    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
        size_of_all_variables += show_size(local_variables_dict[var])
    print(f'Список переменных: {local_variables_dict}')
    return print(f'Размер выделенной памяти: {size_of_all_variables} байт')


# Функция поиска буквы по ее номеру в кодировке.
def find_char1(n):
    local_variables_dict = locals().copy()
    local_var_size(local_variables_dict)
    if (n + 96) < 97 or (n + 96) > 122:
        return 'Ошибка. Введите номер от 1 до 26'
    else:
        return print("Вашему номеру соответствует буква:", chr(n + 96).upper())


print(find_char1(26))
print('*' * 100)


# Функция поиска буквы по номеру из алфавита, строкой.
def find_char2(n):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    local_variables_dict = locals().copy()
    local_var_size(local_variables_dict)
    if n <= 0 or n > len(abc):
        return 'Ошибка. Введите номер от 1 до 26'
    else:
        return print("Вашему номеру соответствует буква:", abc[n - 1].upper())


print(find_char2(26))
print('*' * 100)


# Функция поиска буквы по номеру из алфавита, по списку.
def find_char3(n):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    local_variables_dict = locals().copy()
    local_var_size(local_variables_dict)
    return print("Вашему номеру соответствует буква:", abc[n - 1].upper())


print(find_char3(26))

# Функция 1 занимает 310 байта.
# Функция 2 занимает 437 байт.
# Функция 3 занимает 1942 байта.
# Наименьшее выделение памяти было при использовании функции поиска буквы по её номеру в кодировке.
