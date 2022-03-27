"""
концепт для решения точно такой же как и в задаче 203
там более детально описал алгоритм и привел два решения!!

ну кароче тут обрабатываем самый первый node подходом dummy node
проходимся по всем нодам переставляем next у each node 
пока не пропустим все дубликаты и так до конца
"""

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy_node = ListNode(9999999999)
    dummy_node.next = head
    current_node = dummy_node
        
    while current_node.next is not None:
        if current_node.next.val == current_node.val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
        
    return dummy_node.next

