"""
это мое решение
оно максимаааально простое!!
можешь посмореть в папке Сomputer Sceience
"""

def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is not None:
        return self._insert(root, val)
    else:
        return TreeNode(val)
    
def _insert(self, root, val):
    if val < root.val:
        if root.left is not None:
            self._insert(root.left, val)
        else:
            root.left = TreeNode(val)
    elif val > root.val:
        if root.right is not None:
            self._insert(root.right, val)
        else:
            root.right = TreeNode(val)
        
    return root