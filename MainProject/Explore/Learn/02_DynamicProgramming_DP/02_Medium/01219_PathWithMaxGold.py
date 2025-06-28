# 1219 (Medium) Path with Maximum Gold
"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
Return the maximum amount of gold you can collect under the conditions:
(+) Every time you are located in a cell you will collect all the gold in that cell.
(+) From your position, you can walk one step to the left, right, up, or down.
(+) You can't visit the same cell more than once.
(+) Never visit a cell with 0 gold.
(+) You can start and stop collecting gold from any position in the grid that has some gold.

Constraints:
  m == grid.length
  n == grid[i].length
  1 <= m, n <= 15
  0 <= grid[i][j] <= 100
  There are at most 25 cells containing gold.
"""

from typing import List

# без кэширования промежуточных результатов
# Runtime = 3928 ms  Beats 26.68%  ;  Memory = 17.81 MB  Beats 52.11%
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold, self.grid, self.m, self.n = 0, grid, len(grid), len(grid[0])
        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c] == 0: continue
                max_gold = max(max_gold, self.find_path_max_gold(r, c))
        return max_gold

    def find_path_max_gold(self, r, c):
        # backtracking
        if not(0 <= r < self.m and 0 <= c < self.n) or self.grid[r][c] == 0: return 0
        curr_gold, self.grid[r][c] = self.grid[r][c], 0
        max_gold = curr_gold + max(self.find_path_max_gold(r1, c1) for r1, c1 in ((r-1, c), (r, c+1), (r+1, c), (r, c-1)))
        self.grid[r][c] = curr_gold
        return max_gold


sln = Solution()
grid = [[0,6,0],[5,8,7],[0,9,0]]
print(sln.getMaximumGold(grid))  # Output: 24
""" Explanation:
[0,6,0]
[5,8,7]
[0,9,0]
Path to get the maximum gold, 9 -> 8 -> 7
"""

sln = Solution()
grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
print(sln.getMaximumGold(grid))  # Output: 28
""" Explanation:
[1,0, 7]
[2,0, 6]
[3,4, 5]
[0,3, 0]
[9,0,20]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
"""