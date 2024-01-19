"""
931 (Medium) Minimum Falling Path Sum
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
Constraints:
  n == matrix.length == matrix[i].length
  1 <= n <= 100
  -100 <= matrix[i][j] <= 100
"""
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(n-2, -1, -1):
            row1, row2 = matrix[i], matrix[i+1]
            for j in range(n):
                row1[j] += min(row2[k] for k in range(max(j-1, 0), min(j+2, n)))
        return min(matrix[0])

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Runtime = 93 ms , Beats 100.00% of users with Python3
        n = len(matrix)
        for i in range(n-2, -1, -1):
            row1, row2 = matrix[i], matrix[i+1]
            row1[0] += min(row2[0], row2[1])
            row1[n-1] += min(row2[n-2], row2[-1])
            for j in range(1, n-1):
                row1[j] += min(row2[j-1], row2[j], row2[j+1])
        return min(matrix[0])

sln = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(sln.minFallingPathSum(matrix))

sln = Solution()
matrix = [[-19,57],[-40,-5]]
print(sln.minFallingPathSum(matrix))