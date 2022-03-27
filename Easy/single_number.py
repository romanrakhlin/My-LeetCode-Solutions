"""
this is fuckin bit manipulation problem
and I know how to solve it in O(n^2) runtime + O(1) space
and O(n) runtime + O(n) space but boooooth O(n) runtime + O(1) space
its impossible for me and fuck bit manipulation!
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i