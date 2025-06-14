# 153 (Medium) Find Minimum in Rotated Sorted Array
"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
  [4,5,6,7,0,1,2] if it was rotated 4 times.
  [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time

!!! массив nums может быть НЕ сдвинут !!!

Constraints:
  n == nums.length
  1 <= n <= 5000
  -5000 <= nums[i] <= 5000
  All the integers of nums are unique.
  nums is sorted and rotated between 1 and n times.
"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 18.26 MB  Beats 9.45%
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while True:
            if nums[l] <= nums[r]: return nums[l]  # nums[l..r] монотонно возрастает + случай когда l = r
            # выполнено: l < r
            m = (l + r) // 2  # l <= m < r !!! ВАЖНО что m < r => nums[m] != nums[r]
            if nums[m] > nums[r]:
                l = m + 1
            else:  # nums[m] < nums[r]
                r = m


sln = Solution()
print(sln.findMin(nums=[3,4,5,1,2]))  # Output: 1

sln = Solution()
print(sln.findMin(nums=[4,5,6,7,0,1,2]))  # Output: 0

sln = Solution()
print(sln.findMin(nums=[11,13,15,17]))  # Output: 11

sln = Solution()
print(sln.findMin(nums=[2,1]))  # Output: 1