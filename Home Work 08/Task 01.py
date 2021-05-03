# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.


from hashlib import sha1

s = input('Введите строку: ')


def func(s):
    len_ = len(s)
    hash_set = set()
    for i in range(len_):
        for j in range(i, len_+1):
            if s[i:j] and s[i:j] != s:
                hash_set.add(sha1(s[i:j].encode('utf-8')).hexdigest())

    return len(hash_set)


print(f'Количество подстрок: {func(s)}')
