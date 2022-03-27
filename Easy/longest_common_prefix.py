# https://leetcode.com/problems/longest-common-prefix/

# Основан на принципе Nick White
# https://www.youtube.com/channel/UC1fLEeYICmo3O9cUsqIi7HA

# Мы представляем что прификс это самые первый str.
# Потом запускаем цикл со второго str по последний.
# Продставляем префикс в первый str и если наш str не начинается с префикса
# то мы уменьшаяем префикс на 1 символ. И так пока str не будет с него начинаться.
# После работы с первым str у нас получится префикс подзодящий для первго str.
# Теперь идем с следующему str и делаем все то же самое.
# В итоге у нас должен получиться префикс, подходящий всем str в массиве.
# Его мы и выведем.
def find(strs):
    strs.sort()

    if len(strs) == 0:
        return ""

    prefix = strs[0]

    for i in range(1, len(strs)):
        while prefix not in strs[i]:
            prefix = prefix[:len(prefix) - 1]

    return prefix

arr = ["flower","flow","flight"]
print(find(arr))

