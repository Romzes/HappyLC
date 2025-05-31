# 487 (Medium) Max Consecutive Ones II
"""
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.
Constraints:
  1 <= nums.length <= 10^5
  nums[i] is either 0 or 1
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = total_ones = part_ones = 0
        # инварианты цикла:
        # 1) total_ones >= part_ones
        # nums[i-total_ones .. i-1] = 0,..0,1,0,..,0 и вторая группа нулей содержит part_ones нулей
        for i, a in enumerate(nums):
            if a == 1:
                total_ones += 1
                part_ones += 1
            else:
                total_ones = part_ones + 1
                part_ones = 0
            res = max(res, total_ones)
        return res


sln = Solution()
print(sln.findMaxConsecutiveOnes(nums=[1,0,1,1,0]))

sln = Solution()
print(sln.findMaxConsecutiveOnes(nums=[1,0,1,1,0,1]))