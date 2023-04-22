# Medium 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isValidBST(self, root):
        return self.check_recurs(node=root, v1=float('-inf'), v2=float('inf'))

    def check_recurs(self, node, v1, v2):
        if not node: return True
        # if not (v1 <= node.val <= v2): return False  # нестрогие условия
        if not (v1 < node.val < v2): return False  # строгие условия
        return self.check_recurs(node.left, v1=v1, v2=node.val) and self.check_recurs(node.right, v1=node.val, v2=v2)

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, None, TreeNode(3, TreeNode(2)))
print(sln.isValidBST(root))