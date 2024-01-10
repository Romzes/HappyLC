"""
2385. (Medium) Amount of Time for Binary Tree to Be Infected
You are given the root of a binary tree with unique values, and an integer start.
At minute 0, an infection starts from the node with value start.
Each minute, a node becomes infected if:
  The node is currently uninfected.
  The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

Constraints:
  The number of nodes in the tree is in the range [1, 10^5].
  1 <= Node.val <= 10^5
  Each node has a unique value.
  A node with a value of start exists in the tree.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.start = start; self.start_lev = -1; self.time_amount =-1;
        self.rec(nd=root, lev=1)
        return self.time_amount

    def rec(self, nd, lev):
        # lev = уровень вершины nd
        # return res = (cnt int, has_start bool);
        # cnt = кол-во вершин в максимальном пути от nd до листа
        # has_start = есть ли вершина start в дереве nd
        if not nd: return 0, False
        is_start = (nd.val == self.start)
        if is_start: self.start_lev = lev
        l_res = self.rec(nd.left, lev+1)
        r_res = self.rec(nd.right, lev+1)
        res = (1 + max(l_res[0], r_res[0]), is_start or l_res[1] or r_res[1])
        if res[1]:
            if is_start: time_amount = res[0]-1
            elif l_res[1]: time_amount = self.start_lev - lev + r_res[0]
            elif r_res[1]: time_amount = self.start_lev - lev + l_res[0]
            self.time_amount = max(self.time_amount, time_amount)
        return res

sln = Solution()
root = TreeNode(1,
    TreeNode(5, None, TreeNode(4, TreeNode(9), TreeNode(2))),
    TreeNode(3, TreeNode(10), TreeNode(6))
)
print(sln.amountOfTime(root, start=3))

sln = Solution()
print(sln.amountOfTime(root=TreeNode(1), start=1))