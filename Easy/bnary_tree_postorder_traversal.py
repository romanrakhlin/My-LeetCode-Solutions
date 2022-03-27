"""
итеративный способ
"""

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	visited = []
	stack = []
	cur_node = root
	while len(stack) != 0 or cur_node is not None:
		if cur_node is not None:
			visited = [cur_node.val] + visited
			stack.append(cur_node)
			cur_node = cur_node.right
		else:
			cur_node = stack.pop()
			cur_node = cur_node.left
	return visited

"""
рекурсивный способ
"""

def recursive_dfs(self, cur_node: Optional[TreeNode], visited) -> List[int]:
	if cur_node is not None:
		self.recursive_dfs(cur_node.left, visited)
		self.recursive_dfs(cur_node.right, visited)
		visited.append(cur_node.val)
	return visited

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
	result = self.recursive_dfs(root, [])
	return result

