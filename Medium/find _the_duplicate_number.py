"""
this problem is really hard cause we need O(1) by space and O(n) by runtime
and this is really hard cause we cant store any array and do only one loop!

the difficuulty that we need to understand that its a linked list problem
and can be solved only by using Floyd's algorithm

the Floyd's algorithms can only be used with linked lists
BUT if we somehow represent our array as a linked list...
lets think that only indexes (of array) are values (of linked list)
and values (of array) are nex pointers (of linked list)

for example we have input array:
[1, 3, 4, 2, 2]
 0  1  2  3  4 (indexes)
 
 and linked list representation will be:
 
 0 -> 1 -> 3 -> 2 -> 4
                |    |
                ------
                
after that we need to implement our Floyd's algorithm
but I wont spend time on this i recordered really nice video
about it so u can find it in phone!

the full solution below:
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        begin = 0
        while True:
            begin = nums[begin]
            slow = nums[slow]
            
            if begin == slow:
                return slow

"""
another really simple approach is using Nick White's method
but for another problem 442 but I guess they are simmilar
and this one easier actually
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                return index + 1
            nums[index] = -nums[index]