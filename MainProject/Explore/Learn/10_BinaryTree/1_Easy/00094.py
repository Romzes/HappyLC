# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

### Recursive
class Solution:
    def inorderTraversal(self, root):
        self.res = []
        self.inorder(root)
        return self.res

    def inorder(self, root):
        if root is None: return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(sln.inorderTraversal(root))