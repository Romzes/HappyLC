# Medium 285. Inorder Successor in BST
# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
# If the given node has no in-order successor in the tree, return null.
# The successor of a node p is the node with the smallest key greater than p.val
# !!! All Nodes will have unique values !!!

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def inorderSuccessor(self, root, p):
        if p.right: return self.to_leftmost(node=p.right)
        return self.find_ancestor(root, p)

    def find_ancestor(self, root, p):
        curr, anc = root, None
        while curr != p:
            if p.val < curr.val: anc, curr = curr, curr.left
            elif curr.val < p.val: curr = curr.right
        return anc

    def to_leftmost(self, node):
        lm = node
        while lm.left: lm = lm.left
        return lm

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(9))
for p in [root.right, root, root.left, root.left.left, root.left.right]:
    res = sln.inorderSuccessor(root, p)
    print(res.val if res else None)
