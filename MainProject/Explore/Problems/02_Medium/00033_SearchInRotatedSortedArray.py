# 33 (Medium) Search in Rotated Sorted Array
"""
There is an integer array nums sorted in ascending order (with DISTINCT values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Constraints:
  1 <= nums.length <= 5000
  -10^4 <= nums[i] <= 10^4
  All values of nums are UNIQUE.
  nums is an ascending array that is possibly rotated.
  -10^4 <= target <= 10^4
"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.94 MB  Beats 91.01%
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        return -1

    def search_core(self, nums, target, l, r):
        # nums[l..r] sorted asc
        while l <= r:
            mi = (l+r) // 2
            mv = nums[mi]
            if target == mv: return mi
            if target < mv: r = mi-1
            else: l = mi+1
        return -1


sln = Solution()
print(sln.search(nums=[4,5,6,7,0,1,2], target=0))  # Output: 4

sln = Solution()
print(sln.search(nums=[4,5,6,7,0,1,2], target=3))  # Output: -1

sln = Solution()
print(sln.search(nums=[1], target=0))  # Output: -1