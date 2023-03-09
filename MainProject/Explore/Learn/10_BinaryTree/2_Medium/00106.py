# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Given two integer arrays inorder and postorder
# where inorder is the inorder traversal of a binary tree
# and postorder is the postorder traversal of the same tree,
# construct and return the binary tree.

# !!! inorder and postorder consist of UNIQUE values. !!!

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def buildTree(self, inorder, postorder):
        self.inorder, self.postorder = inorder, postorder
        self.inorder_map = {v: i for i, v in enumerate(self.inorder)}
        return self.build_recurs(n1=0, n2=len(postorder)-1)

    def build_recurs(self, n1, n2):
        if n1 > n2: return None
        tn = TreeNode(val=self.postorder[n2])
        vi = self.inorder_map[tn.val]
        k = n2 - 1
        while n1 <= k and self.inorder_map[self.postorder[k]] > vi:
            k -= 1
        tn.left, tn.right = self.build_recurs(n1, k), self.build_recurs(k+1, n2-1)
        return tn

########## TEST ########################################################################################################
sln = Solution()
root = sln.buildTree(inorder=[2,1,4,3], postorder=[2,4,3,1])
print(root)