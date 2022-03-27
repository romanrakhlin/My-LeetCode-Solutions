"""
(In hint said to use two pointers but I solved it my way)
The idea is to iterate from the end of given string and

when we see # we increase counter
when we see a letter then we check
2.1) if counter equal to 0 it means that we passed all elements
we need to remove and simply append current leeter to the result
2.2) but if counter not zero it means we have to erase it so decrese counter by one
at the end the result string have only symbols we didnt removed
but in reversed order and it doesnt matter cause we only need to ckeck equality
so simply check equality and return it
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.recreate(s) == self.recreate(t)
    
    def recreate(self, s):
        result = ""
        count = 0
        for i in s[::-1]:
            if i == "#":
                count += 1
            else:
                if count == 0:
                    result += i
                else:
                    count -= 1
        return result