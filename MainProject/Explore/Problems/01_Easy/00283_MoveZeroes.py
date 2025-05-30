# 283 (Easy) Move Zeroes
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  # destination index
        for a in nums:
            if a != 0:
                nums[j] = a
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0

sln = Solution()
nums = [0,1,0,3,12]
sln.moveZeroes(nums=nums)
print(nums)

sln = Solution()
nums = [0]
sln.moveZeroes(nums=nums)
print(nums)