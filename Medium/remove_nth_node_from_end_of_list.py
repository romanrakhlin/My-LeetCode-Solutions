"""
алгоритм состоит из трех этапов и на первых двух 
мы делаем проверки для исключения неверных случаев
(если бы не эти ебаные тест кейсы нереальные от литкода
то этих проверок бы не было)

1) пишем отдельную функцию для поиска длинны линкд листа
потом юзая ее задаем в переменную
если длинна равно 1 то просто возвращаем пустой линкд лист

2) находим индекс элемента который нужно удалить
просто из всей длинны вычия данный элемент с конца по счету (n)
если нужно удалить самый первый элемент то тупа возвращем
линкд лист без первого элемента

3) просто уже известный метод по удалению элемента
по заданному индексу тупа находим его потом удаляем и делаем брейк
после этого возвращаем получившийся линкд лист
"""

class Solution:
    def find_len(self, head):
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1
        len_of_ll = self.find_len(head)
        if len_of_ll == 1:
            return None
        
        # 2
        del_index = len_of_ll - n
        if del_index == 0:
            return head.next
        
        # 3
        cur_node = head
        cur_index = 0
        
        while cur_node.next is not None:
            if cur_index + 1 == del_index:
                if cur_node.next.next is not None:
                    cur_node.next = cur_node.next.next
                else:
                    cur_node.next = None
                break
            cur_node = cur_node.next
            cur_index += 1
    
        return head