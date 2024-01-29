"""
51 (Hard) N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.
Constraints:
  1 <= n <= 9
"""
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.N = n; self.arr = n * [0]; i1 = j1 = 0
        while i1 != -1: i1, j1 = self.step(i1, j1)
        return self.res

    def step(self, i1, j1):
        self.arr[i1] = j1
        if j1 == self.N:
            i1 -= 1
            j1 = (self.arr[i1] + 1) if i1 >= 0 else None
            return i1, j1
        if self.is_valid(i1):
            if i1 == self.N-1:
                self.res.append(self.print_border())
                return i1, j1+1
            return i1+1, 0
        else:
            return i1, j1+1

    def is_valid(self, i1):
        j1 = self.arr[i1]
        for i in range(i1):
            j = self.arr[i]
            if j == j1 or i1-i == abs(j1-j): return False
        return True

    def print_border(self):
        border = [self.N * ['.'] for _ in range(self.N)]
        for i in range(self.N):
            border[i][self.arr[i]] = 'Q'
            border[i] = ''.join(border[i])
        return border

sln = Solution()
print(sln.solveNQueens(n=1))

sln = Solution()
print(sln.solveNQueens(n=2))

sln = Solution()
print(sln.solveNQueens(n=3))

sln = Solution()
print(sln.solveNQueens(n=4))

sln = Solution()
print(sln.solveNQueens(n=9))