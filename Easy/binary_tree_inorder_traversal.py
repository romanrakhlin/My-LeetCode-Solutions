"""
итеративный способ
самый топовый!!!!
"""

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	visited = []
	stack = []
	cur_node = root
	while len(stack) != 0 or cur_node is not None:
		if cur_node is not None:
			stack.append(cur_node)
			cur_node = cur_node.left
		else:
			cur_node = stack.pop()
			visited.append(cur_node.val)
			cur_node = cur_node.right
	return visited

"""
и рекурсивный
"""

def recursive_dfs(self, cur_node: Optional[TreeNode], visited) -> List[int]:
	if cur_node is not None:
		self.recursive_dfs(cur_node.left, visited)
		visited.append(cur_node.val)
		self.recursive_dfs(cur_node.right, visited)
	return visited
            
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = self.recursive_dfs(root, [])
    return result

