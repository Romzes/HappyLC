# Easy 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

sln = Solution()
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(sln.isSameTree(p, q))

sln = Solution()
p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
print(sln.isSameTree(p, q))

sln = Solution()
p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
print(sln.isSameTree(p, q))
