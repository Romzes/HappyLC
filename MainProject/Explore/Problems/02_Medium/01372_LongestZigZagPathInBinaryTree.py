# You are given the root of a binary tree.
# A ZigZag path for a binary tree is defined as follow:
#   Choose any node in the binary tree and a direction (right or left).
#   If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
#   Change the direction from right to left or from left to right.
#   Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
# Return the longest ZigZag path contained in that tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def longestZigZag(self, root):
        self.mx = -float('inf')
        self.calc(nd=root)
        return self.mx

    def calc(self, nd):
        res_l = 1 + self.calc(nd.left)[1] if nd.left else 0
        res_r = 1 + self.calc(nd.right)[0] if nd.right else 0
        self.mx = max(self.mx, res_l, res_r)
        return res_l, res_r  # для скорости и экономии памяти нужно возвращать tuple (а не dict)

sln = Solution()
root = TreeNode(0, TreeNode(1), TreeNode(2, TreeNode(3, None, TreeNode(4))))
print(sln.longestZigZag(root))