# Medium 133. Clone Graph
# Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node: return None
        stack, visited, clones = [node], set(), {}
        while len(stack) > 0:
            src = stack.pop()
            if src in visited: continue
            visited.add(src)
            dst = self.get_cloned_node(src, clones)
            for i, src_child in enumerate(src.neighbors):
                dst.neighbors[i] = self.get_cloned_node(src_child, clones)
                if src_child not in visited: stack.append(src_child)
        return clones[node]

    def get_cloned_node(self, src, clones):
        if src not in clones: clones[src] = Node(val=src.val, neighbors=len(src.neighbors) * [None])
        return clones[src]

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


