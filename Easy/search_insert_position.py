# https://leetcode.com/problems/search-insert-position/

"""
тут прям в условии написано что желательно чтобы
алгоритм работал за O(log n) и это как раз прямой намек
на то что мы должны использовать binary search
пиздим код binary search из конспектов (надо уже выучить наконец Рома!!)
и вставляем его в наш алгоритм (я кстати предпочитаю именно
итеративную версию) НО у нас в условии прямым текстом написано
что если target нет в nums то нужно выдать индекс на котором бы
стоял target поэтому в самом начале делаем на это проверку
и если она прозодит то добавляем target в nums и сортируем nums.
"""

class Solution:  
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
            
        min = 0
        max = len(nums) - 1
        mid = 0
        
        while min <= max:
            mid = (min + max) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                max = mid - 1
            elif target > nums[mid]:
                min = mid + 1