"""
тут вообще поебать на эффекивность
эта задача проверяет знание наизуть работы работы алгоритма DFS
есть два типа этого алгоритма - итеративный и рекурсивный

снизу приведен итеативный способ (он больше ценится)
"""

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    cur_node = root
    visited = []
    stack = []
    while len(stack) != 0 or cur_node is not None:
        if cur_node is not None:
            visited.append(cur_node.val)
            stack.append(cur_node)
            cur_node = cur_node.left
        else:
            cur_node = stack.pop()
            cur_node = cur_node.right
    return visited

"""
а вот рекурсивный
как можно видеть, он гораздо легче
и итогда не подходит, на интервью все таки более круто юзать именно итеративный
"""

def recursive_dfs(self, cur_node: Optional[TreeNode], visited) -> List[int]:
    if cur_node is not None:
        visited.append(cur_node.val)
        self.recursive_dfs(cur_node.left, visited)
        self.recursive_dfs(cur_node.right, visited)
    return visited
    
def preorderTraversal(self, cur_node: Optional[TreeNode]) -> List[int]:
    result = self.recursive_dfs(cur_node, [])
    return result

