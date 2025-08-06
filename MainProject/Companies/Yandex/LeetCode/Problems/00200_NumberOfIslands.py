from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid, self.M, self.N = grid, len(grid), len(grid[0])  # grid = M x N
        cnt = 0
        for r in range(self.M):
            for c in range(self.N):
                if grid[r][c] == '1':
                    self.paint_island(r0=r, c0=c)
                    cnt += 1
        return cnt

    def paint_island(self, r0, c0):
        stack = [(r0, c0)]
        while stack:
            r1, c1 = stack.pop()
            if self.grid[r1][c1] != '1': continue
            self.grid[r1][c1] = '#'
            for r2, c2 in (r1+1, c1), (r1-1, c1), (r1, c1+1), (r1, c1-1):
                if 0 <= r2 < self.M and 0 <= c2 < self.N and self.grid[r2][c2] == '1':
                    stack.append((r2, c2))

sln = Solution()  # Example 1
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(sln.numIslands(grid))  # Output: 1

sln = Solution()  # Example 2
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sln.numIslands(grid))  # Output: 3
