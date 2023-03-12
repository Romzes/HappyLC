# Medium 133. Clone Graph
# Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# Node.val is UNIQUE for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node: return None
        stack, clones = [node], {node: self.clone_node(node)}
        while len(stack) > 0:
            src = stack.pop()
            cln = clones[src]
            for i, src_neigh in enumerate(src.neighbors):
                if src_neigh not in clones:
                    clones[src_neigh] = self.clone_node(src_neigh)
                    stack.append(src_neigh)
                cln.neighbors[i] = clones[src_neigh]
        return clones[node]

    def clone_node(self, src):
        return Node(val=src.val, neighbors=len(src.neighbors) * [None])

########## TEST ########################################################################################################
nd1 = Node(1)
nd2 = Node(2)
nd3 = Node(3)
nd4 = Node(4)
nd1.neighbors = [nd2, nd3, nd4]
nd2.neighbors = [nd1, nd3, nd4]
nd3.neighbors = [nd1, nd2]
nd4.neighbors = [nd1, nd2]
sln = Solution()
cnd1 = sln.cloneGraph(nd1)
print(cnd1)


