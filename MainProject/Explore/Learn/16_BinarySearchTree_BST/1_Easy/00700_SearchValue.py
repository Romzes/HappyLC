# Easy 700. Search in a Binary Search Tree
# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
# If such a node does not exist, return null.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def searchBST(self, root, val):
        curr = root
        while curr:
            if val == curr.val: return curr
            if val < curr.val: curr = curr.left
            elif curr.val < val: curr = curr.right
        return None

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(5, TreeNode(3), TreeNode(8))
node = sln.searchBST(root, 8)
print(node.val if node else None)