# Medium 1254. Number of Closed Islands
# Given a 2D grid consists of 0s (land) and 1s (water).
# An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
# Return the number of closed islands.

class Solution:
    def closedIsland(self, grid):
        self.grid, self.M, self.N = grid, len(grid), len(grid[0])  # M x N = rows x columns
        self.LAND, self.WATER = 0, 1
        closed_cnt = 0
        for i0 in range(self.M):
            for j0 in range(self.N):
                if self.grid[i0][j0] == self.LAND: closed_cnt += self.paint_island(i0, j0)
        return closed_cnt

    def paint_island(self, i0, j0):
        is_closed, stack, ordered = 1, [(i0, j0)], set([(i0, j0)])
        while stack:
            i, j = stack.pop()
            self.grid[i][j] = 2
            if i in (0, self.M-1) or j in (0, self.N-1): is_closed = 0
            for i1, j1 in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                k = (i1, j1)
                if i1 < 0 or i1 >= self.M or j1 < 0 or j1 >= self.N or self.grid[i1][j1] != self.LAND or k in ordered:
                    continue
                stack.append(k)
                ordered.add(k)
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