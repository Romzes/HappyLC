# Medium 1091. Shortest Path in Binary Matrix
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
# If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
#   All the visited cells of the path are 0.
#   All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[-1][-1] != 0: return -1
        M = len(grid); N = len(grid[0])  # grid = M x N
        if M*N == 1: return 1
        dirs = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        level = 1; cells = [(M-1, N-1)]; grid[M-1][N-1] = 2
        while cells:
            next_cells = []
            for r, c in cells:
                for dr, dc in dirs:
                    r1, c1 = r+dr, c+dc
                    if r1 < 0 or r1 >= M or c1 < 0 or c1 >= N: continue
                    if grid[r1][c1] != 0: continue
                    if r1 == 0 and c1 == 0: return level + 1
                    grid[r1][c1] = 2
                    next_cells.append((r1, c1))
            level, cells = level + 1, next_cells
        return -1

sln = Solution()
grid = [
    [0,1],
    [1,0]
]
print(sln.shortestPathBinaryMatrix(grid))

sln = Solution()
grid = [
    [0,0,0],
    [1,1,0],
    [1,1,0]
]
print(sln.shortestPathBinaryMatrix(grid))

sln = Solution()
grid = [
    [1,0,0],
    [1,1,0],
    [1,1,0]
]
print(sln.shortestPathBinaryMatrix(grid))

sln = Solution()
grid = [
    [0,0,0],
    [1,1,0],
    [1,1,1]
]
print(sln.shortestPathBinaryMatrix(grid))

