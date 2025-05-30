# 26 (Easy) Remove Duplicates from Sorted Array
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
  Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
  The remaining elements of nums are not important as well as the size of nums.
  Return k.

Constraints:
  1 <= nums.length <= 3 * 104
  -100 <= nums[i] <= 100
  nums is sorted in non-decreasing order.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[k] = nums[j]
                k += 1
        return k


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i, a in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k


sln = Solution()
nums = [1,1,2]
k = sln.removeDuplicates(nums=nums)
print(k)
print(nums)

sln = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = sln.removeDuplicates(nums=nums)
print(k)
print(nums)


