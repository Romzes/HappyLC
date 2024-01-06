"""
300. (Medium) Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.
Constraints:
  1 <= nums.length <= 2500
  -10^4 <= nums[i] <= 10^4
"""

class Solution:
    def lengthOfLIS(self, nums):
        lis = len(nums) * [1]
        for i, v in enumerate(nums):
            for j in range(i):
                if nums[j] < v: lis[i] = max(lis[i], 1+lis[j])
        return max(lis)

import bisect
class Solution:
    def lengthOfLIS(self, nums):
        dp = []
        for n in nums:
            insert_index = bisect.bisect_left(dp, n)
            if insert_index == len(dp): dp.append(n)
            else: dp[insert_index] = n
        return len(dp)

sln = Solution()
print(sln.lengthOfLIS(nums=[5,10,15,1]))

sln = Solution()
print(sln.lengthOfLIS(nums=[10,9,2,5,3,7,101,18]))

sln = Solution()
print(sln.lengthOfLIS(nums=[0,1,0,3,2,3]))

sln = Solution()
print(sln.lengthOfLIS(nums=[7,7,7,7,7,7,7]))

sln = Solution()
print(sln.lengthOfLIS(nums=[5]))