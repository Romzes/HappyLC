# Medium 221. Maximal Square
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

class Solution:
    def maximalSquare(self, matrix):
        self.matrix = matrix; self.M = len(matrix); self.N = len(matrix[0])
        self.MaxK = min(self.M, self.N)
        k = 1
        for m in range(self.M):
            find = self.find_square(k, m, self.N-1, pos='r')
            if find:
                k += 1
                if k > self.MaxK: break
        return (k-1)**2

    def find_square(self, k, m, n, pos):
        # pos = 'r' | 'c'
        if pos == 'r':
            for n1 in range(n-k+2):
                if self.is_square(m1=m-k+1, n1=n1, m2=m, n2=n1+k-1): return True
        elif pos == 'c':
            for m1 in range(m-k+2):
                if self.is_square(m1=m1, n1=n-k+1, m2=m1+k-1, n2=n): return True
        return False

    def is_square(self, m1, n1, m2, n2):
        for i in range(m1, m2+1):
            for j in range(n1, n2+1):
                if self.matrix[i][j] != '1': return False
        return True

sln = Solution()
matrix = [['0']]
print(sln.maximalSquare(matrix))

sln = Solution()
matrix = [['1']]
print(sln.maximalSquare(matrix))

sln = Solution()
matrix = [
    ['1','0','1','0','0'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','0','1','0']
]
print(sln.maximalSquare(matrix))

sln = Solution()
matrix = [
    ['0','1'],
    ['1','0']
]
print(sln.maximalSquare(matrix))


sln = Solution()
matrix = [
    ['1','0','1','1','1'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','0','1','0']
]
print(sln.maximalSquare(matrix))




