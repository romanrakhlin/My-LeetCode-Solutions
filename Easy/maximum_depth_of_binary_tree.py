"""
есть три решения
первое - рекурсивный DFS
второе - BFS
третее - итеративный DFS
в этом видосы обьяснение: https://www.youtube.com/watch?v=hTM3phVI6YQ
"""

"""
начнем с самого первого и легкого
стандартным методом рекурсивного DFS проходимся по дереву

и изначально текущая глубина (depth) равно 0
и если node равен None то возвращем этот 0 в ретёрне

а вот если текущий элемент не равен None, то
уже в depth прибалвляем 1, идем дальше,
рекурсивно запускаем все то же самое по левой и правой веткам
и сохраняем их внутрений depth
но нас итерисует только максиальный depth, поэтому берем только max из двоих
так в итоге с самого низу запишется самый максиальный и будет идти обратно вверх
и мы его выводим в результат
"""

def maxDepth(self, root: Optional[TreeNode]) -> int:
	depth = 0

	if root is not None:
		depth += 1
		left_depth = self.maxDepth(root.left)
		right_depth = self.maxDepth(root.right)
		depth += max(left_depth, right_depth)

	return depth

"""
второй способ

чисто алгоритм BFS. но его вариакция где мы проходимся внутренним
циклом по всем уровням. но сохранять нам ничего не нужно,
мы просто увеличиваем счетсик level на 1
и в конце его возвращаем
"""

def maxDepth(self, root: Optional[TreeNode]) -> int:
	if root is None:
		return 0

	queue = [root]
	level = 0

	while len(queue) != 0:
		for _ in range(len(queue)):
			node = queue.pop(0)

			if node.left is not None:
				queue.append(node.left)

			if node.right is not None:
				queue.append(node.right)

		level += 1

	 return level

"""
третий способ
нравится мне меньше всего!!
это по сути обычный iterative preorder DFS
но вместо хранения node, мы храним Tuple(этот node, его уровень)
"""

def maxDepth(self, root: Optional[TreeNode]) -> int:
	if root is None:
		return 0

	cur_node = (root, 1)
	stack = []
	max_depth = 0

	while len(stack) != 0 or cur_node[0] is not None:
		if cur_node[0] is not None:
			max_depth = max(max_depth, cur_node[1])
			stack.append(cur_node)
			cur_node = (cur_node[0].left, cur_node[1] + 1)
		else:
			cur_node = stack.pop()
			cur_node = (cur_node[0].right, cur_node[1] + 1)

	return max_depth

