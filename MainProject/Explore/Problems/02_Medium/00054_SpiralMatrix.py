# Medium 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix); n = len(matrix[0]); cnt = m*n; res = cnt * [None]; i = j = 0
        vectors = ((0,1), (1,0), (0,-1), (-1,0)); vi = 0
        for k in range(cnt):
            res[k] = matrix[i][j]
            matrix[i][j] = float('inf')
            v = vectors[vi]
            i1, j1 = i + v[0], j + v[1]
            if 0 <= i1 < m and 0 <= j1 < n and matrix[i1][j1] != float('inf'):
                i, j = i1, j1
            else:
                vi = (vi + 1) % len(vectors)
                v = vectors[vi]
                i, j = i + v[0], j + v[1]
        return res

sln = Solution()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(sln.spiralOrder(matrix))

sln = Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
print(sln.spiralOrder(matrix))
