# 64 (Medium) Minimum Path Sum
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Constraints:
  m == grid.length
  n == grid[i].length
  1 <= m, n <= 200
  0 <= grid[i][j] <= 200
"""

from typing import List

# Runtime = 7 ms  Beats 99.50%  ;  Memory = 18.72 MB  Beats 94.37%
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row2 = n * [None]
        row2[n-1] = grid[m-1][n-1]
        for j in range(n-2, -1, -1): row2[j] = grid[m-1][j] + row2[j+1]
        if m == 1: return row2[0]
        row1 = n * [None]
        for i in range(m-2, -1, -1):
            row1[n-1] = grid[i][n-1] + row2[n-1]
            for j in range(n-2, -1, -1): row1[j] = grid[i][j] + min(row1[j+1], row2[j])
            if i == 0: return row1[0]
            row2, row1 = row1, row2


sln = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(sln.minPathSum(grid))  # Output: 7

sln = Solution()
grid = [[1,2,3],[4,5,6]]
print(sln.minPathSum(grid))  # Output: 12