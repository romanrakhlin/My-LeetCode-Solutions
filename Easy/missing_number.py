"""
the simplest way to find missing number
the idea is firsly count summ of elements from 0 to len(nums) + 1
and then count summ of all elemnts in nums
then return first - second
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        need = 0
        for i in range(0, len(nums) + 1):
            need += i
        
        summ = 0
        for i in nums:
            summ += i
        
        return need - summ