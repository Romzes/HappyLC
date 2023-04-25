class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def maxPathSum(self, root):
        self.mps = float('-inf')
        self.max_child_path(root)
        return self.mps

    def max_child_path(self, nd):
        if not nd: return 0
        mlp, mrp = max(0, self.max_child_path(nd.left)), max(0, self.max_child_path(nd.right))
        self.mps = max(self.mps, mlp + nd.val + mrp)
        return nd.val + max(mlp, mrp)

sln = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(sln.maxPathSum(root))

sln = Solution()
root = TreeNode(-3, TreeNode(-2), TreeNode(-1))
print(sln.maxPathSum(root))

sln = Solution()
root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sln.maxPathSum(root))

