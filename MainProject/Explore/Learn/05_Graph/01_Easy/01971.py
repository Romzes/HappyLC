#  Easy 1971. Find if Path Exists in Graph
# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
# Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

class Solution:
    def validPath(self, n, edges, source, destination):
        # n, source, destination: int, edges: List[List[int]]
        if source == destination: return True
        return self.find_path(self.create_graph(edges), source, destination)

    # visited-list variant 1
    def find_path(self, graph, src, dst):
        if src not in graph or dst not in graph: return False
        stack, visited = [src], set()
        while len(stack) > 0:
            cur = stack.pop()
            if cur in visited: continue
            visited.add(cur)
            for nd in graph[cur]:
                if nd == dst: return True
                if nd not in visited: stack.append(nd)
        return False

    # visited-list variant 2
    def find_path(self, graph, src, dst):
        if src not in graph or dst not in graph: return False
        stack = [src]
        ordered = set([src])  # если нет в ordered, то можно добавлять в stack (133. Clone Graph)
        while len(stack) > 0:
            cur = stack.pop()
            for nd in graph[cur]:
                if nd == dst: return True
                if nd not in ordered:
                    ordered.add(nd)
                    stack.append(nd)
        return False

    def create_graph(self, edges):
        graph = {}
        for edge in edges:
            v1, v2 = edge[0], edge[1]
            self.add_edge(graph, v1, v2)
            self.add_edge(graph, v2, v1)
        return graph

    def add_edge(self, graph, v1, v2):
        # edge v1 -> v2
        if v1 not in graph: graph[v1] = set()
        graph[v1].add(v2)

########## TEST ########################################################################################################
sln = Solution()
print(sln.validPath(n=3, edges=[[0,1],[1,2],[2,0]], source=0, destination=2))
print(sln.validPath(n=6, edges=[[0,1],[0,2],[3,5],[5,4],[4,3]], source=0, destination=5))

