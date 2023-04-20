# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def widthOfBinaryTree(self, root):
        if not root: return 0
        level = [(root, 1)]; w = 1
        while level:
            w = max(w, level[-1][1]-level[0][1]+1)
            level = self.calc_next_level(level)
        return w

    def calc_next_level(self, level1):
        nodes2 = []
        for nd, k in level1:
            if nd.left: nodes2.append((nd.left, 2*k))
            if nd.right: nodes2.append((nd.right, 2*k+1))
        return nodes2

sln = Solution()
root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(9)), TreeNode(2, None, TreeNode(9)))
print(sln.widthOfBinaryTree(root))

sln = Solution()
root = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6))), TreeNode(2, None, TreeNode(9, TreeNode(7))))
print(sln.widthOfBinaryTree(root))

sln = Solution()
root = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
print(sln.widthOfBinaryTree(root))