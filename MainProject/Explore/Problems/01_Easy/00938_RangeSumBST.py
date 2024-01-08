"""
938. Easy Range Sum of BST
Given the root node of a binary search tree and two integers low and high,
return the sum of values of all nodes with a value in the inclusive range [low, high].
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low, self.high = low, high
        return self.rec(root)

    def rec(self, nd):
        if not nd: return 0
        s = 0
        if self.low <= nd.val <= self.high: s += nd.val
        if self.low <= nd.val: s += self.rec(nd.left)
        if nd.val <= self.high: s += self.rec(nd.right)
        return s

sln = Solution()
root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
print(sln.rangeSumBST(root=root, low=7, high=15))

sln = Solution()
nd1 = TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6)))
nd2 = TreeNode(15, TreeNode(13), TreeNode(18))
root = TreeNode(10, nd1, nd2)
print(sln.rangeSumBST(root=root, low=6, high=10))

