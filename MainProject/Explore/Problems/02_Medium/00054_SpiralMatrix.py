# Medium 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix); n = len(matrix[0]); cnt = m*n; res = cnt * [None]; i = j = 0
        vectors = ((0,1), (1,0), (0,-1), (-1,0)); vi = 0
        for k in range(cnt):
            res[k] = matrix[i][j]
            matrix[i][j] = float('inf')
            i1, j1 = i + vectors[vi][0], j + vectors[vi][1]
            if 0 <= i1 < m and 0 <= j1 < n and matrix[i1][j1] != float('inf'):
                i, j = i1, j1
            else:
                vi = (vi + 1) % len(vectors)
                i, j = i + vectors[vi][0], j + vectors[vi][1]
        return res

class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix); n = len(matrix[0]); cnt = m*n; res = cnt * [None]
        r1, r2, c1, c2 = 0, m-1, 0, n-1
        r, c = 0, 0
        dirs = ((0,1), (1,0), (0,-1), (-1,0))  # (delta_col, delta_row)
        i = 0
        deltas = ((1,0,0,0), (0,0,0,-1), (0,-1,0,0), (0,0,1,0))
        for k in range(cnt):
            res[k] = matrix[r][c]
            dir = dirs[i]
            if not (r1 <= r + dir[0] <= r2 and c1 <= c + dir[1] <= c2):
                dlt = deltas[i]
                r1 += dlt[0]; r2 += dlt[1]; c1 += dlt[2]; c2 += dlt[3]
                i = (i + 1) % 4
                dir = dirs[i]
            r += dir[0]
            c += dir[1]
        return res


sln = Solution()
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(sln.spiralOrder(matrix))  # Output: [1,2,3,6,9,8,7,4,5]

sln = Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
print(sln.spiralOrder(matrix))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
