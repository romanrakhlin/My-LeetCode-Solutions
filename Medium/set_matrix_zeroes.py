"""
this solution works O(m * n) runtime and O(1) space
cause we edit this matrix IN-PLACE and dont store
absolutely anything besinds first_row_has_zero
this var

dont look on rows and cols var indeed they are
depends on the len of the matrix BUT they are helpers
for interations through matrix and dont count in space efficiency

u can watch this video - https://www.youtube.com/watch?v=T41rL0L3Pnw
he shows all three possible solutions all with the same
runtime complexity and with differend space complexity
HERE we gonna use last and most efficient approach
"""

# O(m + n) space solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        vertical = [1] * len(matrix)
        horizontal = [1] * len(matrix[0])
        
        for m in range(0, rows):
            for n in range(0, cols):
                if matrix[m][n] == 0:
                    vertical[m] = 0
                    horizontal[n] = 0
        
        for m in range(0, rows):
            for n in range(0, cols):
                if vertical[m] == 0:
                    matrix[m][n] = 0
                elif horizontal[n] == 0:
                    matrix[m][n] = 0
        
        return matrix

"""
O(1) space solution
THE BEST !!!!
BREATHLY:
the idea is to iterate though matrix starting from
second row to the last cause we dont need to iterate thought
the first row we gonna use it as helper arr at the end
and first collumn we are using also as a helper
if cur element of a matrix is 0 then we are setting the most
top element to 0 and most left elem to 0 too

after that we have to go though the matrix again
but at this time go though each row backwords
FROM RIGHT TO LEFT and check if most top OR most left elem
from it is 0 then set current element to 0

thats all before returning the matrix we see that we didnt edit
FIRST ROW at all!! thats why we have to check if first row
has 0 in it if its True then set whole row to 0

finally return matrix
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        first_row_has_zero = 0 in matrix[0]
        
        for m in range(1, rows):
            for n in range(0, cols):
                if matrix[m][n] == 0:
                    matrix[m][0] = 0
                    matrix[0][n] = 0
        
        for m in range(1, rows):
            for n in range(cols - 1, -1, -1):
                if matrix[m][0] == 0 or matrix[0][n] == 0:
                    matrix[m][n] = 0
        
        if first_row_has_zero:
            matrix[0] = [0] * cols
        
        return matrix