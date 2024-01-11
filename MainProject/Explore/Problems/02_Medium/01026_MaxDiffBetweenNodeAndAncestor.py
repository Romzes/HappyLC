"""
1026. (Medium) Maximum Difference Between Node and Ancestor
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff = 0
        self.stack = []
        self.rec(root)
        return self.max_diff

    def rec(self, nd):
        if not nd: return
        if not self.stack:
            self.stack.append((nd.val, nd.val))
        else:
            rng = self.stack[-1]
            self.max_diff = max(self.max_diff, abs(nd.val-rng[0]), abs(nd.val-rng[1]))
            self.stack.append((min(rng[0], nd.val), max(rng[1], nd.val)))
        self.rec(nd.left)
        self.rec(nd.right)
        self.stack.pop()

sln = Solution()
root = TreeNode(8,
    TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
    TreeNode(10, None, TreeNode(14, TreeNode(13)))
)
print(sln.maxAncestorDiff(root))

sln = Solution()
root = TreeNode(1,
    None,
    TreeNode(2, None, TreeNode(0, TreeNode(3)))
)
print(sln.maxAncestorDiff(root))
