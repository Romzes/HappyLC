# 235 (Medium) Lowest Common Ancestor of a Binary Search Tree
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Constraints:
  The number of nodes in the tree is in the range [2, 105].
  -10^9 <= Node.val <= 10^9
  All Node.val are unique.
  p != q
  p and q will exist in the BST.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# Recursion Runtime = 48 ms  Beats 95.87%  ;  Memory = 21.05 MB  Beats 47.50%
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pv, self.qv = min(p.val, q.val), max(p.val, q.val)
        return self.rec(root)

    def rec(self, nd):
        if self.pv <= nd.val <= self.qv: return nd
        if self.qv < nd.val: return self.rec(nd.left)
        return self.rec(nd.right)

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        pv, qv, nd = min(p.val, q.val), max(p.val, q.val), root
        while not(pv <= nd.val <= qv): nd = nd.left if qv < nd.val else nd.right
        return nd


sln = Solution()
# root=[6,2,8,0,4,7,9,null,null,3,5]  p=2  q=8
p = TreeNode(2,
    TreeNode(0),
    TreeNode(4, TreeNode(3), TreeNode(5))
)
q = TreeNode(8, TreeNode(7), TreeNode(9))
root = TreeNode(6, p, q)
print(sln.lowestCommonAncestor(root, p, q))  # Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6


# sln = Solution()
# # root=[6,2,8,0,4,7,9,null,null,3,5]  p=2  q=4
# p = TreeNode(2,
#     TreeNode(0),
#     TreeNode(4, TreeNode(3), TreeNode(5))
# )
# q = TreeNode(8, TreeNode(7), TreeNode(9))
# root = TreeNode(6, p, q)
# print(sln.lowestCommonAncestor(root, p, q))  # Output: 6
# # Explanation: The LCA of nodes 2 and 8 is 6