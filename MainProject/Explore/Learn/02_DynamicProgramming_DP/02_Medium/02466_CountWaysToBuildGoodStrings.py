# Medium 2466. Count Ways To Build Good Strings
# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:
#   Append the character '0' zero times.
#   Append the character '1' one times.
# This can be performed any number of times.
# A good string is a string constructed by the above process having a length between low and high (inclusive).
# Return the number of different good strings that can be constructed satisfying these properties.
# Since the answer can be large, return it modulo 10^9 + 7.

from functools import lru_cache

##### Recursive
class Solution:
    def countGoodStrings(self, low, high, zero, one):
        mod = int(10**9 + 7)
        @lru_cache
        def count(i):
            if high < i: return 0
            return ((1 if low <= i else 0) + count(i+zero) + count(i+one)) % mod

        return count(i=0)

##### Iterative
class Solution:
    def countGoodStrings(self, low, high, zero, one):
        dp = (high + 1 + max(zero, one)) * [0]; mod = int(10**9 + 7)
        for i in range(high, -1, -1):
            dp[i] = (1 if low <= i else 0) + dp[i+zero] + dp[i+one]
        return dp[0] % mod

sln = Solution()
print(sln.countGoodStrings(low=3, high=3, zero=1, one=1))

sln = Solution()
print(sln.countGoodStrings(low=2, high=3, zero=1, one=2))