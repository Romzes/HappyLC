# Medium 1161. Maximum Level Sum of a Binary Tree
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def maxLevelSum(self, root):
        curr_nodes = [root]; curr_lev = 1; max_sum = float('-inf'); max_lev = -1
        while curr_nodes:
            curr_sum = sum(nd.val for nd in curr_nodes)
            if curr_sum > max_sum: max_sum = curr_sum; max_lev = curr_lev
            curr_nodes = self.get_next_level(curr_nodes)
            curr_lev += 1
        return max_lev

    def get_next_level(self, curr_nodes):
        next_nodes = []
        for nd in curr_nodes:
            if nd.left: next_nodes.append(nd.left)
            if nd.right: next_nodes.append(nd.right)
        return next_nodes

sln = Solution()
root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
print(sln.maxLevelSum(root))