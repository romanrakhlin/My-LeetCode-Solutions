"""
мое решение которое рабоатет за
O(1) space, O(n) runtime

мой алгоритм:
1) проходимся по всем буквам в строке и добавляем ее в hash_map где
key - сама буква
value - Tuple(индекс буквы в строке, количество появлений в строке)
по итогу получаем заполненный hash_map
2) проходимя по этому hash_map и смотрим если
у данной буквы количество появлений в строке (Tuple.1) равно 1
то тогда позвращаем индекс этой буквы в строке (Tuple.0)

решение работает именно за O(1) space
тк всего в алфавите 26 букв и размер hash_map никогда не превысит 26
то есть, у hash_map етсь upper bound и space - constant
"""
def firstUniqChar(self, s: str) -> int:
    hash_map = {}
        
    for index in range(0, len(s)):
        letter = s[index]
        if letter in hash_map:
            hash_map[letter] = (hash_map[letter][0], hash_map[letter][1] + 1)
        else:
            hash_map[letter] = (index, 1)
        
    for letter in hash_map:
        if hash_map[letter][1] == 1:
            return hash_map[letter][0]
        
    return -1