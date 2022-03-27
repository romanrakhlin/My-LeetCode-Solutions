# O(n) runtime AND O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        results = {}
        for i in nums:
            if i in results:
                results[i] = results[i] + 1
            else:
                results[i] = 1
        print(results)
        max_key = 0
        result = 0
        for i in results.keys():
            if results[i] > max_key:
                max_key = results[i]
                result = i
        return result

"""
Nice explanations here https://www.youtube.com/watch?v=M1IL4hz0QrE
So the idea is set FAVORITE element and COUNTER = 1
When we travering the nums array and see the same as FAVORITE element we increase counter by one
See different dicrease it by one 
If counter it 0 then we no longer need to track current FAVORITE
so state current element as new FAVORITE and so the same things again
The idea is if element appears more theb half of given array then 
after traversing and increasing and decresing counter it gonna still as FAVORITE
so return FAVORITE at the end
"""

# O(n) runitine O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        favorit = nums[0]
        counter = 0
        for i in nums:
            if counter == 0:
                favorit = i
                
            if favorit == i:
                counter += 1
            else:
                counter -= 1
        return favorit