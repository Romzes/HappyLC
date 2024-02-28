"""
513 (Medium) Find Bottom Left Tree Value
Given the root of a binary tree, return the leftmost value in the last row of the tree.
Constraints:
  The number of nodes in the tree is in the range [1, 104].
  -2^31 <= Node.val <= 2^31 - 1
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        while dq:
            ans = dq[0].val
            for i in range(len(dq)):
                nd = dq.popleft()
                if nd.left: dq.append(nd.left)
                if nd.right: dq.append(nd.right)
        return ans

sln = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(sln.findBottomLeftValue(root))

sln = Solution()
root = TreeNode(1,
    TreeNode(2, TreeNode(4)),
    TreeNode(3, TreeNode(5, TreeNode(7)), TreeNode(6))
)
print(sln.findBottomLeftValue(root))