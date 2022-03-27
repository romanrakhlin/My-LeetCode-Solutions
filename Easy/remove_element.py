"""
O(n^2) runtime O(1) space
my solution not eficient
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
        	nums.remove(val)

"""
O(n) runtime O(1) space
my solution not eficient
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k += 1
        return k