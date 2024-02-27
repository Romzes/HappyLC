"""
342 (Easy) Power of Four
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4^x.
Follow up: Could you solve it without loops/recursion ?
Constraints:
  -2^31 <= n <= 2^31 - 1
"""
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        d, r = divmod(2**30, n)
        if r != 0: return False
        e = d ** 0.5
        return e == int(e)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        m = n ** 0.5
        return m == int(m) and 2**30 % m == 0

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and 2**30 % n**0.5 == 0

sln = Solution()
print(sln.isPowerOfFour(n=16))

sln = Solution()
print(sln.isPowerOfFour(n=5))

sln = Solution()
print(sln.isPowerOfFour(n=1))
