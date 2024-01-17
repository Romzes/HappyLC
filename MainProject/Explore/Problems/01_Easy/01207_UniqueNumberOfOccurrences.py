"""
1207. (Easy) Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
Constraints:
  1 <= arr.length <= 1000
  -1000 <= arr[i] <= 1000
"""

from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt1 = Counter(arr)
        return len(cnt1) == len(set(cnt1.values()))

sln = Solution()
print(sln.uniqueOccurrences(arr=[1,2,2,1,1,3]))

sln = Solution()
print(sln.uniqueOccurrences(arr=[1,2]))

sln = Solution()
print(sln.uniqueOccurrences(arr=[-3,0,1,-3,1,1,1,-3,10,0]))