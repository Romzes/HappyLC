"""
1457 (Medium) Pseudo-Palindromic Paths in a Binary Tree
Given a binary tree where node values are digits from 1 to 9.
A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
Constraints:
    The number of nodes in the tree is in the range [1, 10^5].
    1 <= Node.val <= 9
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.path = 10*[0]; self.res = 0
        self.rec(root)
        return self.res

    def rec(self, nd):
        if not nd: return
        self.path[nd.val] = 1 - self.path[nd.val]
        if not nd.left and not nd.right:
            self.res += (sum(self.path) < 2)  # leaf
        else:
            self.rec(nd.left)
            self.rec(nd.right)
        self.path[nd.val] = 1 - self.path[nd.val]

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.masks = 10*[0]; self.masks[1] = 1
        for i in range(2, 10): self.masks[i] = self.masks[i-1] << 1
        self.path = self.res = 0
        self.rec(root)
        return self.res

    def rec(self, nd):
        if not nd: return
        m = self.masks[nd.val]
        self.path ^= m
        if not nd.left and not nd.right:
            self.res += (int.bit_count(self.path) < 2)  # leaf
        else:
            self.rec(nd.left)
            self.rec(nd.right)
        self.path ^= m


sln = Solution()
root = TreeNode(2,
    TreeNode(3, TreeNode(3), TreeNode(1)),
    TreeNode(1, None, TreeNode(1))
)
print(sln.pseudoPalindromicPaths(root))

sln = Solution()
root = TreeNode(2,
    TreeNode(1, TreeNode(1), TreeNode(3, None, TreeNode(1))),
    TreeNode(1)
)
print(sln.pseudoPalindromicPaths(root))

sln = Solution()
root = TreeNode(9)
print(sln.pseudoPalindromicPaths(root))