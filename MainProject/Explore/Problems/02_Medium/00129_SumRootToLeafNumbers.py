# Medium 129. Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def sumNumbers(self, root):
        # root: Optional[TreeNode], return int
        if not root: return 0
        self.sum = 0
        self.add_recurs(node=root, prev=0)
        return self.sum

    def add_recurs(self, node, prev):
        curr = 10 * prev + node.val
        if not node.left and not node.right:
            self.sum += curr
            return
        if node.left: self.add_recurs(node.left, prev=curr)
        if node.right: self.add_recurs(node.right, prev=curr)

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1)
print(sln.sumNumbers(root))

sln = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(sln.sumNumbers(root))
