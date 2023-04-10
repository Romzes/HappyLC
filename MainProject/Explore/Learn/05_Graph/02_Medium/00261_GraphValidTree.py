# Medium 261. Graph Valid Tree
# You have a graph of n nodes labeled from 0 to n - 1.
# You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.

class Solution:
    def validTree(self, n, edges):
        if len(edges) != n-1: return False
        graph = self.create_graph(n, edges)
        nodes = n * [False]
        v0 = edges[0][0]
        nodes[v0], stack = True, [v0]
        while stack:
            v1 = stack.pop()


    def create_graph(self, n, edges):
        graph = n * []
        for e in edges:
            u, v = e[0], e[1]
            if graph[u] is None: graph[u] = []
            graph[u].append(v)
            if graph[v] is None: graph[v] = []
            graph[v].append(u)
        return graph

sln = Solution()
print(sln.validTree(n=5, edges=[[0,1],[0,2],[0,3],[1,4]]))

sln = Solution()
print(sln.validTree(n=5, edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]))
