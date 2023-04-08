# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def verticalOrder(self, root):
        if not root: return None
        pos, neg = [], []  # >= 0, < 0
        q = deque()
        q.append((root, 0))
        while q:
            nd, col = q.popleft()
            arr, i = (pos, col) if col >= 0 else (neg, -col-1)
            if i == len(arr): arr.append([])
            arr[i].append(nd.val)
            if nd.left: q.append((nd.left, col-1))
            if nd.right: q.append((nd.right, col+1))
        res = []
        for i in range(len(neg)-1, -1, -1): res.append(neg[i])
        res.extend(pos)
        return res

sln = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sln.verticalOrder(root))

sln = Solution()
root = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
print(sln.verticalOrder(root))
