# 941 (Easy) Valid Mountain Array
"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
  arr.length >= 3
  There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Constraints:
  1 <= arr.length <= 104
  0 <= arr[i] <= 104
"""

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3: return False
        i = 0
        while i < n-1 and arr[i] < arr[i+1]:
            i += 1
        # подмассив arr[0..i] монотонно возрастает
        if i in (0, n-1): return False
        j = n-1
        while arr[j-1] > arr[j]:
            j -= 1  # проверка j > 0 НЕ нужна
        # подмассив arr[j..n-1] монотонно убывает
        return i == j

sln = Solution()
print(sln.validMountainArray(arr=[2,1]))

sln = Solution()
print(sln.validMountainArray(arr=[3,5,5]))

sln = Solution()
print(sln.validMountainArray(arr=[0,3,2,1]))

sln = Solution()
print(sln.validMountainArray(arr=[1,2,3,4]))