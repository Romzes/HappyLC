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
        # Первое ТУПОЕ решение Runtime = 452 ms , Beats 87.75% of users with Python3
        max_lng = 0
        i0 = j1 = j2 = None
        for i, v in enumerate(nums):
            if v == 1:
                if j1 is None: j1 = i
                j2 = i
                lng = j2 - j1 + 1
                if i0 is not None and j1 < i0 < j2: lng -= 1
                max_lng = max(max_lng, lng)
            elif v == 0 and i0 is None:
                i0 = i
            else:
                j1, j2 = (i0+1, i-1) if i0 < i-1 else (None, None)
                i0 = i
        if max_lng > 0 and i0 is None: max_lng -= 1
        return max_lng

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i0 = -1   # индекс последнего 0
        lng1 = 0  # кол-во единиц до i0 и на отрезке [i0; i] ; lng1 = 3 для  ... , 0, 1, 0 i0, 1, 1 i, ...
        max_lng = 0
        for i, v in enumerate(nums):
            if v == 1:
                lng1 += 1
                max_lng = max(max_lng, lng1)
            if v == 0:
                lng1 = i - i0 - 1
                i0 = i
        if max_lng > 0 and i0 == -1: max_lng -= 1
        return max_lng

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