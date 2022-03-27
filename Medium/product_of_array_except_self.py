"""
really common problems on interviews

there exists only three ways to solve it:
1) go though each element and find product of all element except it
by creating new arr without that specific element and then find it product
it will be two nested loops so O(n^2)
2) this approach really nice and easy to implement firstly we need
to find product of all elements in arr and then go though each element
and devide this product of all elements with each elements
you can try it on your own and see that it works
time complexity is O(n) but we use devision which is banned
3) third approach is really hard to think of and understand
so to underderstand it watch Nick Whites video!
in two words the idea is firstly go from left to right
and find product of elements behind curent element
and then do the same but from right to left
at the end when we will be have two arrays
we need to find products of their element index by index

below the code of the third approach
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # from left to right
        left = [1]
        product = 1
        for i in range(0, len(nums) -1):
            product *= nums[i]
            left.append(product)
        
        # from right to left
        right = [1]
        product = 1
        reverse = nums[::-1]
        for i in range(0, len(reverse) - 1):
            product *= reverse[i]
            right.append(product)
        right = right[::-1]
        
        print(left, right)
        
        # product of left and right
        result = []
        for i in range(0, len(nums)):
            result.append(left[i] * right[i])
        
        return result