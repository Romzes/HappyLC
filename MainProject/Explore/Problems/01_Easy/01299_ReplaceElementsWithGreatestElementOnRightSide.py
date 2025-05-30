# 1299 (Easy) Replace Elements with Greatest Element on Right Side
"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.
After doing so, return the array.
Constraints:
  1 <= arr.length <= 104
  1 <= arr[i] <= 105
"""

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r_max = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            arr[i], r_max = r_max, max(r_max, arr[i])
        arr[-1] = -1
        return arr


sln = Solution()
print(sln.replaceElements(arr=[17,18,5,4,6,1]))

sln = Solution()
print(sln.replaceElements(arr=[400]))