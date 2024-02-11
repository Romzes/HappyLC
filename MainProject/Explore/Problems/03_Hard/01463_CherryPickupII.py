"""
1463 (Hard) Cherry Pickup II
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.
You have two robots that can collect cherries for you:
  Robot #1 is located at the top-left corner (0, 0), and
  Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:
  From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
  When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
  When both robots stay in the same cell, only one takes the cherries.
  Both robots cannot move outside of the grid at any moment.
  Both robots should reach the bottom row in grid.
Constraints:
  rows == grid.length
  cols == grid[i].length
  2 <= rows, cols <= 70
  0 <= grid[i][j] <= 100
"""
from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        M = len(grid); N = len(grid[0])
        pos1 = [N*[0] for _ in range(N-1)]
        pos2 = [N*[0] for _ in range(N-1)]
        for i1 in range(N-1):
            for i2 in range(i1+1, N):
                pos1[i1][i2] = grid[-1][i1] + grid[-1][i2]
        steps = [(d1, d2) for d2 in (-1, 0, 1) for d1 in (-1, 0, 1)]
        for m in range(M-2, -1, -1):
            # pos1 -> pos2
            for i1 in range(N-1):
                for i2 in range(i1+1, N):
                    mx = 0
                    for s in steps:
                        j1 = i1 + s[0]; j2 = i2 + s[1]
                        if 0 <= j1 < N and 0 <= j2 < N and j1 < j2:
                            mx = max(mx, pos1[j1][j2])
                    pos2[i1][i2] = grid[m][i1] + grid[m][i2] + mx
            pos1, pos2 = pos2, pos1
        return pos1[0][N-1]


# Runtime 252 ms , Beats 100.00 %of users with Python3
# Memory 16.74 MB , Beats 100.00% of users with Python3
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        M = len(grid); N = len(grid[0])
        b1 = min(N-2, M-1)
        b2 = max(1, N-M)
        pos1 = [N*[None] for _ in range(b1+1)]
        pos2 = [N*[None] for _ in range(b1+1)]
        for i1 in range(b1+1):
            for i2 in range(max(i1+1, b2), N):
                pos1[i1][i2] = grid[-1][i1] + grid[-1][i2]
        steps = [(d1, d2) for d2 in (-1, 0, 1) for d1 in (-1, 0, 1)]
        for m in range(M-2, -1, -1):
            # row[m+1] = pos1 -> pos2 = row[m]
            b1 = min(N-2, m); b2 = max(1, N-1-m)  # borders for pos2 = row[m]
            for i1 in range(b1+1):
                for i2 in range(max(i1+1, b2), N):
                    # (i1, i2) pos2 = row[m]
                    mx = 0
                    for s in steps:
                        j1 = i1 + s[0]; j2 = i2 + s[1]
                        # if 0 <= j1 < j2 < N: mx = max(mx, pos1[j1][j2])
                        if 0 <= j1 < j2 < N and mx < pos1[j1][j2]: mx = pos1[j1][j2]  # важная оптимизация: убираем max(..)
                    pos2[i1][i2] = grid[m][i1] + grid[m][i2] + mx
            pos1, pos2 = pos2, pos1
        return pos1[0][N-1]


sln = Solution()
grid = [
    [3,1,1],
    [2,5,1],
    [1,5,5],
    [2,1,1]
]
print(sln.cherryPickup(grid))

sln = Solution()
grid = [
    [1,0,0,0,0,0,1],
    [2,0,0,0,0,3,0],
    [2,0,9,0,0,0,0],
    [0,3,0,5,4,0,0],
    [1,0,2,3,0,0,6]
]
print(sln.cherryPickup(grid))