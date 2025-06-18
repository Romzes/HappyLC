# 80 (Medium) Remove Duplicates from Sorted Array II
"""
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
  1 <= nums.length <= 3 * 10^4
  -10^4 <= nums[i] <= 10^4
  nums is sorted in non-decreasing order.
"""

from typing import List

# Runtime = 82ms  Beats 73.43%  ;  Memory = 20.28 MB  Beats 96.20%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for a in nums:
            if j <= 1 or nums[j-2] != a:
                nums[j] = a
                j += 1
        return j


# Runtime = 78 ms  Beats 88.19%  ;  Memory = 20.49 MB  Beats 47.22%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 2
        for i in range(2, len(nums)):
            if nums[j-2] != nums[i]:
                nums[j] = nums[i]
                j += 1
        return j


sln = Solution()
nums = [1,1,1,2,2,3]
print(sln.removeDuplicates(nums))  # Output: 5, nums = [1,1,2,2,3,_]
print(nums)

sln = Solution()
nums = [0,0,1,1,1,1,2,3,3]
print(sln.removeDuplicates(nums))  # Output: 7, nums = [0,0,1,1,2,3,3,_,_]
print(nums)