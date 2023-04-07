# Medium 1020. Number of Enclaves
# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

class Solution:
    def numEnclaves(self, grid):
        self.grid, self.M, self.N = grid, len(grid), len(grid[0])  # M x N = rows x columns
        self.m_edges, self.n_edges = (0, self.M-1), (0, self.N-1)
        self.LAND, self.WATER = 1, 0
        cell_cnt = 0
        for i0 in range(1, self.M-1):
            for j0 in range(1, self.N-1):
                if self.grid[i0][j0] == self.LAND: cell_cnt += self.paint_island(i0, j0)
        return cell_cnt

    def paint_island(self, i0, j0):
        cell_cnt, is_closed, stack = 0, True, [(i0, j0)]
        while stack:
            i, j = stack.pop()
            if self.grid[i][j] != self.LAND: continue
            self.grid[i][j] = 2
            cell_cnt += 1
            if is_closed and (i in self.m_edges or j in self.n_edges): is_closed = False
            for i1, j1 in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if i1 < 0 or i1 >= self.M or j1 < 0 or j1 >= self.N or self.grid[i1][j1] != self.LAND: continue
                stack.append((i1, j1))
        return cell_cnt if is_closed else 0

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