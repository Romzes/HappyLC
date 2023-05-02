# Easy 1822. Sign of the Product of an Array
# There is a function signFunc(x) that returns:
#   1 if x is positive.
#   -1 if x is negative.
#   0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).

class Solution:
    def arraySign(self, nums):
        p = 1
        for v in nums:
            if v == 0: return 0
            p *= (1 if v > 0 else -1)  # умножение - медленная операция
        return p

class Solution:
    def arraySign(self, nums):
        cnt = 0
        for v in nums:
            if v == 0: return 0
            if v < 0: cnt += 1
        return 1 if (cnt % 2 == 0) else -1

sln = Solution()
print(sln.arraySign(nums=[-1,-2,-3,-4,3,2,1]))

sln = Solution()
print(sln.arraySign(nums=[1,5,0,2,-3]))

sln = Solution()
print(sln.arraySign(nums=[-1,1,-1,1,-1]))