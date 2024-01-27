"""
629 (Hard) K Inverse Pairs Array
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].
Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.
Since the answer can be huge, return it modulo 10^9 + 7.
Constraints:
  1 <= n <= 1000
  0 <= k <= 1000
"""
from functools import cache
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # наивное решение
        @cache
        def rec(n, k):
            if n == 1: return int(k == 0)
            if k < 0: return 0
            if k == 0: return 1
            # n > 1 , k > 0
            return sum( rec(n-1, k-i) for i in range(min(n, k+1)) )
        return rec(n, k) % (10**9 + 7)

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def rec(n, k):
            if n == 1: return int(k == 0)
            if k < 0: return 0
            if k == 0: return 1
            # n > 1 , k > 0
            return rec(n-1, k) + rec(n, k-1) - rec(n-1, k-n)
        return rec(n, k) % (10**9 + 7)

sln = Solution()
print(sln.kInversePairs(n=3, k=0))

sln = Solution()
print(sln.kInversePairs(n=3, k=1))