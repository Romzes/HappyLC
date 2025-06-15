"""
404 (Easy) Sum of Left Leaves
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.rec(root, 'none')

    def rec(self, nd, p):
        if not nd: return 0
        if not nd.left and not nd.right: return nd.val if p == 'left' else 0
        return self.rec(nd.left, p='left') + self.rec(nd.right, p='right')

sln = Solution()
root = TreeNode(3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)
print(sln.sumOfLeftLeaves(root))

sln = Solution()
root = TreeNode(1)
print(sln.sumOfLeftLeaves(root))
