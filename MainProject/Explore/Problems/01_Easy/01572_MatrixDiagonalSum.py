# Easy 1572. Matrix Diagonal Sum
# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat):
        n = len(mat); s = 0
        for i in range(n): s += mat[i][i] + mat[i][n-1-i]
        k, r = divmod(n, 2)
        if r == 1: s -= mat[k][k]
        return s

sln = Solution()
mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(sln.diagonalSum(mat))

sln = Solution()
mat = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
]
print(sln.diagonalSum(mat))

sln = Solution()
mat = [[5]]
print(sln.diagonalSum(mat))