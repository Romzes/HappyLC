# 173. Binary Search Tree Iterator
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class BSTIterator:
    def __init__(self, root):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass

########## TEST ########################################################################################################
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(9))
iter = BSTIterator(root)
print(iter.next())
