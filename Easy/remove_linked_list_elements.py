"""
самое элегантное решение !!

сначала было очень друдно его понять, но чем больше
работаешь в linked lists, чем все понятнее становится
как переставляются поинтеры и тд.

суть заключается в том что мы проходимся по всем нодам
и на каждой итерации смотрим - равен ли ноде, стоящий после текущего
тому значению которое нужно удалить?
если он равен, то делаем так - current_node.next = current_node.next.next
то есть (НЕ МЕНЯЯ POINTER TO THE CURRENT_NODE) изменяем 
ссылку на следующий нод у current_node
очень важно понять что сам current_node остается там где был
мы просто изменяем ССЫЛКУ

это мы делаем для того чтобы на следующей итерации уже проверить
новый next node. и так проверять next ноды пока next
не станет нормальным (устрпивающим нас) нодом
в таком случае запускается код в блоке else
где мы просто двигаем current_node вперед
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int):
    dummy_node = ListNode()
    dummy_node.next = head
    current_node = dummy_node

    while current_node.next is not None:
        if current_node.next.val == val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return dummy_node.next

def print_ll(cur_node):
    while cur_node is not None:
        print(cur_node.val)
        cur_node = cur_node.next

ll = ListNode(1, ListNode(6, ListNode(6, ListNode(2))))

print_ll(ll)
result = removeElements(ll, 6)
print()
print_ll(result)

"""
второе решение
асимтотика точно такая же, но более разжеванное решение

алгоритм тут такой:
1) создаем dummy_node он будет стоять перед head
это нужно для того чтобы, елси вдруг значение которое нужно 
удалить, стоит на head, то мы могли бы его удалить
2) делаем цикл пока текущий node не будет равен None
или следующий node не будет рпвен None

делаем проверку если следующий node равен значению которое
нужно удалить, тогда создаем внутреннюю переменную и ставим ее
на этот текущий node. начинаем идти от этой внутренней переменной до 
того момента пока не дойдем до того node, который уже удалять не надо
ТО ЕСТЬ цикл остановися КОГДА внутренняя переменная будет стоять на
последнем node который имеет значение которые нужно удалить

и нам как раз нужно из текущего node сразу скипнуть все значения 
то есть направляем current_node.next = inner_node.next
тем самым пропускем все значения для удаления
ну и понятное дело идем дальше
"""

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy_node = ListNode()
    dummy_node.next = head
    current_node = dummy_node
        
    while current_node is not None and current_node.next is not None:
        if current_node.next.val == val:
            inner_node = current_node
            while inner_node.next is not None and inner_node.next.val == val:
                inner_node = inner_node.next
            current_node.next = inner_node.next
        current_node = current_node.next
        
    return dummy_node.next

