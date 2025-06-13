# 1664 (Medium) Ways to Make a Fair Array
"""
You are given an integer array nums.
You can choose exactly one index (0-indexed) and remove the element.
Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:
  Choosing to remove index 1 results in nums = [6,7,4,1].
  Choosing to remove index 2 results in nums = [6,1,4,1].
  Choosing to remove index 4 results in nums = [6,1,7,4].

An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.
Return the number of indices that you could choose such that after the removal, nums is fair.

Constraints:
  1 <= nums.length <= 10^5
  1 <= nums[i] <= 10^4

"""

from typing import List

# Runtime = 244 ms  Beats 20.99%  ;  Memory = 28.8 2MB  Beats 17.49%
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1
        arr1, arr2 = n*[0], n*[0]
        arr1[0], arr1[1] = nums[0], nums[1]
        for i in range(2, n): arr1[i] = nums[i] + arr1[i-2]
        arr2[-2], arr2[-1] = nums[-2], nums[-1]
        for i in range(n-3, -1, -1): arr2[i] = nums[i] + arr2[i+2]
        ways = 0
        for i in range(n):
            # del index = i
            even = odd = 0
            if i % 2 == 0:
                j1, j2 = i-2, i+1  # even
                k1, k2 = i-1, i+2  # odd
            else:
                j1, j2 = i-1, i+2  # even
                k1, k2 = i-2, i+1  # odd
            if 0 <= j1: even += arr1[j1]
            if j2 < n: even += arr2[j2]
            if 0 <= k1: odd += arr1[k1]
            if k2 < n: odd += arr2[k2]
            if even == odd: ways += 1
        return ways

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        tot_even = tot_odd = 0
        for i, a in enumerate(nums):
            if i % 2 == 0: tot_even += a
            else: tot_odd += a
        curr_even = curr_odd = ways = 0
        for i, a in enumerate(nums):
            # del index = i
            if i % 2 == 0:
                curr_even += a
                even = (curr_even - a) + (tot_odd - curr_odd)
                odd = curr_odd + tot_even - curr_even
            else:
                curr_odd += a
                even = curr_even + (tot_odd - curr_odd)
                odd = (curr_odd - a) + (tot_even - curr_even)
            if even == odd: ways += 1
        return ways


sln = Solution()
print(sln.waysToMakeFair(nums=[2,1,6,4]))  # Output: 1

sln = Solution()
print(sln.waysToMakeFair(nums=[1,1,1]))  # Output: 3

sln = Solution()
print(sln.waysToMakeFair(nums=[1,2,3]))  # Output: 0