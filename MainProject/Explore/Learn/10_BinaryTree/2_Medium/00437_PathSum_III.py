# 437 (Medium) Path Sum III
"""
Given the root of a binary tree and an integer targetSum,
return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf,
but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Constraints:
  The number of nodes in the tree is in the range [0, 1000].
  -10^9 <= Node.val <= 10^9
  -1000 <= targetSum <= 1000
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target_sum = targetSum
        self.prefix_sum = {}
        self.path_cnt = 0
        self.recurs(nd=root, prev_sum=0)
        return self.path_cnt

    def recurs(self, nd, prev_sum):
        if not nd: return
        curr_sum = prev_sum + nd.val
        # кол-во путей, которые заканчиваются в nd
        if curr_sum == self.target_sum: self.path_cnt += 1
        self.path_cnt += self.prefix_sum.get(curr_sum - self.target_sum, 0)
        self.prefix_sum[curr_sum] = self.prefix_sum.get(curr_sum, 0) + 1
        self.recurs(nd=nd.left, prev_sum=curr_sum)
        self.recurs(nd=nd.right, prev_sum=curr_sum)
        self.prefix_sum[curr_sum] -= 1
        if self.prefix_sum[curr_sum] == 0: self.prefix_sum.pop(curr_sum)


sln = Solution()
left = TreeNode(5,
    TreeNode(3, TreeNode(3), TreeNode(-2)),
    TreeNode(2, None, TreeNode(1))
)
right = TreeNode(-3, None, TreeNode(11))
root = TreeNode(10, left, right)
print(sln.pathSum(root, targetSum=8))  # Output: 3