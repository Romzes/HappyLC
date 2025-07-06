# 52 (Hard) N-Queens II
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Constraints:
  1 <= n <= 9
"""

# Runtime = 8ms  Beats 68.50%  ;  Memory = 17.89 MB  Beats 44.00%
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.queens = []  # = [0,4,7] номера столбцов для каждой строки (строки нумеруются сверху)
        self.columns = n * [False]
        self.diags1 = (2 * n - 1) * [False]  # -(n-1) <= c-r <= (n-1) параллельны главной диагонали
        self.diags2 = (2 * n - 1) * [False]  # 0 <= c+r <= 2*n-1 параллельны побочной диагонали
        self.res = 0
        self.backtrack()
        return self.res

    def backtrack(self):
        r = len(self.queens)
        for c in range(self.n):
            d1, d2 = c - r + (self.n - 1), c + r
            if self.columns[c] or self.diags1[d1] or self.diags2[d2]: continue
            if len(self.queens) == self.n-1:
                self.res += 1
                return
            self.queens.append(c)
            self.columns[c] = self.diags1[d1] = self.diags2[d2] = True
            self.backtrack()
            self.queens.pop()
            self.columns[c] = self.diags1[d1] = self.diags2[d2] = False


sln = Solution()
print(sln.totalNQueens(n=4))  # Output: 2

sln = Solution()
print(sln.totalNQueens(n=1))  # Output: 1

sln = Solution()
print(sln.totalNQueens(n=9))  # Output: 352