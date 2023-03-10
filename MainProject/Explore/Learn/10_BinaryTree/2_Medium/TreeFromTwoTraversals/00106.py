# Medium 106. Construct Binary Tree from Inorder and Postorder Traversal
# Given two integer arrays inorder and postorder
# where inorder is the inorder traversal of a binary tree
# and postorder is the postorder traversal of the same tree,
# construct and return the binary tree.

# !!! inorder and postorder consist of UNIQUE values !!!

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def buildTree(self, inorder, postorder):
        self.inorder = inorder
        self.inorder_map = {v: i for i, v in enumerate(inorder)}
        self.postorder, self.post_ind = postorder, len(postorder)-1
        return self.build_recurs(k1=0, k2=len(self.inorder)-1)

    def build_recurs(self, k1, k2):
        # k1 first, k2 last : inorder-indexes
        if k1 > k2: return None
        tn = TreeNode(val=self.postorder[self.post_ind])
        inorder_ind = self.inorder_map[tn.val]
        self.post_ind -= 1
        # !!! важен порядок вычисления: сначала tn.right, потом tn.left
        tn.right = self.build_recurs(k1=inorder_ind+1, k2=k2)
        tn.left = self.build_recurs(k1=k1, k2=inorder_ind-1)
        return tn

########## TEST ########################################################################################################
sln = Solution()
root = sln.buildTree(inorder=[2,1,3], postorder=[2,3,1])
print(root)