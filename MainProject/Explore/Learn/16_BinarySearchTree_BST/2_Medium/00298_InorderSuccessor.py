# Medium 285. Inorder Successor in BST
# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
# If the given node has no in-order successor in the tree, return null.
# The successor of a node p is the node with the smallest key greater than p.val
# !!! All Nodes will have unique values !!!

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def inorderSuccessor(self, root, p):
        if p.right: return self.to_leftmost(node=p.right)
        path = self.build_path(root, p)
        if len(path) == 1: return None
        for i in range(len(path)-2, -1, -1):
            q = path[i]
            if q.left == path[i+1]: return q
        return None

    def build_path(self, root, p):
        node, path = root, []
        while node != p:
            path.append(node)
            if p.val < node.val: node = node.left
            elif node.val < p.val: node = node.right
        path.append(p)
        return path

    def to_leftmost(self, node):
        while node.left: node = node.left
        return node

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(9))
p = root.left.right
res = sln.inorderSuccessor(root, p)
print(res.val if res else None)
