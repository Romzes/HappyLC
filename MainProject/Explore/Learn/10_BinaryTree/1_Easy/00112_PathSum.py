# 112 (Easy) Path Sum
"""
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root: return False  # даже если targetSum = 0
        ts = targetSum - root.val
        if not root.left and not root.right: return ts == 0
        return self.hasPathSum(root.left, ts) or self.hasPathSum(root.right, ts)


sln = Solution()
root = None
print(sln.hasPathSum(root, 0))  # Output: False

sln = Solution()
root = TreeNode(1, TreeNode(10), TreeNode(5))
print(sln.hasPathSum(root, 6))  # Output: True