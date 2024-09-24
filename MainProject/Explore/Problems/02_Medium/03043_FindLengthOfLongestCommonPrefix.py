"""
3043. (Medium) Find the Length of the Longest Common Prefix
You are given two arrays with positive integers arr1 and arr2.
A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit.
For example, 123 is a prefix of the integer 12345, while 234 is not.
A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b.
For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.
You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.
Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.
"""
from typing import List

# примитивное решение
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        for i in range(len(arr1)): arr1[i] = str(arr1[i])
        for i in range(len(arr2)): arr2[i] = str(arr2[i])
        max_len = 0
        for a1 in arr1:
            if len(a1) < max_len: continue
            for a2 in arr2:
                if len(a2) < max_len: continue
                for i in range(min(len(a1), len(a2))):
                    if a1[i] != a2[i]: break
                    max_len = max(max_len, i+1)
        return max_len

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # s1, s2 = sum(len(a1) for a1 in arr1), sum(len(a2) for a2 in arr2)
        # if s1 > s2: arr1, arr2 = arr2, arr1
        set2 = set()
        for a2 in arr2:
            a2 = str(a2)
            for i in range(1, len(a2)+1): set2.add(a2[0:i])
        max_len = 0
        for a1 in arr1:
            a1 = str(a1)
            if len(a1) <= max_len: continue
            for i in range(len(a1), max_len, -1):
                if a1[0:i] in set2:
                    max_len = i
                    break
        return max_len

sln = Solution()
arr1 = [1,10,100]
arr2 = [1000]
print(sln.longestCommonPrefix(arr1, arr2))

sln = Solution()
arr1 = [1,2,3]
arr2 = [4,4,4]
print(sln.longestCommonPrefix(arr1, arr2))

sln = Solution()
arr1 = [3,26]
arr2 = [7,16]
print(sln.longestCommonPrefix(arr1, arr2))

sln = Solution()
arr1 = [10]
arr2 = [17, 11]
print(sln.longestCommonPrefix(arr1, arr2))

sln = Solution()
arr1 = [13,27,45]
arr2 = [21,27,48]
print(sln.longestCommonPrefix(arr1, arr2))



