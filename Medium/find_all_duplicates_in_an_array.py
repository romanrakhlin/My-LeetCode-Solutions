"""
made completely by Nick White's video
so if u dont understand the concept what it!!

the clues is that given integers from 1 to n
so if we do -1 for each we get the list of indexed
and we need to traverswe through every element
to find index and check if its negative
if it is than there are exist duplicaste
that changed it to negative if its not negative
then make it
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                result.append(index + 1)
            nums[index] = - nums[index]
        return result