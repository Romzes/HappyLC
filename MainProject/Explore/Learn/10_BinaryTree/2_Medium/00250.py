# Medium 250. Count Univalue Subtrees
# Given the root of a binary tree, return the number of uni-value subtrees.
# A uni-value subtree means all nodes of the subtree have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def countUnivalSubtrees(self, root):
        return self.count_rec(root)[0]

    def count_rec(self, node):
        # return tuple : cnt = number of univalue-subtrees, flag = (node.val == univalue)
        if not node: return 0, False
        left_cnt, left_flag = self.count_rec(node.left)
        right_cnt, right_flag = self.count_rec(node.right)
        curr_cnt = left_cnt + right_cnt
        curr_flag = (not node.left or (left_flag and node.left.val == node.val)) and \
                    (not node.right or (right_flag and node.right.val == node.val))
        if curr_flag: curr_cnt += 1
        return curr_cnt, curr_flag

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(1, TreeNode(2, None, TreeNode(2))), TreeNode(1))
print(sln.countUnivalSubtrees(root))