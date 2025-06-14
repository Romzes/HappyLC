# 53 (Medium) Maximum Subarray
"""
Given an integer array nums, find the with the largest sum, and return its sum.

Constraints:
  1 <= nums.length <= 10^5
  -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List

# Runtime = 59 ms  Beats 61.99%  ;  Memory = 32.04 MB  Beats 66.37%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = -float('inf')
        i = 0
        while i < n:
            j = i
            s = 0
            while j < n:
                s += nums[j]
                res = max(res, s)
                j = j + 1
                if s <= 0: break
            i = j
        return res

# Runtime = 55ms  Beats 68.50%  ;  Memory = 32.88 MB  Beats 22.52%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        s = 0
        for a in nums:
            s += a
            res = max(res, s)
            if s <= 0: s = 0
        return res


sln = Solution()
print(sln.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6, subarray=[4,-1,2,1]

sln = Solution()
print(sln.maxSubArray(nums=[1]))  # Output: 1, subarray=[1]

sln = Solution()
print(sln.maxSubArray(nums=[5,4,-1,7,8]))  # Output: 23, subarray=[5,4,-1,7,8]