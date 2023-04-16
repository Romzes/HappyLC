# Medium 198. House Robber
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums):
        n = len(nums)
        if n <= 2: return max(nums)
        res = n * [None]
        res[0] = nums[0]; res[1] = max(nums[0], nums[1])
        for i in range(2, n): res[i] = max(res[i-1], nums[i] + res[i-2])
        return res[-1]

class Solution:
    def rob(self, nums):
        lng = len(nums)
        if lng <= 2: return max(nums)
        a = nums[0]; b = max(a, nums[1])
        for i in range(2, lng): a, b = b, max(b, a + nums[i])
        return b

sln = Solution()
print(sln.rob(nums=[1,2,3,1]))

sln = Solution()
print(sln.rob(nums=[2,7,9,3,1]))