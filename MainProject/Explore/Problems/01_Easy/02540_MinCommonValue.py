"""
2540 (Easy) Minimum Common Value
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays.
If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
"""
from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i1 = i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            v1, v2 = nums1[i1], nums2[i2]
            if v1 == v2: return v1
            if v1 < v2: i1 += 1
            else: i2 += 1
        return -1

sln = Solution()
print(sln.getCommon(nums1=[1,2,3], nums2=[2,4]))

sln = Solution()
print(sln.getCommon(nums1=[1,2,3,6], nums2=[2,3,4,5]))