# Easy 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

### Recursive
class Solution:
    def inorderTraversal(self, root):
        self.res = []  # для ускорения: res не передается в рекурсивную функцию
        if root: self.inorder_recurs(root)
        return self.res

    def inorder_recurs(self, node):
        # для ускорения: в рекурсивную функцию всегда передается node != None
        if node.left: self.inorder_recurs(node.left)
        self.res.append(node.val)
        if node.right: self.inorder_recurs(node.right)

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(sln.inorderTraversal(root))