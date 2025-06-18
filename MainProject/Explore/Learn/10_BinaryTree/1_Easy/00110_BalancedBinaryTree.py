# 110 (Easy) Balanced Binary Tree
"""
Given a binary tree, determine if it is height-balanced.
"""

from typing import Optional

# Runtime = 2 ms  Beats 71.66%  ;  Memory = 19.01 MB  Beats 7.38%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recurs(root)['is_bal']

    def recurs(self, root):
        if not root: return dict(is_bal=True, node_h=0)
        res1 = self.recurs(root.left)
        if not res1['is_bal']: return res1
        res2 = self.recurs(root.right)
        if not res2['is_bal']: return res2
        if abs(res1['node_h'] - res2['node_h']) > 1: res1['is_bal'] = False
        else: res1['node_h'] = 1 + max(res1['node_h'], res2['node_h'])
        return res1


sln = Solution()
root = TreeNode(3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)
print(sln.isBalanced(root))  # Output: true

sln = Solution()
left = TreeNode(2,
    TreeNode(3, TreeNode(4), TreeNode(4)),
    TreeNode(3)
)
right = TreeNode(2)
root = TreeNode(1, left, right)
print(sln.isBalanced(root))  # Output: false

sln = Solution()
root = None
print(sln.isBalanced(root))  # Output: true