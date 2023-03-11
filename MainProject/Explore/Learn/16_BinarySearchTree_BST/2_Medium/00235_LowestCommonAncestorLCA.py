# Mediumn 235. Lowest Common Ancestor of a Binary Search Tree

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
        if self.vals[1] < node.val: return self.find_recurs(node.left)
        if self.vals[1] == node.val: return (node, 2) if self.find_recurs(node.left)[0] else (node, 1)
        if node.val < self.vals[0]: return self.find_recurs(node.right)
        if node.val == self.vals[0]: return (node, 2) if self.find_recurs(node.right)[0] else (node, 1)
        # self.vals[0] < node.val < self.vals[1]
        left_res, right_res = self.find_recurs(node.left), self.find_recurs(node.right)
        if left_res[0] and right_res[0]: return (node, 2)
        return left_res if left_res[0] else right_res

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(5, TreeNode(3), TreeNode(8, TreeNode(7), TreeNode(9)))
lca = sln.lowestCommonAncestor(root, 7, 9)
print(lca.val)