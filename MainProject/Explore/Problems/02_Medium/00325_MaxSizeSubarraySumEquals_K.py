"""
325. (Medium) Maximum Size Subarray Sum Equals k
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k.
If there is not one, return 0 instead.
"""

from typing import List
from collections import defaultdict

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_list = len(nums) * [None]; sum_dict = defaultdict(list)
        s = 0
        for i, v in enumerate(nums):
            s += v
            sum_list[i] = s
            sum_dict[s].append(i)
        max_len = 0
        for i in range(len(nums)):
            arr = sum_dict.get(k + (sum_list[i-1] if i > 0 else 0))
            if not arr: continue
            j = arr[-1]
            if j < i: continue
            max_len = max(max_len, j-i+1)
        return max_len

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_dict = defaultdict(list); s = 0
        for i, v in enumerate(nums): sum_dict[s:=s+v].append(i)
        max_len = 0; s = 0
        for i, v in enumerate(nums):
            arr = sum_dict.get(s+k)
            if arr and i <= arr[-1]: max_len = max(max_len, arr[-1] - i + 1)
            s += v
        return max_len

sln = Solution()
print(sln.maxSubArrayLen(nums=[1,-1,5,-2,3], k=3))

sln = Solution()
print(sln.maxSubArrayLen(nums=[-2,-1,2,1], k=1))