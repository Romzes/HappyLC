# Easy 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# Constraints:
# 1 <= numRows <= 30

class Solution:
    def generate(self, numRows):
        res = [[1]]
        if numRows == 1: return res
        for r in range(1, numRows):
            prev = res[r-1]
            curr = (r+1) * [None]; curr[0] = curr[-1] = 1
            for i in range(1, r): curr[i] = prev[i-1] + prev[i]
            res.append(curr)
        return res

sln = Solution()
print(sln.generate(numRows=1))

sln = Solution()
print(sln.generate(numRows=2))

sln = Solution()
print(sln.generate(numRows=5))

