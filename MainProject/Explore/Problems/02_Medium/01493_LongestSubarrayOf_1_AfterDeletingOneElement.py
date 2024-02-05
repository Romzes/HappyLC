"""
1493. (Medium) Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.
Constraints:
  1 <= nums.length <= 10^5
  nums[i] is either 0 or 1.
"""
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i0 = None  # индекс последнего 0
        max_sum1 = prev1 = sum1 = 0  # ...0111011... => prev1 = 3, sum1 = 5
        for i, v in enumerate(nums):
            if v == 1:
                sum1 += 1
            else:
                max_sum1 = max(max_sum1, sum1)
                i0 = i
                prev1 = sum1 = sum1 - prev1
        max_sum1 = max(max_sum1, sum1)
        if i0 is None: max_sum1 -= 1  # нулей нет в массиве nums => нужно обязательно удалить одну единицу
        return max_sum1

### ЭТАЛОННОЕ РЕШЕНИЕ ДЛЯ СОБЕСА
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i0 = None  # индекс последнего 0
        max_sum1 = prev1 = sum1 = 0  # ...0111011... => prev1 = 3, sum1 = 5
        for i, v in enumerate(nums):
            if v == 1:
                sum1 += 1
                max_sum1 = max(max_sum1, sum1)
            else:
                i0 = i
                prev1 = sum1 = sum1 - prev1
        if i0 is None: max_sum1 -= 1  # нулей нет в массиве nums => нужно обязательно удалить одну единицу
        return max_sum1

sln = Solution()
print(sln.longestSubarray(nums=[0,0,0]))

sln = Solution()
print(sln.longestSubarray(nums=[1,1,1]))

sln = Solution()
print(sln.longestSubarray(nums=[1,1,0,1]))

sln = Solution()
print(sln.longestSubarray(nums=[0,1,1,1,0,1,1,0,1]))

sln = Solution()
print(sln.longestSubarray(nums=[1,1,1,0,1,1,0]))