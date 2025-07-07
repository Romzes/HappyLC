# 73 (Medium) Set Matrix Zeroes
"""
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
"""

from typing import List

# Runtime = 3ms  Beats 69.53%  ;  Memory = 18.19MB  Beats 99.46%
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            if 0 not in matrix[r]: continue
            for c in range(n):
                if matrix[r][c] != 0: matrix[r][c] = '#'

        for c in range(n):
            for r in range(m):
                if matrix[r][c] == 0:
                    for r1 in range(m): matrix[r1][c] = 0
                    break

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '#': matrix[r][c] = 0



sln = Solution()
matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
sln.setZeroes(matrix)
print(matrix)
""" Output
[
    [1,0,1],
    [0,0,0],
    [1,0,1]
]
"""

sln = Solution()
matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
sln.setZeroes(matrix)
print(matrix)
""" Output
[
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
]
"""
