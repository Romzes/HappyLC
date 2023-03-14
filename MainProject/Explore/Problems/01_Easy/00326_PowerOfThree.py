# Easy 326. Power of Three
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3^x.
# Constraints: -2^31 <= n <= 2^31 - 1

class Solution:
    MAX_3_POW = 3**19  # MAX_3_POW < 2^31, 2^31 < 3*MAX_3_POW
    def isPowerOfThree(self, n):
        return Solution.MAX_3_POW % n == 0

########## TEST ########################################################################################################
sln = Solution()
print(sln.isPowerOfThree(n=1))
print(sln.isPowerOfThree(n=3))
print(sln.isPowerOfThree(n=-3))
print(sln.isPowerOfThree(n=3**3))
print(sln.isPowerOfThree(n=-3**15))
print(sln.isPowerOfThree(n=123456))