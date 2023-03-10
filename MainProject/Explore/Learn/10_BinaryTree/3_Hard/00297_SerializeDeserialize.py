# Hard 297. Serialize and Deserialize Binary Tree
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
# You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Codec:
    def serialize(self, root):
        # root -> string
        self.data = []
        self.ser_node(root)
        return ','.join(self.data)

    def ser_node(self, node):
        if not node:
            self.data.append('n')
            return
        self.data.append(str(node.val))
        self.ser_node(node.left)
        self.ser_node(node.right)

    def deserialize(self, data):
        # string -> root
        if data is None or data == '': return None
        self.values, self.ind = data.split(','), 0
        return self.deser_node()

    def deser_node(self):
        v = self.values[self.ind]
        self.ind += 1
        if v == 'n': return None
        node = TreeNode(int(v))
        node.left = self.deser_node()
        node.right = self.deser_node()
        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))