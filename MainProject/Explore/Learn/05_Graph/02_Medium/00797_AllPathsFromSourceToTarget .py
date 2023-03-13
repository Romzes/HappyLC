# Medium 797. All Paths From Source to Target
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph, src=None, dst=None):
        # graph: List[List[int]], return List[List[int]]
        if src is None: src = 0
        if dst is None: dst = len(graph)-1
        # return self.dfs_paths(graph, src, dst)
        return self.bfs_paths(graph, src, dst)

    def dfs_paths(self, graph, src, dst):
        res, stack = [], [[src]]
        while len(stack) > 0:
            path = stack.pop()
            cur = path[-1]
            if cur == dst:
                res.append(path)
                continue
            for v in graph[cur]:
                if v == dst: res.append(path + [v])  # оптимизация скорости
                elif v not in path: stack.append(path + [v])
        return res

    def bfs_paths(self, graph, src, dst):
        res, q = [], deque()
        q.append([src])
        while len(q) > 0:
            path = q.popleft()
            cur = path[-1]
            if cur == dst:
                res.append(path)
                continue
            for v in graph[cur]:
                if v == dst: res.append(path + [v])  # оптимизация скорости
                elif v not in path: q.append(path + [v])
        return res

########## TEST ########################################################################################################
sln = Solution()
graph = [[1,2],[3],[3],[]]
print(sln.allPathsSourceTarget(graph))
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(sln.allPathsSourceTarget(graph))
print(sln.allPathsSourceTarget(graph, src=0, dst=0))