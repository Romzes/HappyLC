# Easy 145. Binary Tree Postorder Traversal
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

### Recursive
class Solution:
    def postorderTraversal(self, root):
        res = []
        self.postorder_recurs(root, res)
        return res

    def postorder_recurs(self, node, res):
        if node is None: return
        self.postorder_recurs(node.left, res)
        self.postorder_recurs(node.right, res)
        res.append(node.val)

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(sln.postorderTraversal(root))