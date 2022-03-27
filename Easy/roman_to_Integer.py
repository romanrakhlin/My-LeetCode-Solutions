# https://leetcode.com/problems/roman-to-integer

# Этот алгоритм я нашел на каком-то сайте.
# Суть в том что мы не пишем никакие массивы и функции для перевода строки
# в массив с цифрами. Вместо этого мы пишем словарь и работаем с ним.
# Просто так код занимает меньше места.
# Алгорим будет простым. Делаем цикл по всем индексам заданной строки s.
# Если индекс не равен первому и текущее число (в int) больше предыдущего числа
# то есть это когда например IX, то мы из текущего числа, в нашем примере 10,
# вычитаем 2 * 1. Получившееся число (8) прибавляем в результату.
# Можете на личточке или так в голове у себя протетировать и убедиться что все работает.
def romanToInt(s):
    # Словарь для перевода строк в цифры.
    roman_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # В итоге и будет наш результат.
    int_value = 0

    # Цикл по всем элементам строки.
    for i in range(len(s)):
        if i > 0 and roman_value[s[i]] > roman_value[s[i - 1]]:
            int_value += roman_value[s[i]] - 2 * roman_value[s[i - 1]]
        else:
            int_value += roman_value[s[i]]

    # Возвращаем результат.
    return int_value

# Тетстыыыыыы
print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("XIX"))