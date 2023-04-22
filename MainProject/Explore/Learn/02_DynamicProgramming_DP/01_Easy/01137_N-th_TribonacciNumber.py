# Easy 1137. N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n):
        t0, t1, t2 = 0, 1, 1
        if n <= 2: return (t0, t1, t2)[n]
        for i in range(n-2): t0, t1, t2 = t1, t2, t0+t1+t2
        return t2

sln = Solution()
print(sln.tribonacci(n=0))
sln = Solution()
print(sln.tribonacci(n=1))
sln = Solution()
print(sln.tribonacci(n=2))
sln = Solution()
print(sln.tribonacci(n=3))
sln = Solution()
print(sln.tribonacci(n=4))
sln = Solution()
print(sln.tribonacci(n=25))
