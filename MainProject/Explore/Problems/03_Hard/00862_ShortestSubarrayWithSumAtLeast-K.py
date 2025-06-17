# 862 (Hard) Shortest Subarray with Sum at Least K
"""
Given an integer array nums and an integer k,
return the length of the shortest non-empty subarray of nums with a sum of at least k.
If there is no such subarray, return -1.
A subarray is a contiguous part of an array.

Constraints:
  1 <= nums.length <= 10^5
  -10^5 <= nums[i] <= 10^5
  1 <= k <= 10^9
"""

from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lng = n+1
        i, j, s = 0, 0, nums[0]
        while True:
            # 0 <= i <= j < n, s[k]=sum(nums[i,k]) > 0 где i <= k < j, s = sum(nums[i..j])
            if s <= 0:
                i = j = j+1
                if j == n: break
                s = nums[j]
            elif k <= s:
                lng = min(lng, j - i + 1)
                if lng == 1: return lng
                s -= nums[i]
                i += 1
            else:
                # 0 < s < k
                j += 1
                if j == n: break
                s += nums[j]

        if lng == n+1: lng = -1
        return lng


sln = Solution()
print(sln.shortestSubarray(nums=[1], k=1))  # Output: 1

sln = Solution()
print(sln.shortestSubarray(nums=[1,2], k=4))  # Output: -1

sln = Solution()
print(sln.shortestSubarray(nums=[2,-1,2], k=3))  # Output: 3

sln = Solution()
print(sln.shortestSubarray(nums=[84,-37,32,40,95], k=167))  # Output: 3