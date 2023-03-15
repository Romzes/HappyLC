# Medium 958. Check Completeness of a Binary Tree
# Given the root of a binary tree, determine if it is a complete binary tree.
# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

##### self.node_cnt == self.max_num RECURSION
class Solution:
    def isCompleteTree(self, root):
        if not root: return True
        self.node_cnt = self.max_num = 0
        self.recurs(root, num=1)
        return self.node_cnt == self.max_num

    def recurs(self, node, num):
        if not node: return
        self.node_cnt += 1
        self.max_num = max(self.max_num, num)
        self.recurs(node.left, 2*num)
        self.recurs(node.right, 2*num+1)

##### self.node_cnt == self.max_num STACK
class Solution:
    def isCompleteTree(self, root):
        if not root: return True
        node_cnt = max_num = 0
        stack = [(root, 1)]
        while len(stack) > 0:
            node, num = stack.pop()
            node_cnt += 1
            max_num = max(max_num, num)
            if node.left: stack.append((node.left, 2*num))
            if node.right: stack.append((node.right, 2*num+1))
        return node_cnt == max_num

##### STACK LEAF Optimization
class Solution:
    def isCompleteTree(self, root):
        if not root: return True
        self.node_cnt = self.max_ord = 0
        self.first_leaf_h = None
        return self.check(node=root, h=1, ord=1) and (self.node_cnt == self.max_ord)

    def check(self, node, h, ord):
        if not node: return True
        self.node_cnt += 1
        if node.right and not node.left: return False
        if self.first_leaf_h is not None and self.first_leaf_h < h: return False
        if not node.left and not node.right:
            if self.first_leaf_h is None:
                self.first_leaf_h, self.max_ord = h, ord
                return True
            else:
                if h < self.first_leaf_h - 1: return False
                if ord > self.max_ord + 1: return False
                self.max_ord = max(self.max_ord, ord)
                return True
        return self.check(node.left, h+1, 2*ord) and self.check(node.right, h+1, 2*ord+1)

##### QUEUE Optimization
class Solution:
    def isCompleteTree(self, root):
        if not root: return True
        level, h, no_child = [root], 0, False
        while len(level) > 0:
            h += 1
            level, err = self.get_next_level(level, no_child)
            if err: return False
            no_child = (len(level) != 2**h)
        return True

    def get_next_level(self, full_level, no_child):
        next_level = []
        for node in full_level:
            if node.left:
                if no_child: return next_level, True
                else: next_level.append(node.left)
            else: no_child = True
            if node.right:
                if no_child: return next_level, True
                else: next_level.append(node.right)
            else: no_child = True
        return next_level, False

##### !!! Fastest !!!
from collections import deque
class Solution:
    def isCompleteTree(self, root):
        q, null_flag = deque([root]), False
        while len(q) > 0:
            node = q.popleft()
            if not node:
                null_flag = True
                continue
            if null_flag: return False
            q.append(node.left)
            q.append(node.right)
        return True

########## TEST ########################################################################################################
sln = Solution()
root = TreeNode(1, TreeNode(2,  TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(11), TreeNode(6)))
print(sln.isCompleteTree(root))