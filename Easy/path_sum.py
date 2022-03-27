"""
по сути эта задача решается только одним алгоритмом, это DFS
ее можно решть как рекурсивно, так и итеративно

ниже приведет рекурсивный метод
"""

def recursiveDFS(self, root, summ):
    path_summs = []

    if root is not None:
        summ += root.val

        if root.left is None and root.right is None:
            path_summs.append(summ)

        path_summs += self.recursiveDFS(root.left, summ)
        path_summs += self.recursiveDFS(root.right, summ)

    return path_summs

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    path_summs = self.recursiveDFS(root, 0)
    return targetSum in path_summs

"""
на многих интервью просят решить задачи итеративно))
поэтому вот итератиынфй способ который очень важно знать!!

а вот как решать итеративно я чет хз)))))))
"""

