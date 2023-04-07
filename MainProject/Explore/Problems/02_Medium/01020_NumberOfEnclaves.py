# Medium 1020. Number of Enclaves
# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

class Solution:
    def numEnclaves(self, grid):
        self.grid, self.M, self.N = grid, len(grid), len(grid[0])  # M x N = rows x columns
        self.LAND, self.WATER = 1, 0
        self.not_closed_islands, island_id = set(), 0
        for i0 in range(self.M):
            for j0 in range(self.N):
                if self.grid[i0][j0] != self.LAND: continue
                island_id -= 1
                self.paint_island(island_id, i0, j0)

        cell_cnt = 0
        for i0 in range(self.M):
            for j0 in range(self.N):
                v = self.grid[i0][j0]
                if v != self.WATER and v not in self.not_closed_islands:
                    cell_cnt += 1

        return cell_cnt


    def paint_island(self, island_id, i0, j0):
        stack, ordered = [(i0, j0)], set([(i0, j0)])
        while stack:
            i, j = stack.pop()
            self.grid[i][j] = island_id
            if i in (0, self.M-1) or j in (0, self.N-1): self.not_closed_islands.add(island_id)
            for i1, j1 in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                k = (i1, j1)
                if i1 < 0 or i1 >= self.M or j1 < 0 or j1 >= self.N or self.grid[i1][j1] != self.LAND or k in ordered:
                    continue
                stack.append(k)
                ordered.add(k)

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