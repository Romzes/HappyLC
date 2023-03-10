# Medium 105. Construct Binary Tree from Preorder and Inorder Traversal
# Given two integer arrays preorder and inorder
# where preorder is the preorder traversal of a binary tree
# and inorder is the inorder traversal of the same tree,
# construct and return the binary tree.

# !!! preorder and inorder consist of UNIQUE values !!!

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def buildTree(self, preorder, inorder):
        self.inorder = inorder
        self.inorder_map = {v: i for i, v in enumerate(inorder)}
        self.preorder, self.pre_ind = preorder, 0
        return self.build_recurs(k1=0, k2=len(self.inorder)-1)

    def build_recurs(self, k1, k2):
        # k1 first, k2 last : inorder-indexes
        if k1 > k2: return None
        tn = TreeNode(val=self.preorder[self.pre_ind])
        inorder_ind = self.inorder_map[tn.val]
        self.pre_ind += 1
        # !!! важен порядок вычисления: сначала tn.left, потом tn.right
        tn.left = self.build_recurs(k1=k1, k2=inorder_ind-1)
        tn.right = self.build_recurs(k1=inorder_ind+1, k2=k2)
        return tn

########## TEST ########################################################################################################
sln = Solution()
root = sln.buildTree(preorder=[1,2,3], inorder=[2,1,3])
print(root)