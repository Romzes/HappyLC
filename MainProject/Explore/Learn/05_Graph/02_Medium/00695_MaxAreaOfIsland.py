# Medium 695. Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid):
        self.grid = grid; self.m = len(grid); self.n = len(grid[0])
        self.max_area = 0
        for i0 in range(self.m):
            for j0 in range(self.n):
                if grid[i0][j0] == 1: self.proc_one_island(i0, j0)
        return self.max_area

    def proc_one_island(self, i0, j0):
        stack = [(i0, j0)]
        area = 0
        while stack:
            i, j = stack.pop()
            if self.grid[i][j] != 1: continue
            self.grid[i][j] = -1
            area += 1
            for i1, j1 in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if not (0 <= i1 < self.m) or not (0 <= j1 < self.n) or self.grid[i1][j1] != 1: continue
                stack.append((i1, j1))
        self.max_area = max(self.max_area, area)


sln = Solution()
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(sln.maxAreaOfIsland(grid))

sln = Solution()
grid = [[0,0,0,0,0,0,0,0]]
print(sln.maxAreaOfIsland(grid))