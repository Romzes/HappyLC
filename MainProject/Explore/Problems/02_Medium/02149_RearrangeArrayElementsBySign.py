"""
2149 (Medium) Rearrange Array Elements by Sign
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should rearrange the elements of nums such that the modified array follows the given conditions:
  Every consecutive pair of integers have opposite signs.
  For all integers with the same sign, the order in which they were present in nums is preserved.
  The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
"""
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = len(nums)*[0]
        i, j = 0, 1
        for v in nums:
            if v > 0: res[i] = v; i += 2
            else: res[j] = v; j += 2
        return res

sln = Solution()
print(sln.rearrangeArray(nums=[3,1,-2,-5,2,-4]))

sln = Solution()
print(sln.rearrangeArray(nums=[-1,1]))