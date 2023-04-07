# Medium 1020. Number of Enclaves
# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

class Solution:
    def numEnclaves(self, grid):
        self.grid, self.M, self.N = grid, len(grid), len(grid[0])  # M x N = rows x columns
        self.LAND, self.WATER = 1, 0
        cell_cnt = 0
        for i0 in range(self.M):
            for j0 in range(self.N):
                if self.grid[i0][j0] == self.LAND: cell_cnt += self.paint_island(i0, j0)
        return cell_cnt

    def paint_island(self, i0, j0):
        is_closed, stack, ordered = True, [(i0, j0)], set([(i0, j0)])
        while stack:
            i, j = stack.pop()
            self.grid[i][j] = 2
            if i in (0, self.M-1) or j in (0, self.N-1): is_closed = False
            for i1, j1 in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                k = (i1, j1)
                if i1 < 0 or i1 >= self.M or j1 < 0 or j1 >= self.N or self.grid[i1][j1] != self.LAND or k in ordered:
                    continue
                stack.append(k)
                ordered.add(k)
        return len(ordered) if is_closed else 0

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