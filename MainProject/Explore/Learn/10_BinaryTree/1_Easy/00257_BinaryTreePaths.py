# Easy 257. Binary Tree Paths

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def binaryTreePaths(self, root):
        self.stack = []; self.result = []
        self.rec(root)
        return self.result

    def rec(self, nd):
        # if not nd: return
        self.stack.append(str(nd.val))
        if not nd.left and not nd.right:
            self.result.append('->'.join(self.stack))
        else:
            if nd.left: self.rec(nd.left)
            if nd.right: self.rec(nd.right)
        self.stack.pop()

sln = Solution()
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(sln.binaryTreePaths(root))

sln = Solution()
root = TreeNode(1)
print(sln.binaryTreePaths(root))