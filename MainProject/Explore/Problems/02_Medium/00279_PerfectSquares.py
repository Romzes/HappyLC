"""
279 (Medium) Perfect Squares
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
Constraints:
  1 <= n <= 10^4
"""
from collections import OrderedDict
from functools import cache
class Solution:
    def numSquares(self, n: int) -> int:
        squares = OrderedDict()
        for k in range(1, int(n**0.5)+1): squares[k**2] = 0
        @cache
        def rec(m):
            if m in squares: return 1
            mn = float('+inf')
            for k2 in squares:
                d = m - k2
                if d <= 0: break
                mn = min(mn, rec(d))
            return 1 + mn
        return rec(n)

sln = Solution()
print(sln.numSquares(n=12))

sln = Solution()
print(sln.numSquares(n=13))