# 144. Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

### Recursive
class Solution:
    def preorderTraversal(self, root):
        res = []
        self.preorder_recurs(root, res)
        return res

    def preorder_recurs(self, root, res):
        if root is None: return
        res.append(root.val)
        self.preorder_recurs(root.left, res)
        self.preorder_recurs(root.right, res)


sln = Solution()
root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
print(sln.preorderTraversal(root))
