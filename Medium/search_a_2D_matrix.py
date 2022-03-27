"""
тут другого решения кроме birary search вообще нет!!
можно конечно решить по памяти плохо, сначала сохранив 
матрицу в массив и пройдясь по ней binary search
а можно догадаться проходить по всем row в матрице
и отдельно по каждой юзать birary search

в данном примере решнеие 
O(n) runtime если в общем рассматривать
так как количетсво итераций в основном цилке
напрямую зависит от количетсва rows в заданной matrix
но а так внутри еще рабоатает O(log n)
также мы вообще ничего не храним, так что константная память

поэтому можно скзаать так:
O(1) space, O(n) + O(log n) runtime
"""

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        # binary search on row
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target < row[mid]:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else: # row[mid] == target
                return True

    return False