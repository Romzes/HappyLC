# Medium 117. Populating Next Right Pointers in Each Node II
# Given a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val, self.left, self.right, self.next = val, left, right, next
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

class Solution:
    def connect(self, root):
        pass

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
root = sln.connect(root)
print(root)