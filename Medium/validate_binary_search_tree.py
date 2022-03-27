"""
к этому решению пришел полностью сам!!
изначально пробовал BFS и както его модифицировать
но потом меня осенило как-то собирать массив из
данного Binary Search Tree и проверять отсортирован ли он!

нужен был алгоритм который проходит дерево
и собирает его nodes в таком нужном порядке
для этого я выбрал In-Order DFS
проходимся и собираем в массив

после этого нужно проверить то что массив отсортирован по возрастанию
это просто цикл с проверкой следующего элемента

Time Complexity
Space: O(n)
Time: O(n)
"""

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    nodes = []
        
    # inorder DFS
    cur_node = root
    stack = []
        
    while len(stack) != 0 or cur_node is not None:
        if cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left
        else:
            cur_node = stack.pop()
            nodes.append(cur_node.val)
            cur_node = cur_node.right
        
    # validate array
    for i in range(0, len(nodes) - 1):
        if nodes[i] >= nodes[i + 1]:
            return False
        
    return True