"""
1609 (Medium) Even Odd Tree
A binary tree is named Even-Odd if it meets the following conditions:
  The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
  For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
  For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
Constraints:
  The number of nodes in the tree is in the range [1, 10^5].
  1 <= Node.val <= 10^6
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        nodes = [root]; r = 1; sgn = 1
        while nodes:
            nodes2 = []
            for i in range(len(nodes)):
                nd = nodes[i]
                if nd.val % 2 != r: return False
                if i > 0 and sgn*(nd.val - nodes[i-1].val) <= 0: return False
                if nd.left: nodes2.append(nd.left)
                if nd.right: nodes2.append(nd.right)
            nodes = nodes2; r = 1-r; sgn = -sgn
        return True

# sln = Solution()
# root = None
# print(sln.isEvenOddTree(root))

sln = Solution()
root = TreeNode(5,
    TreeNode(4, TreeNode(3), TreeNode(3)),
    TreeNode(2, TreeNode(7))
)
print(sln.isEvenOddTree(root))

sln = Solution()
root = TreeNode(5,
    TreeNode(9, TreeNode(3), TreeNode(5)),
    TreeNode(1, TreeNode(7))
)
print(sln.isEvenOddTree(root))