# Medium 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

from collections import deque
class Solution:
    def levelOrder(self, root):
        if root is None: return []
        res = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            level, q = self.proc_level(q)
            res.append(level)
        return res

    def proc_level(self, q_curr):
        level = []
        q_next = deque()
        while len(q_curr) > 0:
            tn = q_curr.popleft()
            level.append(tn.val)
            if tn.left is not None: q_next.append(tn.left)
            if tn.right is not None: q_next.append(tn.right)
        return level, q_next

class Solution:
    def levelOrder(self, root):
        if root is None: return []
        res = []
        q_curr = [root]
        while len(q_curr) > 0:
            level, q_next = [], []
            for tn in q_curr:
                level.append(tn.val)
                if tn.left is not None: q_next.append(tn.left)
                if tn.right is not None: q_next.append(tn.right)
            res.append(level)
            q_curr = q_next
        return res

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(20, TreeNode(30), None), TreeNode(2, TreeNode(3), None))
print(sln.levelOrder(root))