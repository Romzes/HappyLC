# 896 (Easy) Monotonic Array
"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""

from typing import List

# Runtime = 24 ms  Beats 73.08%  ;  Memory = 29.25 MB  Beats 22.28%
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True
        dir = None
        for i in range(1, len(nums)):
            delta = nums[i] - nums[i-1]
            if delta == 0: continue
            if dir is None:
                dir = delta > 0
            elif dir ^ (delta > 0) == 1:
                return False

        return True


sln = Solution()
print(sln.isMonotonic(nums=[1,2,2,3]))  # Output: true

sln = Solution()
print(sln.isMonotonic(nums=[6,5,4,4]))  # Output: true

sln = Solution()
print(sln.isMonotonic(nums=[1,3,2]))  # Output: false

sln = Solution()
print(sln.isMonotonic(nums=[0,0,0,4]))  # Output: false