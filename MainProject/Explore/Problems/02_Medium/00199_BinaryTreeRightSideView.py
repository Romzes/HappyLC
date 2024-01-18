"""
199 (Medium) Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
Constraints:
  The number of nodes in the tree is in the range [0, 100].
  -100 <= Node.val <= 100
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Runtime = 47 ms ; Beats 18.61% of users with Python3
        # Memory = 17.42 MB ; Beats 21.26% of users with Python3
        if not root: return []
        res = []; levels = [root]
        while levels:
            res.append(levels[-1].val)
            next_levels = []
            for nd in levels:
                if nd.left: next_levels.append(nd.left)
                if nd.right: next_levels.append(nd.right)
            levels = next_levels
        return res

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Runtime = 30 ms ; Beats 95.30% of users with Python3
        # Memory = 17.08 MB ; Beats 51.09% of users with Python3
        if not root: return []
        res = []; dq = deque(); dq.append(root)
        while dq:
            res.append(dq[-1].val)
            for _ in range(len(dq)):
                nd = dq.popleft()
                if nd.left: dq.append(nd.left)
                if nd.right: dq.append(nd.right)
        return res

sln = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(sln.rightSideView(root))