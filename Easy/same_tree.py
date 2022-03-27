# https://leetcode.com/problems/same-tree/

"""
довольная простенькая проблема для ее решения я написал
preorder dfs и думал но все работало но суть в том что может быть
такое когда дано одно дерево только с левым ребеноком и дерево только с
правым и алгоритм говорил что они одинаковые хотя это не так
поэтому я добавил блок else чтобы когда текущий node был навер None
мы добавляли бы в массив None и именно в таком случае ошибки описанной
выше бы не возникает все отлично работает за O(n) где n 
это количество node в заданном binary tree
"""

class Solution:
    def preorder_dfs(self, root, result):
        if root is not None:
            result.append(root.val)
            self.preorder_dfs(root.left, result)
            self.preorder_dfs(root.right, result)
        else:
            result.append(None)
        return result
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        one = self.preorder_dfs(p, []) 
        two = self.preorder_dfs(q, [])
        print(one, two)
        return one == two