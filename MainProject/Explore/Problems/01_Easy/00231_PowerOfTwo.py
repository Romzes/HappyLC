"""
231 (Easy) Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.
Constraints:
  -2^31 <= n <= 2^31 - 1
"""
class Solution:
    max2 = 2**31
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and Solution.max2 % n == 0

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0

sln = Solution()
print(sln.isPowerOfTwo(n=1))

sln = Solution()
print(sln.isPowerOfTwo(n=16))

sln = Solution()
print(sln.isPowerOfTwo(n=3))