"""
50 (Medium) Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
Constraints:
  -100.0 < x < 100.0
  -2^31 <= n <= 2^31-1
  n is an integer.
  Either x is not zero or n > 0.
  -10^4 <= x^n <= 10^4
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: x = 1/x; n = -n
        p = b = 1
        while b <= n:
            if n & b: p *= x
            b <<= 1; x *= x
        return p

sln = Solution()
print(sln.myPow(x=2, n=10))

sln = Solution()
print(sln.myPow(x=2.1, n=3))

sln = Solution()
print(sln.myPow(x=2, n=-2))