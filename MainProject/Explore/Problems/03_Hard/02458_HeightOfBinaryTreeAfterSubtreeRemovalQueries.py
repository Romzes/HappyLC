"""
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n.
You are also given an array queries of size m.
You have to perform m independent queries on the tree where in the ith query you do the following:
    Remove the subtree rooted at the node with the value queries[i] from the tree.
    It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.
Note:
    The queries are independent, so the tree returns to its initial state after each query.
    The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def treeQueries(self, root, queries):
        self.root = root
        self.queries = {q: {} for q in queries}
        self.calc_all_routes()

    def calc_all_routes(self):
        self.routes = [0]  # number of nodes in route
        self.proc_node(self.root, curr_route_ind=0, prev_node_cnt=0)

    def proc_node(self, nd, curr_route_ind, prev_node_cnt):
        # nd is not None
        prev_node_cnt += 1
        if curr_route_ind is not None:
            self.routes[curr_route_ind] = prev_node_cnt
        else:
            curr_route_ind = len(self.routes)
            self.routes.append(prev_node_cnt)

        qi = self.queries.get(nd.val)
        if qi:
            pass


        if nd.left and not nd.right:
            self.proc_node(nd.left, curr_route_ind, prev_node_cnt)
        elif not nd.left and nd.right:
            self.proc_node(nd.right, curr_route_ind, prev_node_cnt)
        elif nd.left and nd.right:
            self.proc_node(nd.left, curr_route_ind, prev_node_cnt)
            self.proc_node(nd.right, None, prev_node_cnt)


##### Example 1 ########################################################################################################
root = TreeNode(1,
        TreeNode(3, TreeNode(2)),
        TreeNode(4, TreeNode(6), TreeNode(5, None, TreeNode(7)))
    )
sln = Solution()
sln.treeQueries(root, queries=[4])
print(sln.routes)

##### Example 2 ########################################################################################################


