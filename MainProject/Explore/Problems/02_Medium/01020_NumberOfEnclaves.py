# Medium 1020. Number of Enclaves
# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

class Solution:
    def numEnclaves(self, grid):
        self.grid = grid; self.M = len(grid); self.N = len(grid[0])  # M x N = rows x columns
        self.LAND = 1; self.WATER = 0; self.VISITED_LAND = 2
        land_cell_cnt = 0
        for row in self.grid: land_cell_cnt += sum(row)
        boundary_cell_cnt = 0
        for i0 in (0, self.M-1):
            for j0 in range(self.N):
                if self.grid[i0][j0] == self.LAND: boundary_cell_cnt += self.paint_boundary_island(i0, j0)
        for i0 in range(self.M):
            for j0 in (0, self.N-1):
                if self.grid[i0][j0] == self.LAND: boundary_cell_cnt += self.paint_boundary_island(i0, j0)
        return land_cell_cnt - boundary_cell_cnt

    def paint_boundary_island(self, i0, j0):
        cell_cnt = 0; stack = [(i0, j0)]
        while stack:
            i, j = stack.pop()
            if self.grid[i][j] != self.LAND: continue
            self.grid[i][j] = self.VISITED_LAND
            cell_cnt += 1
            for i1, j1 in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if i1 < 0 or i1 >= self.M or j1 < 0 or j1 >= self.N or self.grid[i1][j1] != self.LAND: continue
                stack.append((i1, j1))
        return cell_cnt

sln = Solution()
grid = [
    [0,0,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,0,0,0]
]
print(sln.numEnclaves(grid))

sln = Solution()
grid = [
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,0],
    [0,0,0,0]
]
print(sln.numEnclaves(grid))

sln = Solution()
grid = [
    [0,0,0,1,1,1,0,1,1,1,1,1,0,0,0],
    [1,1,1,1,0,0,0,1,1,0,0,0,1,1,1],
    [1,1,1,0,0,1,0,1,1,1,0,0,0,1,1],
    [1,1,0,1,0,1,1,0,0,0,1,1,0,1,0],
    [1,1,1,1,0,0,0,1,1,1,0,0,0,1,1],
    [1,0,1,1,0,0,1,1,1,1,1,1,0,0,0],
    [0,1,0,0,1,1,1,1,0,0,1,1,1,0,0],
    [0,0,1,0,0,0,0,1,1,0,0,1,0,0,0],
    [1,0,1,0,0,1,0,0,0,0,0,0,1,0,1],
    [1,1,1,0,1,0,1,0,1,1,1,0,0,1,0]
]
print(sln.numEnclaves(grid))