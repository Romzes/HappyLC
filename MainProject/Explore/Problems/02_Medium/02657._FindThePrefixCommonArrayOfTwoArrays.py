"""
2657 (Medium) Find the Prefix Common Array of Two Arrays
You are given two 0-indexed integer permutations A and B of length n.
A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
Return the prefix common array of A and B.
A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
Constraints:
  1 <= A.length == B.length == n <= 50
  1 <= A[i], B[i] <= n
  It is guaranteed that A and B are both a permutation of n integers.
"""
from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A); prefix = n * [None]; s1, s2 = set(), set()
        for i in range(n):
            a, b = A[i], B[i]
            d = 1 if a == b else int(a in s2) + int(b in s1)
            s1.add(a); s2.add(b)
            prefix[i] = d + (prefix[i-1] if i > 0 else 0)
        return prefix

sln = Solution()
print(sln.findThePrefixCommonArray(A=[1,3,2,4], B=[3,1,2,4]))

sln = Solution()
print(sln.findThePrefixCommonArray(A=[2,3,1], B=[3,1,2]))