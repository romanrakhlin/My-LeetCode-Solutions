"""
у этого алгоритма вот такая вот асимптотика
O(1) space, O(n) runtime
O(1) по space тк в алфавите всего 26 букв
и разер hash_map никогда не превысит 26ти

алгоритм работает так:
1) первым делом прровераем одинаковый ли размер у s и t
если нет то сразу выведем False
2) проходимся по всем символам в строк t
и длбавляем в hash_map этот символ как ключ
а значением будет количесво появлений в строке t
3) теперь проходимся по всем символам в строке s
и проверяем если этот символ находится в hash_map
если да, то отнпимаем на 1 из количества появлений
суть в том что если мы отнимем так появление 
каждого симвоала по если это anogram то
по итогу у каждого сисвола должно остаься 0 в hash_map
так как символы из s и из t взаимно заместили друг друга
4) в конце проверяем остались ли нули у всех сиволов или не
и выводим True или False на основе этого
"""

def isAnagram(self, s: str, t: str) -> bool:
    hash_map = {}
     
    if len(t) != len(s):
        return False
        
    for letter in t:
        if letter in hash_map:
            hash_map[letter] += 1
        else:
            hash_map[letter] = 1
        
    print(hash_map)
        
    for letter in s:
        if letter in hash_map:
            hash_map[letter] -= 1
            
    print(hash_map)
        
    for letter in hash_map:
        if hash_map[letter] != 0:
            return False
        
    return True
        
        