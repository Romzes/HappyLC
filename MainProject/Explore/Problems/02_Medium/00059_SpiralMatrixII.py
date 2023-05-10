# Medium 59. Spiral Matrix II
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n):
        matrix = [n*[None] for _ in range(n)]
        i = j = 0
        vectors = ((0,1), (1,0), (0,-1), (-1,0)); vi = 0
        for k in range(1, n*n+1):
            matrix[i][j] = k
            i1, j1 = i + vectors[vi][0], j + vectors[vi][1]
            if 0 <= i1 < n and 0 <= j1 < n and matrix[i1][j1] is None:
                i, j = i1, j1
            else:
                vi = (vi + 1) % len(vectors)
                i, j = i + vectors[vi][0], j + vectors[vi][1]
        return matrix


sln = Solution()
print(sln.generateMatrix(n=3))

sln = Solution()
print(sln.generateMatrix(n=1))

