"""
136 (Easy) Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Constraints:
  1 <= nums.length <= 3 * 10^4
  -3 * 10^4 <= nums[i] <= 3 * 10^4
  Each element in the array appears twice except for one element which appears only once.
"""

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for v in nums: s ^= v
        return s

sln = Solution()
print(sln.singleNumber(nums=[2,2,1]))

sln = Solution()
print(sln.singleNumber(nums=[4,1,2,1,2]))

sln = Solution()
print(sln.singleNumber(nums=[1]))