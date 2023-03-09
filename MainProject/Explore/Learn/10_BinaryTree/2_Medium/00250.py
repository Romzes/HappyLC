# 250. Count Univalue Subtrees
# Given the root of a binary tree, return the number of uni-value subtrees.
# A uni-value subtree means all nodes of the subtree have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def countUnivalSubtrees(self, root):
        return self.count_rec(root)[0]

    def count_rec(self, root):
        if not root: return 0, False
        left_cnt, left_flag = self.count_rec(root.left)
        right_cnt, right_flag = self.count_rec(root.right)
        curr_cnt = left_cnt + right_cnt
        curr_flag = (not root.left or (left_flag and root.left.val == root.val)) and \
                    (not root.right or (right_flag and root.right.val == root.val))
        if curr_flag: curr_cnt += 1
        return curr_cnt, curr_flag

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(1, TreeNode(2, None, TreeNode(2))), TreeNode(1))
print(sln.countUnivalSubtrees(root))