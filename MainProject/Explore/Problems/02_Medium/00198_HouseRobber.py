# Medium 198. House Robber
"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m == 1: return nums[0]
        # dp[i] = макс сумма украденного из домов: 0,1, ... i
        dp = len(nums) * [0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, m):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

sln = Solution()
print(sln.rob(nums=[1,2,3,1]))

sln = Solution()
print(sln.rob(nums=[2,7,9,3,1]))