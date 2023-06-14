# Easy 530. Minimum Absolute Difference in BST
# Given the root of a Binary Search Tree (BST),
# return the minimum absolute difference between the values of any two different nodes in the tree.
# Constraints:
#   The number of nodes in the tree is in the range [2, 10^4].
#   0 <= Node.val <= 10^5

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution(object):
    def getMinimumDifference(self, root):
        c = None; d = float('inf')
        def rec(nd):
            if not nd: return
            nonlocal c, d
            rec(nd.left)
            if c is not None: d = min(d, nd.val-c)
            c = nd.val
            rec(nd.right)
        rec(root)
        return d

sln = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(sln.getMinimumDifference(root))

sln = Solution()
root = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
print(sln.getMinimumDifference(root))

