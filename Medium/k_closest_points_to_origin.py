"""
I read discussion and found out that most efficient solution
are that uses some fucking heaps !
And I not tha smart so thats my solution using tuples and sort
# O(nlogn) - runtime; O(n) - space
"""

import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = [] # O(n)
        
        # collect all distances and points attached with them
        # O(n)
        for point in points:
            distance = math.sqrt( ((0 - point[0]) ** 2) + ((0 - point[1]) ** 2) )
            results.append((distance, point))
            
        # sort array of tuples by distance
        # O(nlogn)
        results.sort(key=lambda x:x[0])
        
        # collect only k first elements in results
        # O(n)
        final = [] # O(n)
        for i in range(k):
            final.append(results[i][1])
        
        # O(nlogn) - runtime; O(n) - space
        return final