"""
изначально ищем best кейсы и если их нет то уже приступаем к написанию решения
разделяем дерево на две части: left и right
и надо написать вспомагательную функцию которая будет проходиться по внутреннему дереву
и возвращать массив со всеми его нодами

можно было использовать например BFS, но я решим не заморачиваться
и сделать рекурсивный DFS. но он работает намного нестандартно
так как нам нужно проверять симметрию

первая нестандартная вещь это параметр reverse
он нужен для того чтобы когда мы проходились по левом поддереву
мы собирал массив нодом слева направа
а когда проходимся по правому поддереву
нам нужно собирать массив наоборот справа налева
это для проверки на симметрию

вторая нестандартная вещь это если текущий нод
по которому проходит DFS равен None то мы сохраняем "None"
это нужно для того если напримре вот такой кейс:
        1
      /   \
     2     2
    /      / 
   3      3
в таком случае наш алгоритм выдаст что дерево симметричное
ведь получившиеся массивы: [2, 3] и [2, 3]
но на самом деле это не так!!
но если мы будем сохранять None, то эта пробоема уйдем
[2, 3, None] != [2, None, 3]
"""

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    elif root.left is None and root.right is None:
        return True
        
    left_child = root.left
    right_child = root.right
        
    left_visited = self.recursiveDFS(left_child, False)
    right_visited = self.recursiveDFS(right_child, True)
        
    return left_visited == right_visited
        
def recursiveDFS(self, root, reverse):
    visited = []
        
    if root is not None:
        visited.append(root.val)
            
        if reverse: # right then lest
            visited += self.recursiveDFS(root.right, reverse)
            visited += self.recursiveDFS(root.left, reverse)
        else: # left then right
            visited += self.recursiveDFS(root.left, reverse)
            visited += self.recursiveDFS(root.right, reverse)
    else:
        visited.append("None") # add dummy node
            
    return visited

