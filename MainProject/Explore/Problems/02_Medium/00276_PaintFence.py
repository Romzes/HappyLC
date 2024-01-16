"""
276. (Medium) Paint Fence
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:
  Every post must be painted exactly one color.
  There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.
Constraints:
  1 <= n <= 50
  1 <= k <= 10^5
  The testcases are generated such that the answer is in the range [0, 2^31 - 1] for the given n and k.

"""

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n <= 2: return k**n
        dp1 = (n-2)*[None]  # кол-во вариантов покрасить [0,1,...i] при условии: i+1, i+2 покрашены в разные цвета
        dp2 = (n-2)*[None]  # кол-во вариантов покрасить [0,1,...i] при условии: i+1, i+2 покрашены в один цвет
        dp1[0] = k; dp2[0] = k-1
        for i in range(1, n-2):
            dp1[i] = dp2[i-1] + (k-1) * dp1[i-1]
            dp2[i] = (k-1) * dp1[i-1]
        return (k**2-k) * dp1[-1] + k * dp2[-1]

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n <= 2: return k**n
        dp1, dp2 = k, k-1
        for i in range(n-3): dp1, dp2 = (k-1) * dp1 + dp2, (k-1) * dp1
        return (k**2-k) * dp1 + k * dp2

sln = Solution()
print(sln.numWays(n=3, k=2))

sln = Solution()
print(sln.numWays(n=1, k=1))

sln = Solution()
print(sln.numWays(n=7, k=2))