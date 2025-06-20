# 2605 (Easy) Form Smallest Number From Two Digit Arrays
"""
Given two arrays of unique digits nums1 and nums2,
return the smallest number that contains at least one digit from each array.

Constraints:
  1 <= nums1.length, nums2.length <= 9
  1 <= nums1[i], nums2[i] <= 9
  All digits in each array are unique.
"""

from typing import List

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 17.95 MB  Beats 11.03%
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        set1, set2 = set(nums1), set(nums2)
        set_inter = set1.intersection(set2)
        if set_inter: return min(set_inter)
        m1, m2 = min(set1), min(set2)
        return 10*m1 + m2 if m1 < m2 else 10*m2+m1


sln = Solution()
print(sln.minNumber(nums1=[4,1,3], nums2=[5,7]))  # Output: 15
# Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.

sln = Solution()
print(sln.minNumber(nums1=[3,5,2,6], nums2=[3,1,7]))  # Output: 3
# Explanation: The number 3 contains the digit 3 which exists in both arrays.