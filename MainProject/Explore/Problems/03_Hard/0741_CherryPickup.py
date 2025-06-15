"""
741 (Hard) Cherry Pickup
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.
  0 means the cell is empty, so you can pass through,
  1 means the cell contains a cherry that you can pick up and pass through, or
  -1 means the cell contains a thorn that blocks your way.

Return the maximum number of cherries you can collect by following the rules below:
  Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
  After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
  When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
  If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.

Constraints:
  n == grid.length
  n == grid[i].length
  1 <= n <= 50
  grid[i][j] is -1, 0, or 1.
  grid[0][0] != -1
  grid[n-1][n-1] != -1
"""
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.init_grid(grid)
        cnt1 = self.path1(grid)
        if cnt1 == float('-inf'): return 0
        return cnt1 + self.path2(grid)

    def init_grid(self, grid):
        M = len(grid); N = len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == -1: grid[i][j] = float('-inf')

    def path1(self, grid):
        M = len(grid); N = len(grid[0])
        dp = [N*[None] for _ in range(M)]
        for i in range(M):
            for j in range(N): dp[i][j] = [0, True]  # True right, False down
        s = 0
        for j in range(N-1, -1, -1): dp[-1][j][0] = (s := s + grid[-1][j])
        for i in range(M-2, -1, -1):
            # dp[i+1] -> dp[i]
            for j in range(N-1, -1, -1):
                r = dp[i][j+1][0] if j < N-1 else float('-inf')
                d = dp[i+1][j][0]
                dp[i][j][0], dp[i][j][1] = grid[i][j] + max(r, d), r >= d
        cnt1 = dp[0][0][0]
        if cnt1 > 0:
            i, j = 0, 0
            while i != M-1 or j != N:
                grid[i][j] = 0
                if dp[i][j][1]: j += 1
                else: i += 1
        return cnt1

    def path2(self, grid):
        M = len(grid); N = len(grid[0])
        dp = [N * [0] for _ in range(M)]
        s = 0
        for j in range(N): dp[0][j] = (s := s + grid[0][j])
        for i in range(1, M):
            # dp[i-1] -> dp[i]
            for j in range(N):
                l = dp[i][j-1] if 0 < j else float('-inf')
                dp[i][j] = grid[i][j] + max(l, dp[i-1][j])
        return dp[-1][-1]


sln = Solution()
grid = [
    [1,1,1,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,1],
    [1,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,1,1,1]
]
print(sln.cherryPickup(grid))

sln = Solution()
grid = [
    [0,1,-1],
    [1,0,-1],
    [1,1,1]
]
print(sln.cherryPickup(grid))

sln = Solution()
grid = [
    [1,1,-1],
    [1,-1,1],
    [-1,1,1]
]
print(sln.cherryPickup(grid))
