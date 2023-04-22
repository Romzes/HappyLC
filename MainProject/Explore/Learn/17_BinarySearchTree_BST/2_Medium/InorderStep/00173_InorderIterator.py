# Medium 173. Binary Search Tree Iterator
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# !!! НУЖНО УСКОРИТЬ !!!
class BSTIterator:
    def __init__(self, root):
        self.root, self.curr_node, self.next_node, self.next_calc = root, None, None, False

    def next(self):
        if self.hasNext():
            self.curr_node, self.next_node, self.next_calc = self.next_node, None, False
            return self.curr_node.val
        else:
            return None

    def hasNext(self):
        self.calc_next_node()
        return self.next_node is not None

    def calc_next_node(self):
        if not self.next_calc:
            if not self.curr_node: self.next_node = self.to_leftmost(node=self.root)
            else: self.next_node = self.inorderSuccessor(p=self.curr_node)
        self.next_calc = True

    def inorderSuccessor(self, p):
        if p.right: return self.to_leftmost(node=p.right)
        return self.find_ancestor(p)

    def find_ancestor(self, p):
        curr, anc = self.root, None
        while curr != p:
            if p.val < curr.val:
                anc, curr = curr, curr.left
            elif curr.val < p.val:
                curr = curr.right
        return anc

    def to_leftmost(self, node):
        lm = node
        while lm.left: lm = lm.left
        return lm

########## TEST ########################################################################################################
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(9))
iter = BSTIterator(root)
while iter.hasNext():
    print(iter.next())
print(iter.next())
