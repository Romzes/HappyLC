# 51 (Hard) N-Queens
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Constraints:
  1 <= n <= 9
"""

from typing import List

# Runtime = 9ms  Beats 82.13%  ;  Memory = 18.05 MB  Beats 95.99%
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.queens = []  # = [0,4,7] номера столбцов для каждой строки (строки нумеруются сверху)
        self.columns = n * [False]
        self.diags1 = (2*n-1) * [False]  # -(n-1) <= c-r <= (n-1) параллельны главной диагонали
        self.diags2 = (2*n-1) * [False]  #      0 <= c+r <= 2*n-1 параллельны побочной диагонали
        self.res_list = []
        self.backtrack()
        return self.res_list

    def backtrack(self):
        if len(self.queens) == self.n:
            self.res_list.append(self.create_board())
            return
        r = len(self.queens)
        for c in range(self.n):
            d1, d2 = c-r + (self.n-1), c+r
            if self.columns[c] or self.diags1[d1] or self.diags2[d2]: continue
            self.queens.append(c)
            self.columns[c] = self.diags1[d1] = self.diags2[d2] = True
            self.backtrack()
            self.queens.pop()
            self.columns[c] = self.diags1[d1] =self.diags2[d2] = False

    def create_board(self):
        board = self.n * [None]
        for r in range(self.n):
            row = self.n * ['.']
            row[self.queens[r]] = 'Q'
            board[r] = ''.join(row)
        return board


sln = Solution()
print(sln.solveNQueens(n=4))
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

sln = Solution()
print(sln.solveNQueens(n=1))
# Output: [["Q"]]

sln = Solution()
# print(sln.solveNQueens(n=9))
