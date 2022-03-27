"""
the solution using Sets
if we gonna analyze the profram line by line
1 - O(n) space, O(n) runtime
2 - O(n) runtime, O(n) runtime => 2*O(n) runtime
Therefore: 2*O(n) runtime, O(n) space
"""
def containsDuplicate(self, nums: List[int]) -> bool:
    nums_set = set(nums)
    if len(nums_set) == len(nums):
        return False
    return True

def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

"""
this is the solution using Hash Maps
lets analize:
1 - O(n) space
2 - O(n) runtime
3 - O(1) runtime
So: O(n) runtime, O(n) space
A little bit quicker!
"""
def containsDuplicate(self, nums: List[int]) -> bool:
    hash_map = {}
    for i in nums:
        if i in hash_map:
            return True
        hash_map[i] = 9999
    return False