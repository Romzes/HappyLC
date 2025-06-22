# 35 (Easy) Search Insert Position
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Constraints:
  1 <= nums.length <= 10^4
  -10^4 <= nums[i] <= 10^4
  nums contains distinct values sorted in ascending order.
  -10^4 <= target <= 10^4
"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 18.62 MB  Beats 25.67%
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            v = nums[m]
            if target == v: return m
            if target < v: r = m-1
            else: l = m+1
        return l  # l = r+1

sln = Solution()
print(sln.searchInsert(nums=[1,3,5,6], target=5))  # Output: 2

sln = Solution()
print(sln.searchInsert(nums=[1,3,5,6], target=2))  # Output: 1

sln = Solution()
print(sln.searchInsert(nums=[1,3,5,6], target=7))  # Output: 4