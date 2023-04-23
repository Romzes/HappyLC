# Medium 120. Triangle
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle); curr = triangle[-1]
        for r in range(n-2, -1, -1):
            for i, t in enumerate(triangle[r]): curr[i] = t + min(curr[i], curr[i+1])
        return curr[0]

sln = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(sln.minimumTotal(triangle))

sln = Solution()
triangle = [[-10]]
print(sln.minimumTotal(triangle))


