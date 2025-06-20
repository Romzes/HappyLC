# 48 (Medium) Rotate Image
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.72 MB  Beats 66.88%
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.
        a1, a2 = 0, len(matrix)-1
        while a1 < a2:
            for a in range(a1, a2):
                d = a - a1
                matrix[a][a2], matrix[a2][a2-d], matrix[a2-d][a1], matrix[a1][a] =\
                    matrix[a1][a], matrix[a][a2], matrix[a2][a2-d], matrix[a2-d][a1]
            a1 += 1
            a2 -= 1


sln = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sln.rotate(matrix)
print(matrix)  # Output: [[7,4,1],[8,5,2],[9,6,3]]

sln = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sln.rotate(matrix)
print(matrix)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]