"""
The first solution is really trivial
Time complexity - O(n logn)
Space complexity - O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in nums: # O(n)
            new_nums.append(i**2)
        new_nums.sort() # O(n logn)
        return new_nums

"""
We gonna try to implement O(n) by runtime solution
Took from this video - https://www.youtube.com/watch?v=4eWKHLSRHPY
Firstly we have to understand that input array's numbers from the left
and from the right sides are arrowed to the center.
[-4,-1,0,3,10]
------> <-----
What we can do is:
1) Create array filled with 0s contatins the same amount
of elements as input cause the task is to return modified input
2) The solution gonna be using TWO POINTERS APPROACH
Setting one pointer at the most left element and another of the most right element
3) We gonna itarate ginven array from right to left and fill it up
from right to left because as we already know the largest elements are
at the sides they are reaching the middle. As we start with sides we gonna look at
most big elements and fill out result array from rihgt to left too
4) Inside iteration of given array. If left element (as positive number) is bigger
than right. Append this element to result array at current index (from right to left).
Then move the left pointer closer to center.
5) The same with right element bigget than left.
6) At the end on the iteration simply return the result array
How that happens that we stop iteratin when we are done???
Because we check whether left or right is bigger and every time complete ONE element
so at the end all elemtns are gonna be checked. I know another approach where we make 
while loop and while pointeers meet then we stop. But I think that this solution is much better!!

Time complexity - O(n)
Space complexity - O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > nums[right]:
                result[i] = abs(nums[left]) ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result