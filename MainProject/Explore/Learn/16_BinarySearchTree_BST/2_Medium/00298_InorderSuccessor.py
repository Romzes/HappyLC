# 285. Inorder Successor in BST
# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
# If the given node has no in-order successor in the tree, return null.
# The successor of a node p is the node with the smallest key greater than p.val

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def inorderSuccessor(self, root, p):
        if isinstance(p, TreeNode): p = p.val

########## TEST ########################################################################################################
