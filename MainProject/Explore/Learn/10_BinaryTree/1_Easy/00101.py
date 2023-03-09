# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isSymmetric(self, root):
        if not root: return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, ln, rn):
        if not ln and not rn: return True
        # if (ln and not rn) or (not ln and rn) or (ln.val != rn.val): return False
        if not ln or not rn or ln.val != rn.val: return False  # упрощение предыдущей закомментированной строки
        # если первый вызов функции = False, то вторая функция не вызывается
        return self.is_mirror(ln.left, rn.right) and self.is_mirror(ln.right, rn.left)

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(2))
print(sln.isSymmetric(root))