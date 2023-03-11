# Medium 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia:
# The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
# !!! All Node.val are UNIQUE !!!

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if isinstance(p, TreeNode): p = p.val
        if isinstance(q, TreeNode): q = q.val
        self.vals = (min(p, q), max(p, q))
        self.empty_res = (None, 0)
        return self.find_recurs(root)[0]

    def find_recurs(self, node):
        # return : (None, 0) ничего не нашли ; (node, 2) нашли p и q; (node, 1) нашли только p или q
        if not node: return self.empty_res
        if node.val not in self.vals:
            left_res = self.find_recurs(node.left)
            if left_res[1] == 2: return left_res
            right_res = self.find_recurs(node.right)
            if left_res[0] and right_res[0]: return (node, 2)
            return left_res if left_res[0] else right_res
        else:  # node.val in (p, q)
            left_res = self.find_recurs(node.left)
            if left_res[0]: return (node, 2)
            right_res = self.find_recurs(node.right)
            if right_res[0]: return (node, 2)
            return (node, 1)

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(5)))
lca = sln.lowestCommonAncestor(root, 2, 5)
print(lca.val)