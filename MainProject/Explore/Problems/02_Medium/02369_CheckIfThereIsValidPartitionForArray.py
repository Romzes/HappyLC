"""
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.
We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:
  The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
  The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
  The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1.
  For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.
Constraints:
  2 <= nums.length <= 10^5
  1 <= nums[i] <= 10^6
"""

from typing import List
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums); dp = N * [False]; dp[1] = (nums[0] == nums[1])
        if N > 2:
            dp[2] = (nums[0] == nums[1] and nums[1] == nums[2]) or (nums[1] - nums[0] == 1 and nums[2] - nums[1] == 1)
        for i in range(3, N):
            if nums[i-1] == nums[i] and dp[i-2]: dp[i] = True
            elif nums[i-2] == nums[i-1] and nums[i-1] == nums[i] and dp[i-3]: dp[i] = True
            elif nums[i-1] - nums[i-2] == 1 and nums[i] - nums[i-1] == 1 and dp[i-3]: dp[i] = True
        return dp[-1]

sln = Solution()
print(sln.validPartition(nums=[4,4,4,5,6]))

sln = Solution()
print(sln.validPartition(nums=[1,1,1,2]))

sln = Solution()
print(sln.validPartition(nums=[1,2,3]))