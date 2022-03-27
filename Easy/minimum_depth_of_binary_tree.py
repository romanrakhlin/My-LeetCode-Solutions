"""
эта задача очень похоже на ее прородителя - Maximum Depth of Binary Tree
тут самый навороченный способ это рекурсивный DFS (также как решение в прородителе)
но прикол в том что если мы его запрогаем, но вместо max, будет получать min
и запустим, все будет работать!!
но вот если отправим на Submission, то выскочит ошибочка!
все дело в том что есть один кейс при котором этот алгоритм ошибается

если у нас вот такое дерево:
1
 \
  2
   \
    3
     \
      4
то есть только одна ветка, либо такая же ветка, направленная влево, не суть
вот на таких кейсах алгоритм дает неправмльные ответы.
он бует выдавать минималку -> 1, он будет думать что самый
первый node имеет самую короткую длину. если написать проверку чтобы 
не считать вообще первый root node в результате, то алгоритм выдаст 2 и так далее
надо хэндлить ошибку немного иначе, нужно сделать вот такую проверку
if left_depth == 0 or right_depth == 0:
    depth += max(left_depth, right_depth)
else:
    depth += min(left_depth, right_depth)
то есть если хоть один из children является None, то тогда мы берем максималку а не минималку
"""

def minDepth(self, root: Optional[TreeNode]) -> int:
    depth = 0

    if root is not None:
        depth += 1

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        if left_depth == 0 or right_depth == 0:
            depth += max(left_depth, right_depth)
        else:
            depth += min(left_depth, right_depth)

    return depth