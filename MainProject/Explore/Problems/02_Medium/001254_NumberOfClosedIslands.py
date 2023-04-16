# Medium 1254. Number of Closed Islands
# Given a 2D grid consists of 0s (land) and 1s (water).
# An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.

class Solution:
    def closedIsland(self, grid):
        self.grid = grid; self.M = len(grid); self.N = len(grid[0])  # M x N = rows x columns
        self.m_edges = (0, self.M-1); self.n_edges = (0, self.N-1)
        self.LAND = 0; self.WATER = 1; self.VISITED_LAND = 2
        closed_cnt = 0
        for i0 in range(1, self.M-1):
            for j0 in range(1, self.N-1):
                if self.grid[i0][j0] == self.LAND: closed_cnt += self.paint_island(i0, j0)
        return closed_cnt

    def paint_island(self, i0, j0):
        is_closed = True; stack = [(i0, j0)]
        while stack:
            i, j = stack.pop()
            if self.grid[i][j] != self.LAND: continue
            self.grid[i][j] = self.VISITED_LAND
            if is_closed and (i in self.m_edges or j in self.n_edges): is_closed = False
            for i1, j1 in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if i1 < 0 or i1 >= self.M or j1 < 0 or j1 >= self.N or self.grid[i1][j1] != self.LAND: continue
                stack.append((i1, j1))
        return is_closed

sln = Solution()
grid = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
]
print(sln.closedIsland(grid))

sln = Solution()
grid = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0]
]
print(sln.closedIsland(grid))

sln = Solution()
grid = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,0,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]
]
print(sln.closedIsland(grid))