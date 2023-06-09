# Easy 1351 Count Negative Numbers in a Sorted Matrix
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
# return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid):
        m = len(grid); n = len(grid[0]); neg = 0; r = m-1; c = 0
        while True:
            if r < 0 or c >= n: return neg
            if grid[r][c] >= 0: c += 1
            else: neg += n-c; r -= 1

sln = Solution()
grid = [
    [ 4, 3, 2,-1],
    [ 3, 2, 1,-1],
    [ 1, 1,-1,-2],
    [-1,-1,-2,-3]
]
print(sln.countNegatives(grid))

sln = Solution()
grid = [
    [3,2],
    [1,0]
]
print(sln.countNegatives(grid))