# 827 (Hard) Making A Large Island
"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.
"""

from typing import List

# Runtime = 1251 ms  Beats28.29%  ;  Memory = 39.51 MB  Beats 32.97%
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])  # num-row, num-columns
        self.res = 0
        self.create_islands()
        self.connect_islands()
        return self.res

    def create_islands(self):
        self.islands = {}  # island_num: island_size
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0: continue
                self.add_island(start_i=i, start_j=j)

    def add_island(self, start_i, start_j):
        island_num = 2 + len(self.islands)
        island_size = 0
        stack = [(start_i, start_j)]
        while stack:
            curr_i, curr_j = stack.pop()
            if self.grid[curr_i][curr_j] != 1: continue
            island_size += 1
            self.grid[curr_i][curr_j] = island_num
            for next_i, next_j in ((curr_i-1, curr_j), (curr_i+1, curr_j), (curr_i, curr_j-1), (curr_i, curr_j+1)):
                if next_i < 0 or next_i >= self.m or next_j < 0 or next_j >= self.n or self.grid[next_i][next_j] != 1:
                    continue
                stack.append((next_i, next_j))
        self.islands[island_num] = island_size
        self.res = max(self.res, island_size)

    def connect_islands(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] != 0: continue
                self.proc_zero(i, j)

    def proc_zero(self, i, j):
        near_islands = set()
        for i1, j1 in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            if i1 < 0 or i1 >= self.m or j1 < 0 or j1 >= self.n or self.grid[i1][j1] == 0: continue
            near_islands.add(self.grid[i1][j1])
        size = 1 + sum(self.islands[island_num] for island_num in near_islands)
        self.res = max(self.res, size)


sln = Solution()
grid = [
    [1,0],
    [0,1]
]
print(sln.largestIsland(grid))  # Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

sln = Solution()
grid = [
    [1,1],
    [1,0]
]
print(sln.largestIsland(grid))  # Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

sln = Solution()
grid = [
    [1,1],
    [1,1]
]
print(sln.largestIsland(grid))  # Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.