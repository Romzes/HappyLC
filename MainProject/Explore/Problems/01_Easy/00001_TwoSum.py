# Easy 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 18.92 MB  Beats 33.94%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stat = {}
        for i, a in enumerate(nums):
            j = stat.get(target-a)
            if j is not None: return [j, i]
            stat[a] = i


sln = Solution()
print(sln.twoSum(nums=[2,7,11,15], target=9))  # Output: [0,1]

sln = Solution()
print(sln.twoSum(nums=[3,2,4], target=6))  # Output: [1,2]

sln = Solution()
print(sln.twoSum(nums=[3,3], target=6))  # Output: [0,1]