"""
872. (Easy) Leaf-Similar Trees
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

from typing import Optional, List
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []
        self.build_leaves(root1, leaves1)
        self.build_leaves(root2, leaves2)
        return leaves1 == leaves2

    def build_leaves(self, nd, leaves: List[int]):
        if not nd: return
        if not nd.left and not nd.right:
            leaves.append(nd.val)
        else:
            self.build_leaves(nd.left, leaves)
            self.build_leaves(nd.right, leaves)

sln = Solution()
root1 = TreeNode(3,
    TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    TreeNode(1, TreeNode(9), TreeNode(8))
)
root2 = TreeNode(3,
    TreeNode(5, TreeNode(6), TreeNode(7)),
    TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8)))
)
print(sln.leafSimilar(root1, root2))

sln = Solution()
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(sln.leafSimilar(root1, root2))