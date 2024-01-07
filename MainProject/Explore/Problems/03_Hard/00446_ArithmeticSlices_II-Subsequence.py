"""
446. (Hard) Arithmetic Slices II - Subsequence
Given an integer array nums, return the number of all the arithmetic subsequences of nums.
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
  For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
  For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
  For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.
Constraints:
  1  <= nums.length <= 1000
  -2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3: return 0
        dp = [{} for _ in range(N)]
        dp[1][nums[1]-nums[0]] = 1
        # dp[i][d] = кол-во разных d-прогрессий длины >= 2, которые заканчиваются в точке nums[i]
        s = 0
        for i in range(2, N):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = dp[j].get(d, 0)  # кол-во разных d-прогрессий длины >= 2, которые заканчиваются в точке nums[j]
                s += cnt  # кол-во разных d-прогрессий длины >= 3, у которых последние два члена nums[j], nums[i]
                dp[i][d] = dp[i].get(d, 0) + cnt + 1  # +1 это d-прогрессия длины=2 nums[j], nums[i]
        # print(dp)
        return s

sln = Solution()
print(sln.numberOfArithmeticSlices(nums=[2,4,6,8,10]))

sln = Solution()
print(sln.numberOfArithmeticSlices(nums=[7,7,7,7,7]))
