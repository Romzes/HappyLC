# 113 (Medium) Path Sum II
"""
Given the root of a binary tree and an integer targetSum,
return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node.
A leaf is a node with no children.

Constraints:
  The number of nodes in the tree is in the range [0, 5000].
  -1000 <= Node.val <= 1000
  -1000 <= targetSum <= 1000
"""

from typing import Optional, List
import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.stack = []  # List[val=int]
        self.res = []  # List[List[val=int]]
        self.recurs(nd=root, targetSum=targetSum)
        return self.res

    def recurs(self, nd: Optional[TreeNode], targetSum: int):
        if not nd: return
        self.stack.append(nd.val)
        ts = targetSum - nd.val
        if not nd.left and not nd.right and ts == 0:
            self.res.append(copy.deepcopy(self.stack))
        else:
            self.recurs(nd=nd.left, targetSum=ts)
            self.recurs(nd=nd.right, targetSum=ts)
        self.stack.pop()


sln = Solution()
root = TreeNode(5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8,
        TreeNode(13),
        TreeNode(4, TreeNode(5), TreeNode(1))
    )
)
print(sln.pathSum(root, targetSum=22))  # Output: [[5,4,11,2],[5,8,4,5]]

sln = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(sln.pathSum(root, targetSum=5))  # Output: []

sln = Solution()
root = TreeNode(1, TreeNode(2))
print(sln.pathSum(root, targetSum=0))  # Output: []