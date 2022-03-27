"""
This problem is really weird but ok
We gonna use https://en.wikipedia.org/wiki/H-index
in section called Calculation all information we need
more info - https://www.youtube.com/watch?v=RYSkjEIovsw

The idea is to go through the array and find
the element on which it's index became greated that or equal to
the it's value. When we find this situation this means that
the previous one was the last one that where index were smaller than
the value and thats what we need. And we have to return the length
and because all eleemnts in array starts with 0 we simply
return current index as length

This solutions works in O(n logn) by time and O(1) by space
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        
        for i, v in enumerate(citations):
            if i >= v:
                return i
        
        return len(citations)

"""
But leetcode leaves us a hint that a faster approach is to use extra space.
So we ganna implement it this way later right now Im so fucking tired
"""

        