# Medium 116. Populating Next Right Pointers in Each Node
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# The binary tree has the following definition:
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val, self.left, self.right, self.next = val, left, right, next
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

class Solution:
    def connect(self, root):
        if not root: return root
        level = [root]
        while len(level) > 0:
            level = self.calc_next_level(level)
        return root

    def calc_next_level(self, curr_level):
        next_level = []
        for i, tn in enumerate(curr_level):
            if i < len(curr_level) - 1: tn.next = curr_level[i+1]
            if tn.left:
                next_level.append(tn.left)
                next_level.append(tn.right)
        return next_level

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
root = sln.connect(root)
print(root)