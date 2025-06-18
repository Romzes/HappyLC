# 217 (Easy) Contains Duplicate
"""
Given an integer array nums,
return true if any value appears at least twice in the array, and return false if every element is distinct.

Constraints:
  1 <= nums.length <= 10^5
  -10^9 <= nums[i] <= 10^9
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return not(len(set(nums)) == len(nums))  # самое быстрое !!!
        s = set()
        for a in nums:
            if a in s: return True
            s.add(a)
        return False


sln = Solution()
print(sln.containsDuplicate(nums=[1,2,3,1]))  # Output: true

sln = Solution()
print(sln.containsDuplicate(nums=[1,2,3,4]))  # Output: false

sln = Solution()
print(sln.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))  # Output: true