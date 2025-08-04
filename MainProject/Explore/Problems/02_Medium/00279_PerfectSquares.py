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
        for k in range(int(n**0.5), 0, -1): squares[k**2] = None
        @cache
        def rec(m):
            if m in squares: return 1
            mn = float('+inf')
            for k2 in squares:
                d = m - k2
                if d < 0: continue
                mn = min(mn, rec(d))
            return 1 + mn
        return rec(n)

class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_n = int(n**0.5)
        if n == sqrt_n**2: return 1
        self.squares = OrderedDict()
        for k in range(sqrt_n, 0, -1): self.squares[k**2] = None
        self.dp = {k2: 1 for k2 in self.squares}
        self.res = float('+inf')
        self.n = n
        self.rec(m=n, cnt=0)
        return self.res

    def rec(self, m, cnt):
        if m in self.dp: return self.dp[m]
        if self.res <= cnt: return float('+inf')
        mn = float('+inf')
        for k2 in self.squares:
            d = m - k2
            if d < 0: continue
            mn = min(mn, 1 + self.rec(d, cnt+1))
            if m == self.n and mn < float('+inf'): self.res = min(self.res, mn)
        if mn < float('+inf'): self.dp[m] = mn
        return mn

class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_n = int(n**0.5)
        if n == sqrt_n**2: return 1
        squares = OrderedDict()
        for k in range(1, sqrt_n+1): squares[k**2] = None
        curr_level = set([n]); cnt = 0
        while True:
            cnt += 1
            next_level = set()
            for v in curr_level:
                if v in squares: return cnt
                for k2 in squares:
                    d = v - k2
                    if d > 0: next_level.add(d)
                    else: break
            curr_level = next_level


# НЕПРАВИЛЬНОЕ РЕШЕНИЕ - самый большой квадрат
class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_n = int(n ** 0.5)  # sqrt_n ** 2 <= n
        if sqrt_n ** 2 == n: return 1
        squares = [k**2 for k in range(sqrt_n, 0, -1)]
        rest = n
        i = 0
        cnt = 0
        while rest > 0:
            cnt += 1
            while rest < squares[i]: i += 1
            rest -= squares[i]
        return cnt


sln = Solution()
print(sln.numSquares(n=1))

sln = Solution()
print(sln.numSquares(n=12))  # 12 = 9+1+1+1 = 4+4+4  => самое большой квадрат выбирать не всегда правильно

sln = Solution()
print(sln.numSquares(n=13))