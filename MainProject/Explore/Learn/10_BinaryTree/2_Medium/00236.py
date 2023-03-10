# Medium 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia:
# The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
# !!! All Node.val are UNIQUE !!!

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if isinstance(p, TreeNode): p = p.val
        if isinstance(q, TreeNode): q = q.val
        pass

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
lca = sln.lowestCommonAncestor(root, 2, 3)
print(lca.val)