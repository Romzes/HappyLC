# 81 (Medium) Search in Rotated Sorted Array II
"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that
the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain DUPLICATES.
Would this affect the runtime complexity? How and why?

Constraints:
  1 <= nums.length <= 5000
  -10^4 <= nums[i] <= 10^4
  nums is GUARANTEED to be rotated at some pivot.
  -10^4 <= target <= 10^4
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    return self.search_core(nums, target, l=l, r=m)
                l = m+1
            else: # nums[l] > nums[m]
                if nums[m] <= target <= nums[r]:
                    return self.search_core(nums, target, l=m, r=r)
                r = m-1
        return False

    def search_core(self, nums, target, l, r):
        # nums[l..r] sorted asc
        while l <= r:
            mi = (l+r) // 2
            mv = nums[mi]
            if target == mv: return True
            if target < mv: r = mi-1
            else: l = mi+1
        return False


sln = Solution()
print(sln.search(nums=[2,5,6,0,0,1,2], target=0))  # Output: true

sln = Solution()
print(sln.search(nums=[2,5,6,0,0,1,2], target=3))  # Output: false

sln = Solution()
print(sln.search(nums=[1,0,1,1,1], target=0))  # Output: true  ВАЖНОЕ ОТЛИЧИЕ ОТ задачи № 33 где unique-array