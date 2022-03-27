"""
вот мое решение к данной проблеме
просто итеративное решение
максиальное простое и рабочее !!
"""

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root is not None:
        if val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
        else: # equal
            return root
            
    return None

"""
а вот еще на всякий итеративный способ
чисто для галочки))
"""
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return None
    elif root.val == val:
        return root
        
    if val < root.val:
        return self.searchBST(root.left, val)
    elif val > root.val:
        return self.searchBST(root.right, val)

        