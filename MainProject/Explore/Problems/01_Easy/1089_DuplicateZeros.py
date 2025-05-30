# 1089 (Easy) Duplicate Zeros
"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.

Constraints:
  1 <= arr.length <= 104
  0 <= arr[i] <= 9
"""

from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        lng = len(arr)
        sz = 0
        for i2, a in enumerate(arr):
            sz += (2 if a == 0 else 1)
            if sz >= lng: break
        j = lng - 1  # destination index
        if sz > lng:
            i2 -= 1
            arr[j] = 0
            j -= 1
        for i in range(i2, -1, -1):
            if arr[i] == 0:
                arr[j] = arr[j-1] = 0
                j -= 2
            else:
                arr[j] = arr[i]
                j -= 1


arr = [1,0,2,3,0,4,5,0]
sln = Solution()
sln.duplicateZeros(arr)
print(arr)

arr = [1,2,3]
sln = Solution()
sln.duplicateZeros(arr)
print(arr)

arr = [1,0,2,3,0,0,5,0]
sln = Solution()
sln.duplicateZeros(arr)
print(arr)
