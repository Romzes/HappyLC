# Medium 117. Populating Next Right Pointers in Each Node II
# Given a binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val, self.left, self.right, self.next = val, left, right, next
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# !!! Код решения задач 116 и 117 полностью совпадает !!!
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
            if tn.left: next_level.append(tn.left)
            if tn.right: next_level.append(tn.right)
        return next_level

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
root = sln.connect(root)
print(root)