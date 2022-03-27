"""
решаем по аналогии с оригинальной задачей
Я реаилзовал простой In-Order DFS, каждую итерацию
проверяем если элемент уже словаре been
если да, то выводим True, если нет то просто добавляем его туда

причина по который Я использую именно словарь - это память
мог бы юзат массив и писать if x in arr, но эта операция будет работать за O(n)
а так Я юзаю словарь и просто сохраняю k - val за ключ, а value любое, например 9999999

Time Complexity:
Space: O(n)
Time: O(n)
"""

def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    been = {}
        
    cur_node = root
    stack = []
        
    while len(stack) != 0 or cur_node is not None:
        if cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left
        else:
            cur_node = stack.pop()
                
            if cur_node.val in been:
                return True
            been[k - cur_node.val] = 9999999
                
            cur_node = cur_node.right
        
    return False