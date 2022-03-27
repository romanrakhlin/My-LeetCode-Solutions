# https://leetcode.com/problems/add-binary/

"""
пишем сначала метод для переаода из бинарки в int
и из int в бинарку и просто в основном методе делаем один 
return в котором все красиво складываем
и еще не забываем в метод перевода из int в бинарку
проверку на ввод 0 потому что так мы должны вернуть
бинарный 0
"""

class Solution:
    def from_binary_to_int(self, b):
        result = 0
        count = 0
        for i in b[::-1]:
            result += (2 ** count) * int(i)
            count += 1
        return result
        
    def from_int_to_binary(self, n):
        if n == 0:
            return "0"
        result = ""
        while n:
            result = str(n % 2) + result
            n //= 2
        return result
        
    def addBinary(self, a: str, b: str) -> str:
        return self.from_int_to_binary(self.from_binary_to_int(a) + self.from_binary_to_int(b))