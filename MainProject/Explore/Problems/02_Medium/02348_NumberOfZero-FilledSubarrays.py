"""
2348 (Medium) Number of Zero-Filled Subarrays
Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
  1 <= nums.length <= 10^5
  -10^9 <= nums[i] <= 10^9
"""

from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = cnt = 0
        for a in nums:
            if a != 0:
                cnt = 0
            else:
                cnt += 1
                res += cnt
        return res


sln = Solution()  # Example 1
print(sln.zeroFilledSubarray(nums=[1,3,0,0,2,0,0,4]))  # Output: 6
""" Explanation:
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
"""

sln = Solution()  # Example 2
print(sln.zeroFilledSubarray(nums=[0,0,0,2,0,0]))  # Output: 9
""" Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
"""

sln = Solution()  # Example 3
print(sln.zeroFilledSubarray(nums = [2,10,2019]))  # Output: 0
