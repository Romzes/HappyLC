# Easy 104. Maximum Depth of Binary Tree
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def maxDepth(self, root):
        if root is None: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(sln.maxDepth(root))