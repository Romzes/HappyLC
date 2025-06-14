"""
1493. (Medium) Longest Subarray of 1's After Deleting One Element
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.
!!! НУЖНО ОБЯЗАТЕЛЬНО УДАЛИТЬ 1 ЭЛЕМЕНТ !!!

Constraints:
  1 <= nums.length <= 10^5
  nums[i] is either 0 or 1.
"""
from typing import List

# Runtime 423 ms , Beats 93.00% of users with Python3
# Memory 19.49 MB , Beats 94.22% of users with Python3
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j0 = -1  # индекс последнего 0
        max_sum1 = sum1 = 0  # ...011101(1)... => sum1 = 5
        for i, v in enumerate(nums):
            if v == 1:
                sum1 += 1
            else:
                max_sum1 = max(max_sum1, sum1)
                sum1 = i - j0 - 1
                j0 = i
        return min(max(max_sum1, sum1), len(nums)-1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j0 = -1  # индекс последнего 0
        max_sum1 = sum1 = 0  # ...011101(1)... => sum1 = 5
        for i, v in enumerate(nums):
            if v == 1:
                sum1 += 1
                max_sum1 = max(max_sum1, sum1)
            else:
                sum1 = i - j0 - 1
                j0 = i
        if j0 == -1: max_sum1 -= 1  # нулей нет в массиве nums => нужно обязательно удалить одну единицу
        return max_sum1


# Runtime 402 ms , Beats 99.67%  ;  Memory 20.04 MB , Beats 66.82%
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_sum1 = prev1 = sum1 = 0  # ...0111011... => prev1 = 3, sum1 = 5
        for v in nums:
            if v == 1:
                sum1 += 1
            else:
                if sum1 > max_sum1: max_sum1 = sum1
                prev1 = sum1 = sum1 - prev1
        return min(max(max_sum1, sum1), len(nums) - 1)


### ЭТАЛОННОЕ РЕШЕНИЕ ДЛЯ СОБЕСА
# Runtime 43 ms , Beats 81.15%  ;  Memory 21.92 MB , Beats 7.66%
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        has_zero = False
        res = 0
        cnt_tot = cnt = 0  # cnt_tot >= cnt
        for a in nums:
            # пример: nums = .. 0 1 1 1 0 [cnt = 1 1] a .. ; cnt_tot = 5, cnt = 2
            if a == 1:
                cnt += 1
                cnt_tot += 1
            else:
                # nums = .. 0 1 1 1 0 1 1 0 .. ; cnt_tot = 3, cnt = 0
                has_zero = True
                cnt_tot = cnt
                cnt = 0
            res = max(res, cnt_tot)
        if not has_zero: res = len(nums)-1
        return res


sln = Solution()
print(sln.longestSubarray(nums=[1,1,0,1]))  # Output: 3

sln = Solution()
print(sln.longestSubarray(nums=[0,1,1,1,0,1,1,0,1]))  # Output: 5

sln = Solution()
print(sln.longestSubarray(nums=[1,1,1]))  # Output: 2

sln = Solution()
print(sln.longestSubarray(nums=[0,0,0]))  # Output: 0

sln = Solution()
print(sln.longestSubarray(nums=[1,1,1,0,1,1,0]))  # Output: 5