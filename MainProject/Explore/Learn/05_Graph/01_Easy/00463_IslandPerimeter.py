# Easy 463. Island Perimeter
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.

### DFS
class Solution:
    def islandPerimeter(self, grid):
        self.grid = grid; self.m = len(grid); self.n = len(grid[0])
        for i0 in range(self.m):
            for j0 in range(self.n):
                if grid[i0][j0] == 1: return self.calc_island_perimeter(i0, j0)
        return 0

    def calc_island_perimeter(self, i0, j0):
        stack = [(i0, j0)]
        perim = 0
        while stack:
            i, j = stack.pop()
            if self.grid[i][j] != 1: continue
            self.grid[i][j] = -1
            for i1, j1 in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if i1 in (-1, self.m) or j1 in (-1, self.n) or self.grid[i1][j1] == 0:
                    perim += 1
                elif self.grid[i1][j1] == 1:
                    stack.append((i1, j1))
        return perim

class Solution:
    def islandPerimeter(self, grid):
        m = len(grid); n = len(grid[0]); perim = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                if j == 0 or grid[i][j-1] == 0: perim += 1
                if j == n-1 or grid[i][j+1] == 0: perim += 1
                if i == 0 or grid[i-1][j] == 0: perim += 1
                if i == m-1 or grid[i+1][j] == 0: perim += 1
        return perim

sln = Solution()
grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
print(sln.islandPerimeter(grid))

sln = Solution()
grid = [[1]]
print(sln.islandPerimeter(grid))

sln = Solution()
grid = [[1,0]]
print(sln.islandPerimeter(grid))