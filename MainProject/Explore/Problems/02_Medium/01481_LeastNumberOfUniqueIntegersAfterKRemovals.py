"""
1481 (Medium) Least Number of Unique Integers after K Removals
Given an array of integers arr and an integer k.
Find the least number of unique integers after removing exactly k elements.
"""
from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        values = sorted(Counter(arr).values()); n = len(values); s = 0
        for v in values:
            s += v
            if s <= k: n -= 1
            else: break
        return n

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        values = sorted(Counter(arr).values()); n = len(values)
        for v in values:
            k -= v
            if k < 0: break
            n -= 1
        return n

sln = Solution()
print(sln.findLeastNumOfUniqueInts(arr=[5,5,4], k=1))

sln = Solution()
print(sln.findLeastNumOfUniqueInts(arr=[4,3,1,1,3,3,2], k=3))