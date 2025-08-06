from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        return self.is_sym_recurs(left_nd=root.left, right_nd=root.right)

    def is_sym_recurs(self, left_nd: Optional[TreeNode], right_nd: Optional[TreeNode]) -> bool:
        if left_nd is None and right_nd is None: return True
        # left_nd, right_nd - хотя бы одна вершина not None
        if left_nd is None or right_nd is None or left_nd.val != right_nd.val:
            return False
        # left_nd.val = right_nd.val
        return self.is_sym_recurs(left_nd=left_nd.left, right_nd=right_nd.right) and self.is_sym_recurs(left_nd=left_nd.right, right_nd=right_nd.left)