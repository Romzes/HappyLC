"""
209. (Medium) Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum >= target.
A subarray is a contiguous non-empty sequence of elements within an array.
If there is no such subarray, return 0 instead.
Constraints:
  1 <= target <= 10^9
  1 <= nums.length <= 10^5
  1 <= nums[i] <= 10^4
"""

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums); min_len = N+1; s = nums[0]; i = j = 0
        while j < N:
            # дано: i <= j < N
            if s < target:
                j += 1
                if j < N: s += nums[j]
                else: break
            else:
                # s >= target
                min_len = min(min_len, j-i+1)
                if min_len == 1: return 1
                if i < j: s -= nums[i]; i += 1
                else: j += 1; i = j
        if min_len == N+1: min_len = 0
        return min_len

sln = Solution()
print(sln.minSubArrayLen(target=7, nums=[2,3,1,2,4,3]))

sln = Solution()
print(sln.minSubArrayLen(target=4, nums=[1,4,4]))

sln = Solution()
print(sln.minSubArrayLen(target=11, nums=[1,1,1,1,1,1,1,1]))