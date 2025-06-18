# 103 (Medium) Binary Tree Zigzag Level Order Traversal
"""
Given the root of a binary tree,
return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Constraints:
  The number of nodes in the tree is in the range [0, 2000].
  -100 <= Node.val <= 100
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.86 MB  Beats 95.41%
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        zigzag = []
        nodes = [root]
        dir = 1
        while nodes:
            j1, j2, step = (0, len(nodes), 1) if dir == 1 else (len(nodes)-1, -1, -1)
            zigzag.append([nodes[j].val for j in range(j1, j2, step)])
            next_nodes = []
            for nd in nodes:
                if nd.left: next_nodes.append(nd.left)
                if nd.right: next_nodes.append(nd.right)
            nodes = next_nodes
            dir *= -1
        return zigzag


sln = Solution()
root = TreeNode(3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)
print(sln.zigzagLevelOrder(root))  # Output: [[3],[20,9],[15,7]]

sln = Solution()
root = TreeNode(1)
print(sln.zigzagLevelOrder(root))  # Output: [[1]]

sln = Solution()
root = None
print(sln.zigzagLevelOrder(root))  # Output: []