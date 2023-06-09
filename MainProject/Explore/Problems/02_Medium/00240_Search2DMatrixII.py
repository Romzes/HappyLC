# Easy 240. Search a 2D Matrix II
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#   Integers in each row are sorted in ascending from left to right.
#   Integers in each column are sorted in ascending from top to bottom.

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix); n = len(matrix[0]); r = m-1; c = 0
        while True:
            if r < 0 or c >= n: return False
            v = matrix[r][c]
            if v == target: return True
            if v < target: c += 1
            else: r -=1

sln = Solution()
matrix = [
    [ 1,  4,  7, 11, 15],
    [ 2,  5,  8, 12, 19],
    [ 3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
print(sln.searchMatrix(matrix, target=5))

sln = Solution()
matrix = [
    [ 1,  4,  7, 11, 15],
    [ 2,  5,  8, 12, 19],
    [ 3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
print(sln.searchMatrix(matrix, target=20))