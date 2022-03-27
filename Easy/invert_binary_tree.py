"""
есть два способа, правда второй ценится выше на интервью
первый способ маааксимально простой и понятный
это рекурсивный DFS, где мы просто на каждой итерации либо preorder, 
либо postorder, меняем детей местами, вот и все
"""
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is not None:
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
    return root

"""
вот этот способ просто пушка!! первым делом понятное дело сразу выводим ответы в best cases
главное по памяти знать BFS алгоритм!
по сути эти самая стандартная вариация этого алгоритма, мы просто на каждой итерации,
где мы из queue берем первый в очереди node и исключаем его и очередли, меняем местами его детей
и далее проверяем его детей на None и добавляем в очередь!!
"""
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    elif root.left is None and root.right is None:
        return root
        
    queue = deque([root])
        
    while len(queue) != 0:
        node = queue.popleft()
        node.right, node.left = node.left, node.right

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
                
    return root

