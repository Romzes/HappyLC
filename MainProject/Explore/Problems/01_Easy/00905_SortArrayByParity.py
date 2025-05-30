# 905 (Easy) Sort Array By Parity
"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
Constraints:
  1 <= nums.length <= 5000
  0 <= nums[i] <= 5000
"""

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)
        # nums[0,..,i-1] - четные ; nums[j,...len(nums)-1] - нечетные
        while i < j-1:
            if nums[i] % 2 == 0:
                i += 1
            else:
                j -= 1
                nums[j], nums[i] = nums[i], nums[j]  # nums[j] = нечетное
        return nums


sln = Solution()
print(sln.sortArrayByParity(nums=[3,1,2,4]))

sln = Solution()
print(sln.sortArrayByParity(nums=[0]))