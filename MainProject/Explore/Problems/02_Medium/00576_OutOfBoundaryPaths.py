"""
576 (Medium) Out of Boundary Paths
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary).
You can apply at most maxMove moves to the ball.
Given the five integers m, n, maxMove, startRow, startColumn,
return the number of paths to move the ball out of the grid boundary.
Since the answer can be very large, return it modulo 10^9 + 7.
Constraints:
  1 <= m, n <= 50
  0 <= maxMove <= 50
  0 <= startRow < m
  0 <= startColumn < n
"""

# Runtime = 55 ms , Beats 100.00% of users with Python3
# Memory = 22.54 MB , Beats 35.26% of users with Python3
from functools import cache
class Solution1:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def rec(i, j, maxMove):
            if i == -1 or i == m or j == -1 or j == n: return 1
            if maxMove == 0: return 0
            maxMove -= 1
            return rec(i-1, j, maxMove) + rec(i+1, j, maxMove) + rec(i, j-1, maxMove) + rec(i, j+1, maxMove)
        return rec(startRow, startColumn, maxMove) % (10**9 + 7)

# Runtime = 81 ms , Beats 80.92% of users with Python3
# Memory = 16.94 MB , Beats 89.88% of users with Python3
class Solution2:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0: return 0
        if maxMove == 1: return (startRow == 0) + (startRow == m-1) + (startColumn == 0) + (startColumn == n-1)
        b1 = self.create_board(m, n); b2 = self.create_board(m, n)
        for k in range(maxMove-1):
            for i in range(1, m+1):
                for j in range(1, n+1):
                    b2[i][j] = b1[i-1][j] + b1[i+1][j] + b1[i][j-1] + b1[i][j+1]
            b1, b2 = b2, b1
        i, j = startRow+1, startColumn+1
        res = b1[i-1][j] + b1[i+1][j] + b1[i][j-1] + b1[i][j+1]
        return res % (10**9 + 7)

    def create_board(self, m, n):
        b = [(n+2)*[0] for _ in range(m+2)]
        for j in range(n+2): b[0][j] = b[-1][j] = 1  # 2 крайних строки
        for i in range(m+2): b[i][0] = b[i][-1] = 1  # 2 крайних столбца
        return b

# Runtime = 62 ms , Beats 99.13% of users with Python3
# Memory = 16.93 MB , Beats 91.04% of users with Python3
class Solution3:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow - maxMove > 0 and startRow + maxMove < m and \
                startColumn - maxMove > 0 and startColumn + maxMove < n:
            return 0
        if maxMove == 1: return (startRow == 0) + (startRow == m-1) + (startColumn == 0) + (startColumn == n-1)
        b1 = self.create_board(m, n); b2 = self.create_board(m, n)
        i1, i2 = startRow + 1 - maxMove, startRow + 1 + maxMove
        j1, j2 = startColumn + 1 - maxMove, startColumn + 1 + maxMove
        for k in range(maxMove):
            i1 += 1; i2 -= 1; j1 += 1; j2 -= 1;
            for i in range(max(1, i1), min(m, i2)+1):
                for j in range(max(1, j1), min(n, j2)+1):
                    b2[i][j] = b1[i-1][j] + b1[i+1][j] + b1[i][j-1] + b1[i][j+1]
            b1, b2 = b2, b1
        return b1[startRow+1][startColumn+1] % (10**9 + 7)

    def create_board(self, m, n):
        b = [(n+2)*[0] for _ in range(m+2)]
        for j in range(n+2): b[0][j] = b[-1][j] = 1  # 2 крайних строки
        for i in range(m+2): b[i][0] = b[i][-1] = 1  # 2 крайних столбца
        return b


Solution = Solution3

sln = Solution()
print(sln.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))

sln = Solution()
print(sln.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))