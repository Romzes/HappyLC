# Medium 701. Insert into a Binary Search Tree
# You are given the root node of a binary search tree (BST) and a value to insert into the tree.
# Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
# You can return any of them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def insertIntoBST(self, root, val):
        vn = TreeNode(val)
        if not root: return vn
        curr = root
        while curr:
            if val < curr.val:
                if curr.left: curr = curr.left
                else:
                    curr.left = vn
                    return root
            elif curr.val < val:
                if curr.right: curr = curr.right
                else:
                    curr.right = vn
                    return root

########## TEST ########################################################################################################
sln = Solution()
root = None
sln.insertIntoBST(root)