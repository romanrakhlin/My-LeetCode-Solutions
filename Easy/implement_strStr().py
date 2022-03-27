# https://leetcode.com/problems/implement-strstr/

"""
сначала разберем случаи которые алгоритм не сможет определеить сам 
самом начале делаем проверки является ли haystack пустым
и needle пустым тогда будем возвращать 0 а если haystack пустой
а needle нет то вернет -1 после этого пишем сам алгоритм
задаеи переменную с индексом и ставим ее на ноль
после этого нам нужно пройтиь по haystack столько раз сколько
всего в ней символов каждый раз мы делаем проверку начинается ли haystack
с needle если нет то убираем один элемент из начала haystack
и увеличивает index на 1 если же начинается то возвращаем текущий index
в противном случае вернем -1
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        elif len(haystack) == 0 and len(needle) != 0:
            return -1
        index = 0
        for i in range(len(haystack)):
            if haystack.startswith(needle) == False:
                haystack = haystack[1:]
                index += 1
            else:
                return index
        return -1