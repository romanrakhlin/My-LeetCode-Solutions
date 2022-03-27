# https://leetcode.com/problems/merge-two-sorted-lists/

"""
вот прям офигенный видос - https://www.youtube.com/watch?v=GfRQvf7MB3k&t=512s
в котором он наглядно обьясняет как перемещаются поинтеры и тд

ну если кратко то мы создаем dummy node и начинаем строить наш merged list из него
проверяем какой элемент меньше l1 или l2, меньший из них
ставим как next of dummy node, и двигаем поинетр меньшего вперед
рано или поздно мы в какомто из lists дойдем до конца (None)
в таком случае наш цикл остановится
и мы просто смотри какой из lists мы недопрошли, и его просто ставим
как next of dummy node и все 

COMPLEXITY ANALISISE

O(1) space
константная память тк мы вообше ничего не храним в памяти
только всего ОДНУ переменную и по сути просто перебираем ссылки linked lists

O(n + m) runtime
worst case это когда даны lists одинаковой длины и мы проходим полностью тот и тот
в таком случае, если длинна первого - n, а второго - m,
то всего мы сделаем n + m итераций
"""

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    current_node = result
        
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next
                
        current_node = current_node.next
    
    if list1 is not None:
        current_node.next = list1
    if list2 is not None:
        current_node.next = list2
        
    return result.next

