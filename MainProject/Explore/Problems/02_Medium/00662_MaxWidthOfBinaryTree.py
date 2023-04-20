# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# STACK BFS
class Solution:
    def widthOfBinaryTree(self, root):
        if not root: return 0
        stack = [(root, 1)]; levels = {}
        while stack:
            nd, k = stack.pop()
            h = int(math.log2(k))
            lev = levels.get(h)
            if lev: lev[0] = min(lev[0], k); lev[1] = max(lev[1], k);
            else: levels[h] = [k, k]
            if nd.right: stack.append((nd.right, 2*k+1))
            if nd.left: stack.append((nd.left, 2*k))
        return 1 + max(lev[1]-lev[0] for lev in levels.values())

## QUEUE BFS
class Solution:
    def widthOfBinaryTree(self, root):
        if not root: return 0
        level = [(root, 1)]; w = 1
        while level:
            w = max(w, level[-1][1]-level[0][1]+1)
            level = self.calc_next_level(level)
        return w

    def calc_next_level(self, level1):
        nodes2 = []
        for nd, k in level1:
            if nd.left: nodes2.append((nd.left, 2*k))
            if nd.right: nodes2.append((nd.right, 2*k+1))
        return nodes2

sln = Solution()
root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(9)), TreeNode(2, None, TreeNode(9)))
print(sln.widthOfBinaryTree(root))

sln = Solution()
root = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, TreeNode(7))))
print(sln.widthOfBinaryTree(root))

sln = Solution()
root = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
print(sln.widthOfBinaryTree(root))