# Medium 450. Delete Node in a BST
# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# 1) Search for a node to remove.
# 2) If the node is found, delete the node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def deleteNode(self, root, key):
        pass

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(5, TreeNode(3), TreeNode(8))
root = sln.deleteNode(root, key=5)
print(root.val if root else None)