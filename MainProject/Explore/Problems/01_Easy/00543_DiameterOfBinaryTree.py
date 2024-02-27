"""
543 (Easy) Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.rec(nd=root)
        return self.res

    def rec(self, nd):
        if not nd: return 0
        k1, k2 = self.rec(nd.left), self.rec(nd.right)
        self.res = max(self.res, k1+k2)
        return 1 + max(k1, k2)

sln = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(sln.diameterOfBinaryTree(root))

sln = Solution()
root = TreeNode(1, TreeNode(2))
print(sln.diameterOfBinaryTree(root))