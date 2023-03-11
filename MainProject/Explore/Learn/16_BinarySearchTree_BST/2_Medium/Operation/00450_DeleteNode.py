# Medium 450. Delete Node in a BST
# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# 1) Search for a node to remove.
# 2) If the node is found, delete the node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def deleteNode(self, root, key):
        if not root: return None
        key_node, key_par = self.find_key(root, key)
        if not key_node: return root  # key not found
        if key_node.left and key_node.right:
            min_node, min_par = self.find_min_node(key_node, key_node.right)
            key_node.val = min_node.val
            if min_par.left == min_node: min_par.left = None
            else: min_par.right = None
        else:
            key_child = key_node.left if key_node.left else key_node.right
            if key_par:
                if key_par.left == key_node: key_par.left = key_child
                elif key_par.right == key_node: key_par.right = key_child
            else: root = key_child
        return root

    def find_min_node(self, key_node, key_node_right):
        min_node, min_par = key_node_right, key_node
        while min_node.left: min_node, min_par = min_node.left, min_node
        return min_node, min_par

    def find_key(self, root, key):
        key_node, key_par = root, None
        while key_node and key_node.val != key:
            key_par = key_node
            if key < key_node.val: key_node = key_node.left
            elif key_node.val < key: key_node = key_node.right
        return key_node, key_par

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(5, TreeNode(3), TreeNode(8))
root = sln.deleteNode(root, key=8)
print(root.val if root else None)