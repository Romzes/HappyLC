# Easy 1342. Number of Steps to Reduce a Number to Zero
# Given an integer num, return the number of steps to reduce it to zero.
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

### Simple
class Solution:
    def numberOfSteps(self, num):
        cnt = 0
        while num != 0:
            num = (num-1) if (num % 2) == 1 else int(num/2)
            cnt += 1
        return cnt

### Bit
class Solution:
    def numberOfSteps(self, num):
        cnt = 0
        while num != 0:
            num = (num & ~0x1) if (num & 0x1) else (num >> 1)
            cnt += 1
        return cnt

sln = Solution()
print(sln.numberOfSteps(num=14))

sln = Solution()
print(sln.numberOfSteps(num=8))

sln = Solution()
print(sln.numberOfSteps(num=123))