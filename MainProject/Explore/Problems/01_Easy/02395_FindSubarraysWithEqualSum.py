# 2395 (Easy) Find Subarrays With Equal Sum
"""
Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum.
Note that the two subarrays must begin at different indices.
Return true if these subarrays exist, and false otherwise.
A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
  2 <= nums.length <= 1000
  -10^9 <= nums[i] <= 10^9
"""

from typing import List

# Runtime = 0ms  Beats 100.00%  ;  Memory = 17.74MB  Beats 93.20%
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for i in range(len(nums)-1):
            s = nums[i] + nums[i+1]
            if s in sums: return True
            sums.add(s)
        return False


sln = Solution()
print(sln.findSubarrays(nums=[4,2,4]))  # Output: true

sln = Solution()
print(sln.findSubarrays(nums=[1,2,3,4,5]))  # Output: false

sln = Solution()
print(sln.findSubarrays(nums=[0,0,0]))  # Output: true