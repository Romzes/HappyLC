# Easy 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n):
        if n <= 2: return n
        a, b = 1, 2
        for k in range(3, n+1): a, b = b, a + b
        return b

sln = Solution()
print(sln.climbStairs(n=1))

sln = Solution()
print(sln.climbStairs(n=2))

sln = Solution()
print(sln.climbStairs(n=3))